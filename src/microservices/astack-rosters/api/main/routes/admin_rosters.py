from fastapi import APIRouter, Depends, responses

from main.routes.security.token import TokenFactory

from main.config.event_builder import EventBuilder
from main.config.event_publisher import EventPublisher

from main.utilities.load_env_file import Environment
from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_admin import AdminDarkKnightBase
from main.schemas.schemas_player import PlayerSheets
from main.schemas.schemas_team import TeamBase

from main.database.generate_session import generate_session_instance
from main.database.query_classes.player_query import ConstructPlayerQuery

from sqlalchemy.orm import Session

from loguru import logger

rosters = APIRouter()

'''
Canvas page that loads players and their teams
'''
@rosters.get("/canvas")
async def canvas_page (
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token),
    session: Session = Depends(generate_session_instance)
    ):
    '''
    Will load players sorted by teams and display them on this page
    '''
    logger.info(f'Connected to database with session instance: {session}')
    
    player_query_constructor = ConstructPlayerQuery(dk_session=session)
    data = player_query_constructor.retrieve_all_players()

    logger.info(f'Retrieved transactions: {data} from database')

    return responses.JSONResponse(content=data, status_code=200)

'''
Allows admin to create a new team and fire event to postgres event handler
'''
@rosters.post("/create-new-team")
async def create_new_team (
    team: TeamBase,
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)
    ):

    logger.info("Received new request to create a new team")

    event_builder = EventBuilder(
        data=dict(team),
        data_type='team.add',
        topic_published_to=Environment.POSTGRES_EVENTS_TOPIC,
        data_source='astackrosters',
        publisher_name=admin.username,
        )

    new_team_event = event_builder.create()

    publisher = EventPublisher(Environment.POSTGRES_EVENTS_TOPIC, dict(new_team_event))
    resulting_payload = publisher.publish()

    return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=resulting_payload)))

'''
Allows admin to create delete an exisiting team based on the id
To get id of team, will need to view it on the canvas page
'''
@rosters.delete("/delete-team/{id}")
async def remove_team_by_id (
    team_id: int,
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)
    ):

    logger.info("Received new request to delete team from database")

    delete_team = {'team_id': team_id}

    event_builder = EventBuilder(
        data=delete_team,
        data_type='team.delete',
        topic_published_to=Environment.POSTGRES_EVENTS_TOPIC,
        data_source='astackrosters',
        publisher_name=admin.username
    )

    delete_team_event = event_builder.create()
    publisher = EventPublisher(topic_name=Environment.POSTGRES_EVENTS_TOPIC, event=dict(delete_team_event))
    payload = publisher.publish()

    return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=payload)))
    
@rosters.post("/add-new-player")
async def add_new_player (
    player: PlayerSheets,
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)
    ):

    logger.info('Received request to add player to database')

    # Always format user input before publishing it to topic
    event_builder = EventBuilder(
        data= dict(ObjectBuilder().format_new_player_input(player=player)),
        data_type='player.add',
        topic_published_to=Environment.POSTGRES_EVENTS_TOPIC,
        data_source='astackrosters',
        publisher_name=admin.username
    )

    new_player_event = event_builder.create()
    # THis shouldn't return anything anymore
    publisher = EventPublisher(topic_name=Environment.POSTGRES_EVENTS_TOPIC, event=dict(new_player_event))
    payload = publisher.publish()

    return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=payload)))

@rosters.delete("/delete-player/{id}")
async def delete_existing_player (
    player_id: str,
    admin: AdminDarkKnightBase = Depends(TokenFactory.get_user_from_token)
    ):

    logger.info("Received new request to delete team from database")

    delete_player = {'player_id': player_id}

    event_builder = EventBuilder(
        data=delete_player,
        data_type='player.delete',
        topic_published_to=Environment.POSTGRES_EVENTS_TOPIC,
        data_source='astackrosters',
        publisher_name=admin.username
    )

    delete_team_event = event_builder.create()
    publisher = EventPublisher(topic_name=Environment.POSTGRES_EVENTS_TOPIC, event=dict(delete_team_event))
    payload = publisher.publish()

    return responses.JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=payload)))