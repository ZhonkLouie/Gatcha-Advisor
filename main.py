from agents_owned import add_user_agents
from agents import agent_list
from scoring import scoring_alg

def main():
    owned_agents, team_type = add_user_agents()
    for i in owned_agents:
        print(f"{i} is an {agent_list[i]["element"]} {agent_list[i]["class"]} from {agent_list[i]["faction"]}")
    score = scoring_alg(owned_agents, agent_list, team_type)
    print(f"Your team is... {score}")
    
main()