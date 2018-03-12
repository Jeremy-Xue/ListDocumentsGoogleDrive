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

# Python wrapper for drive API
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Get authentication
gauth = GoogleAuth()
# Create a local webserver and auto handles authentication.
gauth.LocalWebserverAuth()
# Get drive from authentication
drive = GoogleDrive(gauth)
# Iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
count = 1
for file1 in file_list:
  print('%s: Document Title: %s' % (str(count), file1['title']))
  count += 1
