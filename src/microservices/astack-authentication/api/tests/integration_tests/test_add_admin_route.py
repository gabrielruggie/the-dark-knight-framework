from fastapi.testclient import TestClient
from main.routes import *
from main.app import api

from mock import patch

client = TestClient(api)
'''
Valid validation key
{
    "login_id": 1234,
    "validation_key": "dk-validation-key",
    "admin_level": 1,
    "position":"developer"
}
'''
def test_send_valid_add_request():

    response = client.get(
        "/admin-stack/new-admin/add/?admin_request=ewoibG9naW5faWQiOiAxMjM0LAoidmFsaWRhdGlvbl9rZXkiOiAiZGstdmFsaWRhdGlvbi1rZXkiLAoiYWRtaW5fbGV2ZWwiOiAxLAoicG9zaXRpb24iOiJkZXZlbG9wZXIiCn0="
        )
    assert response.json() == {
        "login_id": 1234,
        "admin_level": 1,
        "position": "developer"
        }

'''
Invalid validation key
{
    "login_id": 1234,
    "validation_key": "hello_world",
    "admin_level": 1,
    "position":"developer"
}
'''
def test_send_invalid_add_request():
    response = client.get(
        "/admin-stack/new-admin/add/?admin_request=ewoibG9naW5faWQiOiAxMjM0LAoidmFsaWRhdGlvbl9rZXkiOiAiaGVsbG9fd29ybGQiLAoiYWRtaW5fbGV2ZWwiOiAxLAoicG9zaXRpb24iOiJkZXZlbG9wZXIiCn0="
    )
    assert response.json() == {
        "status": "failed",
        "message": "not a valid admin request"
    }

@patch('main.database.query_classes.admin_query.ConstructAdminQuery.add_dk_details', autospec=True)
@patch('main.database.query_classes.admin_query.ConstructAdminQuery.insert_to_admin_table', autospec=True)
def test_post_method(MockedAddDkDetails, MockedInsertion):

    response = client.post(
        "/admin-stack/new-admin/add/", json={
        'username':"testUser",
        'position':"developer",
        'login_id':1234,
        'first_name':"gabriel",
        'last_name':"ruggie",
        'email':"gruggie@gmail.com",
        'password':"hell0World",
        'confirm_password':"hell0World",
        'astack_right_level':1
    }
    )

    # Verify query constructor methods are being called
    assert MockedAddDkDetails.called == True
    assert MockedInsertion.called == True

    # expecting success message due to session error being surpressed when offline
    assert response.json() == {'status': 'success', 'message': ''}
