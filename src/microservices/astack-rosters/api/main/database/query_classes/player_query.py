from typing import List
from main.database.tables.table import Table
from main.database.query_classes.base_query import BaseQuery

from main.schemas.schemas_player import PlayerDatabase

from loguru import logger
from sqlalchemy.orm import Session

class PlayerQuery(BaseQuery[Table.Player, PlayerDatabase, PlayerDatabase]):
    ...

class ConstructPlayerQuery:

    def __init__(self, dk_session: Session):
        self.session = dk_session
        self.player_query = PlayerQuery(Table.Player, tablename='player')
    
    def retrieve_all_players (self) -> List:

        try:

            return self.player_query.get_all_resources(dk_session=self.session)
        
        except Exception as e:
            logger.error(f'{e}')

