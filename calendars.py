import creds
import json
import requests
import pycronofy
import datetime

### Authorization ###
token = creds.credentials['cronofy_access_token']
cronofy = pycronofy.Client(access_token=token)

### Get Dates ###

def get_upcoming_events(cal_id=creds.credentials['apple_cal_id_home'], in_future=5):
    # timezone id
    tzid = 'US/Eastern'
    # set local time
    # example_datetime_string = '2016-01-06T16:49:37Z' #ISO 8601.
    to_date = (datetime.datetime.now() + datetime.timedelta(days=in_future))
    from_date = datetime.datetime.now()
    free_busy_blocks = cronofy.read_free_busy(calendar_ids=cal_id,from_date=from_date,to_date=to_date)

    for block in free_busy_blocks:
        print(block)