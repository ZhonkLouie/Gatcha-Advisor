from agents import agent_list

def add_user_agents():
    # Asks the user for 3 characters and checks if each character is valid
    owned_agents = []
    team_type = input("What type of team is this? (Anomaly/DPS): ")
    print("Valid agents:", list(agent_list.keys()))
    while len(owned_agents) < 3:
        current_add = input("Please type in the agent name that you own: ")
        if current_add not in agent_list:
            print(f"{current_add} is not a valid agent, please try again")
        else:
            owned_agents.append(current_add)
            print(f"{current_add} has been added to the list")
    return owned_agents, team_type