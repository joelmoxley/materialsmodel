#!/usr/bin/python2.4
#
# Copyright 2008 Google Inc.
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


help = """get a remote shell w/ access to the datastore.
"""

import code
import getpass
import sys

# from django.conf import settings


sys.path.append("/usr/local/google_appengine")
# sys.path.append("/usr/local/google_appengine/lib")

import glob
dirs = glob.glob("/usr/local/google_appengine/lib/*")
for d in dirs:
    sys.path.append(d)
sys.path.append("/usr/local/google_appengine/lib/yaml/lib")

from google.appengine.dist import use_library
use_library('django', '1.1')
from django.core.management.base import BaseCommand

from google.appengine.ext.remote_api import remote_api_stub


def auth_func():
    return raw_input('Username:'), getpass.getpass('Password:')

class Command(BaseCommand):
    """ Start up an interactive console backed by your app using remote_api """

    help = 'Start up an interactive console backed by your app using remote_api.'

    app_id = 'materialsmodel'
    host = '%s.appspot.com' % app_id

    remote_api_stub.ConfigureRemoteDatastore(app_id, 
                                             '/remote_api',
                                             auth_func,
                                             host)

    doc = 'App Engine interactive console for %s' % (app_id,)
    try:
        import IPython
        IPython.Shell.IPShell(user_ns=locals()).mainloop(sys_exit=1, banner=doc)
    except:
        code.interact(doc, None, locals())

