import json
import pprint
from instagram_private_api import Client, ClientCompatPatch
import sys

user_name = 'jxrnge'
password = sys.argv[1]



api = Client(user_name, password)
results = api.news()

id = sys.argv[2]
print("Searching for id: " + str(id))
api = Client(user_name, password)
username = api.user_info(id)['user']['username']
print("Username is " + str(username))
