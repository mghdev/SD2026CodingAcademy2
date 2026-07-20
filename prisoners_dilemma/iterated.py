from math import ceil,sqrt
from agents import Agent, default_agents_all,default_agents_basic_only
from tournament import runTournament,TournamentScore
from copy import copy
import random

def adjacentIndices(i:int,size:int) -> list[int]:
    up = -size
    down = +size
    right = +1
    left = -1
    up_left = up+left
    up_right = up+right
    down_left = down+left
    down_right = down+right
    
    if i == 0:  # top-left corner
        return [i+right, i+down, i+down_right]
    if i == size-1:  # top-right corner
        return [i+left,i+down_left,i+down]
    if i == size*(size-1):  # bottom-left corner
        return [i+up,i+up_right,i+right]
    if i == size*size-1:  # bottom-right corner
        return [i+up_left,i+up,i+left]
    
    if i < size:  # top row
        return [i+left,i+right,i+down_left,i+down,i+down_right]
    if i % size == 0:  # left column
        return [i+up,i+up_right,i+right,i+down,i+down_right]
    if i % size == (size-1):  # right column
        return [i+up_left,i+up,i+left,i+down_left,i+down]
    if i > size*(size-1):  # bottom row
        return [i+up_left,i+up,i+up_right,i+left,i+right]
    
    # default
    return [i+up_left,i+up,i+up_right,i+left,i+right,i+down_left,i+down,i+down_right]

class Region:
    def __init__(self,i:int,size:int) -> None:
        self.agent : int = 0
        self.index : int = i
        self.adjacent : list[int] = adjacentIndices(i,size)
    
    def __repr__(self):
        return f"Region({self.agent},{self.index},{self.adjacent})"

def addScore(totals: dict,id,points):
    if id in totals:
        totals[id] += points
    else:
        totals[id] = points

def doBattles(world: list[Region],agents:list[Agent],num_rounds = 25) -> list[list[TournamentScore]]:
    all_scores = []
    for region in world:
        participants = [agents[world[i].agent] for i in region.adjacent]
        participants.append(agents[region.agent])
        id_list = [i for i in region.adjacent]
        id_list.append(region.index)
        all_scores.append(runTournament(participants,id_list,num_rounds))
    return all_scores

def replaceInhabitants(world: list[Region],all_scores:list[list[TournamentScore]]):
    new_world = copy(world)
    for i in range(len(world)):
        items = [region_score.id for region_score in all_scores[i]]
        weights = [region_score.score for region_score in all_scores[i]]
        winner_home_idx = random.choices(items,weights)[0]
        new_world[i].agent = world[winner_home_idx].agent
    return new_world

def countPopuation(world: list[Region],agents: list[Agent]):
    agent_pop = [0 for _ in agents]
    for region in world:
        agent_pop[region.agent] += 1
    return agent_pop

def runIteratedTournament(agent_list:list[Agent],*,world_size=0,num_generations=100,min_copies=100):
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
    return world_history,population_history

def main():
    print(runIteratedTournament(default_agents_basic_only,num_generations=2,min_copies=10))

if __name__ == "__main__":
    main()