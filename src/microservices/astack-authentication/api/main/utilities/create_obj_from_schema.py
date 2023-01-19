from main.schemas.schemas_admin import *
from main.schemas.schemas_response import Response, ServiceResponse

from loguru import logger
from typing import Dict

class ObjectBuilder:

    @staticmethod
    def convert_response_to_service_response (response: Response) -> ServiceResponse:

        try: 

            service_response = ServiceResponse(
                schema_version='1.0',
                http_code=response.http_code,
                error_code=response.error_code,
                msg=response.msg
            )

            return service_response
        
        except Exception as e:
            logger.error(f'{e}')

    @staticmethod
    def format_new_admin (admin: NewAdminDarkKnight) -> NewAdminDarkKnight:

        try:

            new_admin_fmt = NewAdminDarkKnight(
                login_id=admin.login_id,
                first_name=admin.first_name.strip().lower(),
                last_name=admin.last_name.strip().lower(),
                username=admin.username.strip(),
                email=admin.email.strip(),
                password=admin.password,
                confirm_password=admin.confirm_password,
                position=admin.position,
                astack_right_level=admin.astack_right_level
            )

            return new_admin_fmt
        
        except Exception as e:
            logger.error(f'{e}')
    
    @staticmethod
    def build_admin_base (data: Dict):

        try:

            admin = AdminDarkKnightBase(
                username=data['username'],
                astack_right_level=data['right_level']
            )

            return admin
        
        except Exception as e:
            logger.error(f'{e}')
    

