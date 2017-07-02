import base64
import httplib2
import os

from apiclient import discovery

import oauth2client


DEFAULT_SCOPES = 'https://www.googleapis.com/auth/gmail.modify'


def get_credentials(appname, secret_file, scopes=DEFAULT_SCOPES):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'gmail.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = oauth2client.client.flow_from_clientsecrets(secret_file, scopes)
        flow.user_agent = appname
        oauth2args = '--auth_host_name localhost --logging_level INFO'.split()
        flags = oauth2client.tools.argparser.parse_args(oauth2args)
        credentials = oauth2client.tools.run_flow(flow, store, flags)

    return credentials


def b64_url_decode(data):
    """ deals with appending the right number of =s """
    data += '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data)


def get_gmail_service(appname, client_secret_file):
    """ get an authenticated gmail service instance """
    credentials = get_credentials(appname, client_secret_file)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    return service
