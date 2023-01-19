from main.config.event_builder import EventBuilder
import json

'''
Tests ability to create a version 1.0 event and extract its contents
'''
def test_event_builder ():

    test_event = {
        "name": "gabriel",
        "date": "8/17/2022",
        "message": "hello world"
    }

    event_builder = EventBuilder(
        data=test_event,
        data_type="testevent",
        data_source="test",
        topic_published_to="None",
        publisher_name="test_event_builder"
    )

    result = event_builder.create()

    result_data = json.loads(result.data)

    # Verify that we are only generating 6 digit numbers
    assert len(str(result.id)) == 6

    # Check event contents
    assert result.version == '1.0'
    assert result_data['name'] == 'gabriel'
    assert result_data['date'] == '8/17/2022'
    assert result_data['message'] == 'hello world'
