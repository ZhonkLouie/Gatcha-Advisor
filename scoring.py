team_status_code = {0: "All Good", 
               1: "Missing an anomaly agent", 
               2: "Missing a dps agent", 
               3:"Missing a support agent", 
               4: "Missing a stun agent"}

def scoring_user(owned_list, agent_database, team_type):
    # Assuming user entry is length of 3, scores their character as if they were a team in game
    """
        Status Returns:
        0 = All Good
        1 = Missing Anomaly
        2 = Missing DPS
        3 = Missing Support
        4 = Missing Stun
    """
    if team_type == "Anomaly":
        anom_agents = 0
        sup_agents = 0
        for i in owned_list:
            if agent_database[i]["class"] == "Anomaly":
                anom_agents += 1
        if (anom_agents == 2 and sup_agents == 1) or anom_agents > 2:
            return 0
        else:
            if sup_agent < 1:
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

def scoring_banner(team_status, banner_chrs):
    # Checks if the current banner character would fix a missing agent in user's team
    if team_status == 0:
        return "Not needed"
    

    