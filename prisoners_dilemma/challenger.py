from tournament import runTournament,printScores
from iterated import runIteratedTournament
from visualize import visualizeIteratedTournament
from agents import Agent, default_agents_all, default_agents_basic_only, default_agents_unpredictable_only, randomDefaultAgents

def cooperateOrBetray(my_past_moves,opponent_past_moves):
    return "B"

def main():
    my_agent = Agent("Snitch",cooperateOrBetray)
    tournament_participants = default_agents_all + [my_agent]
    printScores(runTournament(tournament_participants))
    
    visualizeIteratedTournament(tournament_participants,min_copies=10,num_generations=20)

if __name__ == "__main__":
    main()