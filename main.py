from agents_owned import *
from agents import *
from scoring import *

def main():
    # Asks for user input for characters and then scores them based on team make up
    owned_agents, team_type = add_user_agents()
    print("=" * 50)
    for i in owned_agents:
        print(f"{i} is an {agent_list[i]["element"]} {agent_list[i]["class"]} from {agent_list[i]["faction"]}")
    score = scoring_user(owned_agents, agent_list, team_type)
    if score != 0:
        print(f"Your team is missing {team_status_code[score]}")
        print("=" * 50)
        print(f"Current banner character: {banner_chr}")
        print(scoring_banner(score, banner_chr, agent_list))
    else:
        print(f"Your team is all good, banner character not needed")
    
if __name__ == "__main__":
    main()