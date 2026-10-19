def scoring_alg(owned_list, agent_database, team_type):
    if team_type == "Anomaly":
        anom_agents = 0
        sup_agents = 0
        for i in owned_list:
            if agent_database[i]["class"] == "Anomaly":
                anom_agents += 1
        if anom_agents == 2 and sup_agents == 1:
            return "All good"
        elif anom_agents > 2:
            return "All good"
        else:
            return "Missing something"
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
            return "All good"
        else:
            return "Missing something"