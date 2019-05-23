from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError

# Some endpoints, e.g. user_following are available only after authentication
api = Client(
    auto_patch=True, authenticate=True,
    username='jxrnge', password='xxx')


result = api.user_info2('northeast_clo')
user_id = result['id']

followers = []
results = api.user_followers(user_id)
print results
for user in results:
    followers.extend(user['username'])

next_max_id = results.get('next_max_id')
while next_max_id:
    results = api.user_followers(user_id, max_id=next_max_id)
    for user in results:
        followers.extend(user['username'])

    if len(followers) >= 600:       # get only first 600 or so
        break
    next_max_id = results.get('next_max_id')
followers.sort(key=lambda x: x['pk'])


for follower in followers:
	print follower
