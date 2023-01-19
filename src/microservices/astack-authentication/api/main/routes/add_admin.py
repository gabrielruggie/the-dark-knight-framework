from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from loguru import logger 

from main.schemas.schemas_admin import NewAdminDarkKnight
from main.schemas.schemas_response import Response

from main.utilities.verify_user_credentials import VerifyUserFactory as factory
from main.utilities.load_env_file import Environment
from main.utilities.create_obj_from_schema import ObjectBuilder

# Session dependencies
from main.database.generate_session import generate_session_instance
from main.database.query_classes.admin_query import ConstructAdminQuery
from sqlalchemy.orm import Session

# Miscellaneous
import base64
import uuid

admin = APIRouter()

'''
Fetches validation key from .env file and returns it
'''

DK_VALIDATION_KEY = Environment.DK_VALIDATION_KEY

'''
Receives a request from browser to load admin registration page. 
Only requests with a valid base64 JSON object are accepted.

Valid validation key
{
    "login_id": 1234,
    "validation_key": "dk-validation-key",
    "admin_level": 1,
    "position":"developer"
}
'''
@admin.get("/")
async def load_admin_add_page (admin_request: str) -> JSONResponse:
    try:

        # Converting from base64 -> bytes -> str -> dict
        request_bytes = base64.b64decode(admin_request)
        request_str = request_bytes.decode("utf-8")
        request_obj = eval(request_str)

    except UnicodeDecodeError as u:
        logger.error(f'Received error when trying to decode admin request: {u}')
        response = Response(http_code=500, error_code=300, msg='There as an error while loading the page. Please report this error or try a different url')
        return JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=response)))

    if not request_obj["validation_key"] == DK_VALIDATION_KEY:
        logger.error("the admin request had an invalid request key. failing...")
        response = Response(http_code=500, error_code=301, msg='There was an error while loading the page. Pleas report this error or try a different url')
        return JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=response)))
    
    logger.info(
        f'Admin is verified with attributes: login_id: {request_obj["login_id"]} admin_level: {request_obj["admin_level"]}, position: {request_obj["position"]}'
        )
    del request_obj["validation_key"]

    response = Response(http_code=200, error_code=0, msg='')
    return JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=response)))

'''
Adds a new admin to our postgres database. 
Postgres configuration variables can be found in the .env file
'''
@admin.post("/")
async def add_admin_to_dk (new_admin: NewAdminDarkKnight, session: Session = Depends(generate_session_instance)) -> JSONResponse:

    try:

        logger.debug("Verifing user fields now...")
        logger.debug(f'{session}')

        new_admin_fmt = ObjectBuilder().format_new_admin(admin=new_admin)

        validation_response= verify_admin_registration_fields(admin=new_admin_fmt, session=session)

        if validation_response.http_code != 200:
            logger.error(f'{validation_response.msg}')
            return JSONResponse(dict(validation_response))

        admin_id = str(uuid.uuid4())
        admin_query_constructor = ConstructAdminQuery(dk_session=session)
        new_dk_admin = admin_query_constructor.add_dk_details(new_admin=new_admin_fmt, unique_id=admin_id, password=new_admin.password)
        admin_query_constructor.insert_to_admin_table(admin=new_dk_admin)

        # Redirect the user in message if need be
        logger.info("Admin successfully added to database")
        response = Response(http_code=200, error_code=0, msg='Successfully registered new admin to ASTACK')
        return JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=response)))
    
    except Exception as e:
        logger.error(f'An unexpected error occurred while trying to register admin.: {e}')
        response = Response(http_code=500, error_code=310, msg='An unexpected error occurred while processing your request. Please inform your supervisor of this error!')
        return JSONResponse(dict(ObjectBuilder().convert_response_to_service_response(response=response)))

'''
Verfies an Admin's input fields
Returns a status payload depending on the success of the verification
'''
def verify_admin_registration_fields (admin: NewAdminDarkKnight, session: Session) -> Response:
    confirmed_password = admin.password if admin.password == admin.confirm_password else None
    
    if confirmed_password == None:
        return Response(http_code=400, error_code=320, msg='Passwords do not match!')
    
    if not factory.verify_correct_password(confirmed_password):
        return Response(http_code=400, error_code=321, msg='Password must contain a number and uppercase letter!')

    if not factory.verify_email(admin.email):
        return Response(http_code=400, error_code=322, msg='Email is not valid!')
    
    if not factory.verify_admin_does_not_exist(admin.login_id, session=session):
        return Response(http_code=400, error_code=323, msg="Admin already exists")
    
    return Response(http_code=200, error_code=0, msg='Admin successfully registered to ASTACK!')
