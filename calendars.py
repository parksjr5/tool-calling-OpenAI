import creds
import json
import requests
import pycronofy
import datetime
import uuid

### Authorization ###
token = creds.credentials['cronofy_access_token']
cronofy = pycronofy.Client(access_token=token)

### Get Dates ###

def get_upcoming_events(cal_id=creds.credentials['apple_cal_id_home'], in_future=5):
    """Collects days and times of when busy and returns them in a list of JSONs

    :param cal_id: id of calendar from cronofy
    :type cal_id: string
    :param in_future: days in future, max of 5 due to weather forecast
    :type in_future: int

    :return events: list containing a JSON of event start, end, and busy
    :rtype: list of JSONs
    """
    # timezone id
    tzid = 'US/Eastern'
    # set local time
    # example_datetime_string = '2016-01-06T16:49:37Z' #ISO 8601.
    to_date = (datetime.datetime.now() + datetime.timedelta(days=in_future))
    from_date = datetime.datetime.now()
    free_busy_blocks = cronofy.read_free_busy(calendar_ids=cal_id,from_date=from_date,to_date=to_date)

    events = []
    for block in free_busy_blocks:
        block.pop('calendar_id', None)
        events.append(block)

    return events

def write_event(start_time, length_of_meeting):
    # Example timezone id
    timezone_id = 'US/Eastern'
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
    event_id = 'example-%s' % uuid.uuid4()

    event = {
        'event_id': event_id,
        'summary': 'Test Event', # The event title
        'description': 'Discuss proactive strategies for a reactive world.',
        'start': start_time,
        'end': (start_time + datetime.timedelta(hours=length_of_meeting)),
        'location': {
            'description': 'My Desk!',
        },
    }

    cronofy.upsert_event(calendar_id=creds.credentials['apple_cal_id_home'], event=event)