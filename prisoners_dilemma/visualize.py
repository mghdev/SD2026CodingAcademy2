from iterated import runIteratedTournament,Region,countPopuation,doBattles,replaceInhabitants
from agents import default_agents_all
from math import ceil,sqrt

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    pygame.init()

import threading,colorsys,random,time

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = [200,200,200,255]
TEXT_COLOR = [20,20,10,255]

INSET = 5
INFO_TEXT_RECT = pygame.Rect(0,480,720,240)
WORLD_RECT = pygame.Rect(0,0,480,480)
LEGEND_RECT = pygame.Rect(480,0,240,720)

FONT_SIZE = 32
DEFAULT_FONT = pygame.font.Font(None,FONT_SIZE)

def generateDistinctColors(n):
    colors = []
    for i in range(n):
        hue = i / n
        saturation = 0.7 
        lightness = 0.6 
        r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
        colors.append((int(r * 255), int(g * 255), int(b * 255), 255)) 
    return colors

def drawWorld(screen,world:list[Region],num_cols,agent_colors):
    row_size = WORLD_RECT.height // num_cols
    col_size = WORLD_RECT.width // num_cols
    for i,agent in enumerate(world):
        row = i//num_cols
        col = i%num_cols
        rect = [WORLD_RECT.left+col_size*col,
                WORLD_RECT.top+row_size*row,
                col_size,
                row_size]
        pygame.draw.rect(screen,agent_colors[agent],rect)
    pygame.draw.rect(screen,TEXT_COLOR,WORLD_RECT,2)

def drawLegend(screen,agent_list,agent_colors,population,*,font=DEFAULT_FONT):
    x = LEGEND_RECT.left + 2*INSET
    for i in range(len(agent_list)):
        y = LEGEND_RECT.top + 2*INSET + (FONT_SIZE+2*INSET)*i
        pygame.draw.rect(screen,agent_colors[i],(x,y,FONT_SIZE,FONT_SIZE))
        name_surface = font.render(f"{agent_list[i].name}: {population[i]}",True,TEXT_COLOR)
        screen.blit(name_surface,(x+FONT_SIZE+INSET,y+INSET))

def drawInfoText(screen,text,*,font=DEFAULT_FONT):
    lines = text.split("\n")
    for i,line in enumerate(lines):
        text_surface = font.render(line,True,TEXT_COLOR)
        screen.blit(text_surface,(INFO_TEXT_RECT.left+INSET,INFO_TEXT_RECT.top+INSET+i*FONT_SIZE))
    
def finishedText(generation):
    return f"Tournament is finished.\nUse arrow keys to move between generations.\nCurrent generation: {generation}"

def inProgressText(generation):
    return f"Running Tournament.\nCurrent generation: {generation}"

GENERATION_EVENT_PERIOD = 1
TOURNAMENT_FINISHED_EVENT = pygame.USEREVENT + 1
TOURNAMENT_GENERATION_FINISHED_EVENT = pygame.USEREVENT + 2
world_history = []
population_history = []
def backgroundIteratedTournament(agent_list,min_copies=100,num_generations=100,*,world_size=0):
    global world_history,population_history    
    num_agents = len(agent_list)
    if not world_size > 0:
        world_size = ceil(sqrt(num_agents*min_copies))
    region_count = world_size*world_size
    world = [Region(i,world_size) for i in range(region_count)]
    randomized = random.sample(range(region_count),region_count)
    
    next_agent = 0
    while len(randomized) > 0:
        i = randomized.pop()
        world[i].agent = next_agent
        next_agent = (next_agent+1)%num_agents
    
    world_history = []
    population_history = []
    for i in range(num_generations):
        world_history.append([region.agent for region in world])
        population_history.append(countPopuation(world,agent_list))
        world = replaceInhabitants(world,doBattles(world,agent_list))
        if i % GENERATION_EVENT_PERIOD == 0:
            pygame.event.post(pygame.event.Event(TOURNAMENT_GENERATION_FINISHED_EVENT,generation=i))
    pygame.event.post(pygame.event.Event(TOURNAMENT_FINISHED_EVENT))


def visualizeIteratedTournament(agent_list,*,min_copies=100,num_generations=100):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    agent_colors = generateDistinctColors(len(agent_list))
    font = pygame.font.Font(None,FONT_SIZE)
    info_text = inProgressText(0)
    
    world_size = ceil(sqrt(len(agent_list)*min_copies))
    tournament_thread = threading.Thread(
        target = backgroundIteratedTournament,
        args=(agent_list,min_copies,num_generations,),
        daemon=True
    )
    tournament_thread.start()
    tournament_in_progress = True
    current_generation = 0
    
    hold_delay = 0.5
    left_timestamp = 0
    right_timestamp = 0
    pressing_left = False
    pressing_right = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if not tournament_in_progress:
                    if event.key == pygame.K_LEFT:
                        pressing_left = True
                        left_timestamp = time.perf_counter()
                        current_generation = max(current_generation-1,0)
                        info_text = finishedText(current_generation)
                    elif event.key == pygame.K_RIGHT:
                        pressing_right = True
                        right_timestamp = time.perf_counter()
                        current_generation = min(current_generation+1,len(world_history)-1)
                        info_text = finishedText(current_generation)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressing_left = False
                elif event.key == pygame.K_RIGHT:
                    pressing_right = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == TOURNAMENT_FINISHED_EVENT:
                tournament_in_progress = False
                current_generation = len(world_history)-1
                info_text = finishedText(current_generation)
            elif event.type == TOURNAMENT_GENERATION_FINISHED_EVENT:
                if tournament_in_progress:
                    if event.generation > current_generation:
                        current_generation = event.generation
                        info_text = inProgressText(current_generation)
        
        if pressing_left:
            t = time.perf_counter()
            if t-left_timestamp > hold_delay:
                current_generation = max(current_generation-1,0)
                info_text = finishedText(current_generation)
        if pressing_right:
            t = time.perf_counter()
            if t-right_timestamp > hold_delay:
                current_generation = min(current_generation+1,len(world_history)-1)
                info_text = finishedText(current_generation)
        
        screen.fill(BACKGROUND_COLOR)
        
        drawInfoText(screen,info_text)
        if (tournament_in_progress and current_generation > 0) or not tournament_in_progress:
            drawLegend(screen,agent_list,agent_colors,population_history[current_generation])
            drawWorld(screen,world_history[current_generation],world_size,agent_colors)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def main():
    visualizeIteratedTournament(default_agents_all,num_generations=20)

if __name__ == "__main__":
    main()