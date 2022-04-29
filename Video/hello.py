from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service


# Define the auth scopes to request.
scope = 'https://www.googleapis.com/auth/analytics.readonly'
key_file_location = 'C:/Users/slinfo/Documents/GitHub/3Team/Video/active-landing-339302-f8a2d8c6730f.json'

# Authenticate and construct service.
service = get_service(
    api_name='analytics',
    api_version='v3',
    scopes=[scope],
    key_file_location=key_file_location)

# Get a list of all Google Analytics accounts for this user
accounts = service.management().accounts().list().execute()

if accounts.get('items'):
    # Get the first Google Analytics account.
    account = accounts.get('items')[0].get('id')

    # Get a list of all the properties for the first account.
    properties = service.management().webproperties().list(accountId=account).execute()

# 일주일간 세션수와, 페이지뷰수 받아오기
result = service.data().ga().get(
    ids='ga:259130646',
    start_date='7daysAgo',
    end_date='today',
    metrics='ga:sessions,ga:pageviews').execute()