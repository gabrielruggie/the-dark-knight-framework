from loguru import logger

'''
Class that generates a team id based on school name, grade level and team captain last name
'''
class GenerateTeamId:

    school_level_values = {"sr": 4000, "jr": 3000, "soph": 2000, "frosh": 1000}

    school_name_values = {"luke": 40, "ascension": 30, "giles": 20, "celestine": 10}

    team_cap_last_name = None

    team_church = None

    team_school_level = None

    def __calculate_captain_hash (cls, name: str):
        ascii_chars = [ord(letter) for letter in name]

        return sum(ascii_chars) % 100

    # Generates response that will be used by API
    def generate_team_spec_response (cls, team_name: str):
        return {"team_name": team_name.lower(),
                "team_id": cls.__calculate_team_id(team_name=team_name),
                "church": cls.team_church,
                "team_school_level": int(cls.team_school_level / 1000) if cls.team_school_level != None else 0,
                "cap_last_name": cls.team_cap_last_name
                }
    
    def __calculate_team_id (cls, team_name: str):
        team_name_low = team_name.lower()
        st_no_space = team_name_low.find("st.")
        st_w_space = team_name_low.find("st. ")

        if st_no_space != -1:
            return cls.__generate_hidden_values(team_name_low=team_name_low, st=st_no_space+3)
        elif st_w_space != -1:
            return cls.__generate_hidden_values(team_name_low=team_name_low, st=st_w_space+4)
        else:
            return cls.__generate_hidden_values(team_name_low=team_name_low)
    
    # Calculates team id based on the format below:
    # <OPTIONAL: St.> <SCHOOL NAME> <SCHOOL SENIORITY> <CAPTAIN LAST NAME> 
    # <OPTIONAL: St.> MUST have a period
    # Returns 0 if KeyErro is caught
    def __generate_hidden_values (cls, team_name_low: str, st=None):

        if st != None:
            cut_team_name_low = team_name_low[st:]
            split_name = cut_team_name_low.split(" ")

            if split_name[0] == "":
                split_name.remove(split_name[0])
            
            cls.team_church = split_name[0]
            cls.team_cap_last_name = split_name[2]

            try:
                school_name = cls.school_name_values[cls.team_church]
                cls.team_school_level = cls.school_level_values[split_name[1]]
                cap_name = cls.__calculate_captain_hash(name=cls.team_cap_last_name)

                return cls.team_school_level + school_name + cap_name
            
            except KeyError:
                logger.error(f'Key Error occurred while indexing with {cut_team_name_low}')
                return 0
        else:
            split_name = team_name_low.split(" ")

            cls.team_church = split_name[0]
            cls.team_cap_last_name = split_name[2]

            try:
                school_name = cls.school_name_values[cls.team_church]
                cls.team_school_level = cls.school_level_values[split_name[1]]
                cap_name = cls.__calculate_captain_hash(name=cls.team_cap_last_name)

                return cls.team_school_level + school_name + cap_name
            
            except KeyError:
                return 0


gen_response = GenerateTeamId().generate_team_spec_response("Ascension Jr Smith")
