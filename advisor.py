from agents import agent_list

owned_agents = []

adding_agents = True
while adding_agents:
    current_add = input("Please type in an agent name that you own: ")
    if current_add not in agent_list:
        print(f"{current_add} is not a valid agent, please try again")
    else:
        owned_agents.append(current_add)
        print(f"{current_add} has been added to the list")
        user_cont = input("Would you like to continue? (Y/N): ")
        if user_cont.upper() == "N":
            adding_agents = False

for i in owned_agents:
    print(f"{i} is an {agent_list[i]["element"]} {agent_list[i]["class"]} from {agent_list[i]["faction"]}")