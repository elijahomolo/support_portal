import json
from pprint import pprint
import os

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("No secret key set for Flask application")
auth=('eomolo@anaconda.com', SECRET_KEY)

#data = '{"subject":"Test"}'
