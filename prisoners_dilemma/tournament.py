from agents import Agent

NUM_ROUNDS = 200
POINTS_COOPERATE_SUCCESS = 3
POINTS_COOPERATE_FAILURE = 0
POINTS_BETRAY_SUCCESS = 5
POINTS_BETRAY_FAILURE = 1

class TournamentScore:
    def __init__(self,name,id) -> None:
        self.name : str = name
        self.id : int = id
        self.score : int = 0
        self.rounds_played : int = 0

def playRound(policy0,policy1,history):
    return [policy0(history[0],history[1]),policy1(history[1],history[0])]

def playManyRounds(policy0,policy1,n):
    history = [[],[]]
    for i in range(n):
        move_0,move_1 = playRound(policy0,policy1,history)
        history[0] += [move_0]
        history[1] += [move_1]
    return history

def scoreRounds(history: list[list[str]]):
    scores = [0,0]
    for move_0,move_1 in zip(history[0],history[1]):
        if move_0 == "C" and move_1 == "C":
            scores[0] += POINTS_COOPERATE_SUCCESS
            scores[1] += POINTS_COOPERATE_SUCCESS
        elif move_0 == "B" and move_1 == "B":
            scores[0] += POINTS_BETRAY_FAILURE
            scores[1] += POINTS_BETRAY_FAILURE
        elif move_0 == "B":
            scores[0] += POINTS_BETRAY_SUCCESS
            scores[1] += POINTS_COOPERATE_FAILURE
        else:
            scores[0] += POINTS_COOPERATE_FAILURE
            scores[1] += POINTS_BETRAY_SUCCESS
    return scores

def scoreAgents(agent_list:list[Agent], scores : list[TournamentScore],i:int,j:int,repetitions=NUM_ROUNDS):
    agent1 = agent_list[i]
    agent2 = agent_list[j]
    history = playManyRounds(agent1.policy,agent2.policy,repetitions)
    s = scoreRounds(history)
    scores[i].score += s[0]
    scores[j].score += s[1]
    scores[i].rounds_played += 1
    if i != j:
        scores[j].rounds_played += 1

def printScores(scores: list[TournamentScore]):
    for i in range(len(scores)):
        print(i+1,". ",scores[i].name," - ",scores[i].score," (",scores[i].rounds_played,")",sep="")

#========================    
def runTournament(agent_list: list[Agent], id_list: list[int]|None = None,num_rounds=NUM_ROUNDS) -> list[TournamentScore]:
    if not id_list:
        id_list = [i for i in range(len(agent_list))]
    scores = [TournamentScore(agent.name,id_list[i]) for i,agent in enumerate(agent_list)]
    
    for i in range(len(agent_list)):
        for j in range(i,len(agent_list)):
            s = scoreAgents(agent_list,scores,i,j,num_rounds)
    
    scores.sort(key=(lambda a : a.score),reverse=True)
    return scores

def main():
    from agents import default_agents_all,randomDefaultAgents
    print("\nTournament with all default agents:")
    printScores(runTournament(default_agents_all))
    
    print("\nTournament with 5 random default agents:")
    printScores(runTournament(randomDefaultAgents(5)))

if __name__ == "__main__":
    main()
