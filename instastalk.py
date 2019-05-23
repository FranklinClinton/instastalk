import json
import pprint
from instagram_private_api import Client, ClientCompatPatch
import dbconnect


user_name = 'jxrnge'
password = sys.argv[1]

api = Client(user_name, password)
results = api.news()

api = Client(user_name, password)
items = results.get('stories',[])
for item in items:
        handled = False
        if item['story_type'] == 60 and True == True:                                                            #60 is like
                #print(item['pk']) #Unique ID I think
                print(item['args']['text'])
                lenght = len(item['args']['links'])
                if lenght > 1:                                                                  #XXXX and XXXX liked XXXX post
                    recipient_id = item['args']['links'][lenght - 1]['id']                      #The last value in the arry is the recipient
                    #print("Recipient: " + api.user_info(recipient_id)['user']['username'])
                    likers = []
                    for x in range(lenght - 1):                                                 #All other items are initators
                            profile_id = item['args']['links'][x]['id']
                            likers.append(profile_id)
                            #profile_info = api.user_info(profile_id)
                            #print("Liker: " + profile_info['user']['username'])
                    media_id = item['args']['media'][0]['id']
                    media_pk = api.media_info(media_id)['items'][0]['pk']
                    media_url = item['args']['media'][0]['image']
                    #media_url = "SKIPPED, DEBUG"
                    #print("Media URL: " + media_url)
                    for liker in likers:
                            dbconnect.medialike(liker, recipient_id, media_pk, str(media_url))

                else:                                                                           #XXXX liked XXXX post
                    liker_id = item['args']['links'][lenght - 1]['id']                          #The only value here is the liker
                    print("Liker: " + api.user_info(liker_id)['user']['username'])
                    medialenght = len(item['args']['media'])
                    for x in range(medialenght):                                                     #Fetch all medias
                        media_id = item['args']['media'][x]['id']
                        media_uploader_id = str(media_id).split("_")[1]
                        media_url = item['args']['media'][x]['image']
                        media_url = "SKIPPED, DEBUG"
                        print("Uploader ID: " + media_uploader_id)
                        print("Media URL: " + media_url)
                handled = True
        if item['story_type'] == 101 and True == True:                                                            #101 is follow
                #print(item['pk']) #Unique ID I think
                print(item['args']['text'])
                lenght = len(item['args']['links'])
                if lenght > 1:                                                                  #XXXX and XXXX liked XXXX post
                    initiator_id = item['args']['links'][0]['id']                                    #The last value in the arry is the recipient
                    print("Initiator: " + api.user_info(initiator_id)['user']['username'])
                    for x in range(lenght - 1):                                                 #All other items are initators
                            profile_id = item['args']['links'][x+1]['id']
                            profile_info = api.user_info(profile_id)
                            print("Recepient: " + profile_info['user']['username'])

                else:                                                                           #XXXX liked XXXX post
                    liker_id = item['args']['links'][lenght - 1]['id']                          #The only value here is the liker
                    print("Initator (else): " + api.user_info(liker_id)['user']['username'])
                    print(item)
                handled = True
        if item['story_type'] == 13 and True == True:                                                            #13 is liked comment
                #print(item['pk']) #Unique ID I think
                print(item['args']['text'])
                lenght = len(item['args']['links'])
                if lenght > 1:                                                                  #XXXX and XXXX liked XXXX post
                    recipient_id = item['args']['links'][lenght - 1]['id']                      #The last value in the arry is the recipient
                    print("Recipient: " + api.user_info(recipient_id)['user']['username'])
                    for x in range(lenght - 1):                                                 #All other items are initators
                            profile_id = item['args']['links'][x]['id']
                            profile_info = api.user_info(profile_id)
                            print("Liker: " + profile_info['user']['username'])
                    media_id = item['args']['media'][0]['id']
                    media_url = item['args']['media'][0]['image']
                    media_url = "SKIPPED, DEBUG"
                    print("Media URL: " + media_url)

                else:                                                                           #XXXX liked XXXX post
                    liker_id = item['args']['links'][lenght - 1]['id']                          #The only value here is the liker
                    print("Liker: " + api.user_info(liker_id)['user']['username'])
                    medialenght = len(item['args']['media'])
                    for x in range(medialenght):                                                     #Fetch all medias
                        media_id = item['args']['media'][x]['id']
                        media_uploader_id = str(media_id).split("_")[1]
                        media_url = item['args']['media'][x]['image']
                        media_url = "SKIPPED, DEBUG"
                        print("Uploader ID: " + media_uploader_id)
                        print("Media URL: " + media_url)
                handled = True
        if handled == False and True == True:                                                            #unknown
                print("unkown story")
                print(" ")
                print(item)
                print(item['args']['text'])
