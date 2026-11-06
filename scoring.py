team_status_code = {0: "All Good", 
               1: "Anomaly", 
               2: "Attack", 
               3: "Support", 
               4: "Stun"}

def scoring_user(owned_list, agent_database, team_type):
    # Assuming user entry is length of 3, scores their character as if they were a team in game
    if team_type == "Anomaly":
        anom_agents = 0
        sup_agents = 0
        for i in owned_list:
            if agent_database[i]["class"] == "Anomaly":
                anom_agents += 1
            elif agent_database[i]["class"] == "Support":
                sup_agents += 1
        if (anom_agents == 2 and sup_agents == 1) or anom_agents > 2:
            return 0
        else:
            if sup_agents < 1:
                return 3
            elif anom_agents < 2:
                return 1
    elif team_type == "DPS":
        dps_agent = 0
        stun_agent = 0
        sup_agent = 0
        for i in owned_list:
            if agent_database[i]["class"] == "Attack":
                dps_agent += 1
            elif agent_database[i]["class"] == "Stun":
                stun_agent += 1
            elif agent_database[i]["class"] == "Support":
                sup_agent += 1
        if dps_agent == 1 and stun_agent == 1 and sup_agent == 1:
            return 0
        else:
            if dps_agent < 1:
                return 2
            elif stun_agent < 1:
                return 4
            elif sup_agent < 1:
                return 3

def scoring_banner(team_status, banner_chr, agent_list):
    # Checks if the current banner character would fix a missing agent in user's team based on class
    if agent_list[banner_chr]["class"] == team_status_code[team_status]:
        return "Should get current banner character"
    else:
        return "Banner character not needed"