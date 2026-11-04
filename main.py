from agents_owned import add_user_agents
from agents import agent_list
from scoring import scoring_user, scoring_banner

def main():
    # Asks for user input for characters and then scores them based on team make up
    owned_agents, team_type = add_user_agents()
    print("=" * 50)
    for i in owned_agents:
        print(f"{i} is an {agent_list[i]["element"]} {agent_list[i]["class"]} from {agent_list[i]["faction"]}")
    score = scoring_user(owned_agents, agent_list, team_type)
    if score == 0:
        score = "All good"
    elif score == 1:
        score = "Missing an anomaly agent"
    elif score == 2:
        score = "Missing a dps agent"
    elif score == 3:
        score = "Missing a support agent"
    elif score == 4:
        score = "Missing a stun agent"
    print(f"Your team is... {score}")
    
if __name__ == "__main__":
    main()