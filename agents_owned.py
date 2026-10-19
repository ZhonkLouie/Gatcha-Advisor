from agents import agent_list

def add_user_agents():
    owned_agents = []
    adding_agents = True
    team_type = input("What type of team is this? (Anomaly/DPS): ")
    while adding_agents:
        current_add = input("Please type in the agent name that you own: ")
        if current_add not in agent_list:
            print(f"{current_add} is not a valid agent, please try again")
        else:
            owned_agents.append(current_add)
            print(f"{current_add} has been added to the list")
            user_cont = input("Would you like to continue? (Y/N): ")
            if user_cont.upper() == "N":
                adding_agents = False
    return owned_agents, team_type