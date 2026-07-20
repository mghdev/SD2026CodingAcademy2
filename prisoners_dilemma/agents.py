import random

class Agent:
    def __init__(self,name,func) -> None:
        self.policy = func
        self.name : str = name
    
    def __repr__(self):
        return f"Agent({self.name})"


def copycatPolicy(my_past_moves,opponent_past_moves):
    if opponent_past_moves:
        return opponent_past_moves[-1]
    return "C"

def dovePolicy(my_past_moves,opponent_past_moves):
    return "C"

def forgivenessPolicy(my_past_moves,opponent_past_moves):
    if opponent_past_moves:
        if random.random() > 0.9:
                return "C"   
        return opponent_past_moves[-1]
    return "C"

def grudgeHolderPolicy(my_past_moves, opponent_past_moves):
    if "B" in opponent_past_moves:
        return "B"
    return "C"

def maverickPolicy(my_past_moves,opponent_past_moves):
    if random.random() > 0.5:
        return "C"
    return "B"

def zodiacPolicy(my_past_moves,opponent_past_moves):
    if len(opponent_past_moves) > 2:
        if opponent_past_moves[-1] == "B":
            if opponent_past_moves[-2] == "B":
                if opponent_past_moves[-3] == "B":
                    if len(opponent_past_moves) % 100 != 0:
                        return "B"
                elif len(opponent_past_moves) % 25 != 0:
                    return "B"
            elif len(opponent_past_moves) % 3 != 0:
                return "B"
        if  len(my_past_moves) % 10 == 0:
            return "B"
    return "C"

def punisherPolicy(my_past_moves, opponent_past_moves):
    if not opponent_past_moves:
        return "C"
    if "B" in opponent_past_moves[-min(len(opponent_past_moves),3):]:
        return "B"
    return "C"

def ratPolicy(my_past_moves,opponent_past_moves):
    if opponent_past_moves:
        if len(opponent_past_moves) % 15 == 0:
            return "B"
        return opponent_past_moves[-1]
    return "C"

def wolfPolicy(my_past_moves,opponent_past_moves):
    return "B"

copycat = Agent("copycat",copycatPolicy)
dove = Agent("dove",dovePolicy)
forgiveness = Agent("forgiveness",forgivenessPolicy)
grudge_holder = Agent("grudge_holder",grudgeHolderPolicy)
maverick = Agent("maverick",maverickPolicy)
zodiac = Agent("zodiac",zodiacPolicy)
punisher = Agent("punisher",punisherPolicy)
rat = Agent("rat",ratPolicy)
wolf = Agent("wolf",wolfPolicy)

default_agents_all = [copycat,dove,forgiveness,grudge_holder,maverick,zodiac,punisher,rat,wolf]
default_agents_basic_only = [dove,wolf]
default_agents_unpredictable_only = [forgiveness,maverick]

def clamp(low,x,high):
    return max(min(x,high),low)

def randomDefaultAgents(n):
    n = clamp(0,n,len(default_agents_all))
    return random.sample(default_agents_all,n)