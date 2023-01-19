from typing import Optional, Dict
import json
from loguru import logger

'''
Generates an 4 digiti id for a new team based on sponsoring church, grade and hashed last name value
'''
class TeamIdGenerator:

    def __init__ (self, church: str, school_level: int, name: str):
        self.church = str(church).lower()
        self.school_level = school_level
        self.name = str(name).lower()

        with open('./resources/churches.json', 'r') as file:
            self.church_map: Optional[Dict] = json.load(file)

    def __get_church_name (self) -> str:
        name = self.church.replace('st.', '')
        return name.strip()

    # Avoid duplicate teams through hashing last name
    def __hash_last_name (self) -> int:
        hashed_name = abs(int(hash(self.name)))
        last_two_digits = hashed_name % 100

        return last_two_digits

    def __convert_school_level (self) -> int:
        # 1=Freshman, 2=Sophomore, 3=Junior, 4=Senior
        # Anything else should be marked as invalid
        if self.school_level < 1 or self.school_level > 4:
            return None

        return self.school_level * 100

    def generate (self) -> int:

        church_name = self.__get_church_name()
        found_church_id = int(self.church_map[church_name])
        team_level = self.__convert_school_level()

        if found_church_id == None or team_level == None:
            logger.warning(f'There was an error while creating an id for church: {self.church}.\
                            This church may not be registered with the software.'
                            )
            raise Exception

        name_id = self.__hash_last_name()

        return found_church_id + team_level + name_id