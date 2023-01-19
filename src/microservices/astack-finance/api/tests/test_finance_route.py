from fastapi.testclient import TestClient

from main.routes.security.token import TokenFactory as TF

from main.schemas.schemas_admin import AdminDarkKnightBase
from main.schemas.schemas_response import Response
from main.app import api

from mock import patch

client = TestClient(api)


test_admin = AdminDarkKnightBase(username="tester", position="developer", astack_right_level=1)
async def override_get_user_from_token ():
    return test_admin


# Mock get_user_from_token
api.dependency_overrides[TF.get_user_from_token] = override_get_user_from_token

'''
Tests that publish method is called
'''
@patch("main.config.event_publisher.EventPublisher.publish", autospec=True, return_value=Response(http_code=200, error_code=0, msg=''))
def test_finance_transaction_publisher (MockPublishMethod):

    # Insert `None` into route because api version comes from docker compose env variable
    response = client.post(
        "/admin-stack/None/finance-manager/add-transaction", json={
            "first_name":"gabriel",
            "last_name":"ruggie",
            "amount":20
        }
    )
    
    # Turn off dependency mock for final test
    api.dependency_overrides = {}

    assert response.json() == {'error_code': 0, 'http_code': 200, 'msg': '', 'schema_version': '1.0'}

'''
Verify that without overriding `get_user_from_token` that TF throws HTTP exception for finance route
Insert `None` into route because api version comes from docker compose env variable
'''
def test_finance_canvas_page_throws_httpexception ():
    response = client.get(
        "/admin-stack/None/finance-manager/canvas"
    )

    assert response.json() == {'detail': 'Not authenticated'}
