# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#from __future__ import print_function

import webapp2
import httplib2
import os

# Python wrapper for drive API
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


#from googleapiclient import discovery
#from oauth2client import client
#from oauth2client import tools
#from oauth2client.file import Storage
#from apiclient import errors

#try:
#    import argparse
#    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
#except ImportError:
#    flags = None
# ...

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)
#Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))

SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secrets.json'
APPLICATION_NAME = 'Drive API Python Quickstart'

#def get_credentials():
"""Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    #home_dir = os.path.expanduser('~')
    #credential_dir = os.path.join(home_dir, '.credentials')
    #if not os.path.exists(credential_dir):
    #    os.makedirs(credential_dir)
    #credential_path = os.path.join(credential_dir,
    #                               'drive-python-quickstart.json')

    #store = Storage('storage.json')
    #credentials = store.get()
    #if not credentials or credentials.invalid:
    #    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    #    #flags = tools.argparser.parse_args(args=[])
    #    credentials = tools.run_flow(flow, store, flags)
    # Redirect the user to auth_uri on your platform.
        #if flags:
        #    credentials = tools.run_flow(flow, store, flags)
        #else: # Needed only for compatibility with Python 2.6
    #credentials = tools.run(flow, store)
    #print('Storing credentials to ' + credential_path)
    #service = discovery.build('drive', 'v3')
    #return credentials

'''
def retrieve_all_files(service):
  """Retrieve a list of File resources.

  Args:
    service: Drive API service instance.
  Returns:
    List of File resources.
  """
  result = []
  page_token = None
  while True:
    #try:
    param = {}
    if page_token:
        param['pageToken'] = page_token
        files = service.files().list(**param).execute()

        result.extend(files['items'])
        page_token = files.get('nextPageToken')
    if not page_token:
        break
    #except errors.HttpError, error:
     # print('An error occurred: %s') % error
     # break
  return result
'''

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json


class MainPage(webapp2.RequestHandler):
    def get(self):
        #credentials = get_credentials()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        '''result = retrieve_all_files(service)
        for file in result:
            self.response.write('test')
        '''

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
