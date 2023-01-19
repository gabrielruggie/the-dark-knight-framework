from main.schemas.schemas_status import Status

from main.utilities.create_obj_from_schema import ObjectBuilder



def test_status_conversion ():

    status = Status(
        status_code=200, 
        message=''
    )

    error = ObjectBuilder().convert_status_to_error(status=status)

    assert error.json() == '{"schema_version": "1.0", "http_code": 200, "msg": "", "admin_id": null, "log_type": "error", "is_cached": 1, "service": null, "cache_key": null}'