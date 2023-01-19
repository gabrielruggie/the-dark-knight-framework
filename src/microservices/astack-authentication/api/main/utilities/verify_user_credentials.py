from passlib.hash import sha256_crypt
import re

from main.database.query_classes.admin_query import ConstructAdminQuery
from main.schemas.schemas_response import Response

from loguru import logger
from sqlalchemy.orm import Session
'''
User verification class used to verify user input fields to registration forms
'''
class VerifyUserFactory:

    email_pattern = re.compile("\w+@[a-zA-Z]{0,6}\.[a-zA-Z]{0,4}")
    pw_contains_uppercase_let = re.compile(".*[A-Z]+.*")
    pw_contains_number = re.compile(".*[0-9]+.*")

    @classmethod
    def verify_admin_and_return (cls, login_id: int, password: str, username: str, session: Session ) -> Response:
        admin_query_factory = ConstructAdminQuery(dk_session=session)
        
        result = admin_query_factory.get_admin_from_login_id(login_id=login_id)

        if result == None:
            return Response(http_code=400, error_code=50, msg="Could not find user in database") 
        
        logger.info("Verifying metadata...")

        if not cls.verify_passwords(password, result["hashed_password"]):
            return Response(http_code=400, error_code=51, msg="Passwords don't match!")
        logger.debug("Password verified")
        
        if not username == result["username"]:
            return Response(http_code=400, error_code=52, msg="Usernames don't match!")
        logger.debug("Username verified")
        
        if not login_id == int(result["login_id"]):
            return Response(http_code=400, error_code=53, msg="Login Ids don't match!")        
        logger.debug("Login Id verified")

        return Response(http_code=200, error_code=0, msg=f'{result["login_id"]}, {result["username"]}, {result["astack_right_level"]}')

    @classmethod
    def verify_admin_does_not_exist (cls, login_id: int, session: Session):
        admin_query_factory = ConstructAdminQuery(dk_session=session)
        result = admin_query_factory.get_admin_from_login_id(login_id=login_id)
        
        if result != None:
            return False
        
        return True

    @classmethod
    def verify_correct_password (cls, user_password):
        '''
        Passwords must be at least 8 characters long and have an uppercase letter and at least 1 number
        '''
        if len(user_password) >= 8 and cls.pw_contains_uppercase_let.fullmatch(user_password) and cls.pw_contains_number.fullmatch(user_password):
            return True
        return False

    @classmethod
    def verify_passwords (cls, user_password, hashed_password):
        return sha256_crypt.verify(user_password, hashed_password)

    @classmethod
    def verify_email (cls, user_email):
        if cls.email_pattern.fullmatch(user_email):
            return True
        return False