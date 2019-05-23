import json
import pprint
from instagram_private_api import Client, ClientCompatPatch
import sys

user_name = 'jxrnge'
password = sys.argv[1]



api = Client(user_name, password)
results = api.news()

media_id = sys.argv[2]
print("Searching for mediaid: " + str(media_id))
api = Client(user_name, password)
mediainfo = api.media_info(media_id)
 
print("Username is " + str(mediainfo))
