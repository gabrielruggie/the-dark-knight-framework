from fastapi import APIRouter, Depends, responses

from main.database.query_classes.player_query import ConstructPlayerQuery
from main.database.query_classes.team_query import ConstructTeamQuery
from main.database.generate_session import generate_session_instance

from sqlalchemy.orm import Session

from main.schemas.schemas_player import PlayerStats
from main.schemas.schemas_team import TeamStats, TeamDatabase
from main.schemas.schemas_response import Response

from main.utilities.generate_team_id import GenerateTeamId

from loguru import logger

router = APIRouter()

@router.get("/ymbl/stats")
async def retrieve_all_player_stats (session: Session = Depends(generate_session_instance)):

    '''
    queries player table and returns list of JSON player objects filtered down as PlayerStat objects
    '''
    logger.info(f'Connected to database with session instance: {session}')
    
    player_query_constructor = ConstructPlayerQuery(dk_session=session)
    data = player_query_constructor.retrieve_all_players()

    logger.info(f'Retrieved transactions: {data} from database')

    return responses.JSONResponse(content=data, status_code=200)

@router.post("/ymbl/sendstats")
async def update_player_stats (player: PlayerStats, session: Session = Depends(generate_session_instance)):
    
    logger.info(f'Connected to database with session instance: {session}')

    # Mark attributes that will be removed soon by "" or 0
    # Might be able to get rid of team attributes
    player_dict = {
        'first_name': player.first_name,
        'last_name': player.last_name,
        'id': player.id,
        'player_number': player.player_number,
        'team_church': player.team_church,
        'team_cap_name': player.team_cap_name,
        'team_level': player.team_level,
        'team_id': player.team_id,
        'tot_points': player.tot_points,
        'tot_assists': player.tot_assists,
        'tot_rebounds': player.tot_rebounds,
        'tot_steals': player.tot_steals,
        'tot_blocks': player.tot_blocks,
        'games_played': player.games_played
    }

    player_query_constructor = ConstructPlayerQuery(dk_session=session)
    response = player_query_constructor.update_player_by_id(player_dict=player_dict)

    # Set status_code to 500 so it triggers error on frontend
    return responses.JSONResponse(content=response.msg, status_code=response.http_code)

@router.post("/ymbl/sendstats-new-team")
async def create_new_team_and_players (team: TeamStats, session: Session = Depends(generate_session_instance)):
    
    logger.info(f'Connected to database with session instance: {session}')

    # Schema Type is Current TeamDatabase schema. Change to new one before going to production
    # We will be removing wins, losses, total points and pts allowed
    gen_response = GenerateTeamId().generate_team_spec_response(team_name=team.team_name)
    
    if gen_response['team_id'] != 0:
        logger.info(f'Team id successfully created. General Response: {gen_response}')
        team_dict = TeamDatabase(
            church=gen_response['church'],
            school_level=gen_response['team_school_level'],
            cap_last_name=gen_response['cap_last_name'],
            team_name=gen_response['team_name'],
            id=gen_response['team_id'],
        )

        team_query_constructor = ConstructTeamQuery(dk_session=session)
        team_creation_response = team_query_constructor.create_new_team(team_data=team_dict)

        if team_creation_response.http_code != 200:
            return responses.JSONResponse(content=team_creation_response.msg, status_code=team_creation_response.http_code)

        logger.info("Moving unto player queries...")
        
        player_query_constructor = ConstructPlayerQuery(dk_session=session)
        player_creation_response = player_query_constructor.create_players(player_name_list=team.roster, team_data=team_dict)
        
        return responses.JSONResponse(content=player_creation_response.msg, status_code=player_creation_response.http_code)

    else:
        logger.error(f'Team id invalid: General Response: {gen_response}')
        response = Response(http_code=500, error_code=660, msg="Team Name is invalid, please review team input instructions")
        return responses.JSONResponse(content=response.msg, status_code=response.http_code)


