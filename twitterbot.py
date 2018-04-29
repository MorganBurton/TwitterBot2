from time import sleep
import tweepy, json, time, os
#user info stored, following, followers, whitelisted
with open ('keys.json', 'r') as keys_file:
	keys_data = json.load(keys_file)

user_name = keys_data['authentication']['user_name']
authentication = tweepy.OAuthHandler(keys_data["authentication"]["CONSUMER_KEY"], keys_data["authentication"]["CONSUMER_SECRET"])
authentication.set_access_token(keys_data["authentication"]["ACCESS_TOKEN"], keys_data["authentication"]["ACCESS_SECRET"])
api = tweepy.API(authentication)

following = api.friends_ids(user_name)
followers = api.followers_ids(user_name)

#Choose what bot does
def options():

	print ('Type 1 to start, press any other key to unfollow not followed back:  ')
	choice = input('choose option: ')
	if choice == '1':
		follow()
	else:
		unfollow()
#michaels a cunt

#to follow someone else's followers
def follow():
	copy_name = input("type follower name to copy: ")
	copy_followers = api.followers_ids(copy_name)

	

	
	blacklist = []
	if os.stat('info.json').st_size != 0:
		with open('info.json', 'r') as outfile:
			blacklist = json.load(outfile)
	followed_list = [blacklist]

	#remove ppl already following n not to follow again
	copy_followers_adjusted = set(copy_followers) - set(following)

	print (len(copy_followers_adjusted))

	for x in copy_followers_adjusted:
		api.create_friendship(x)
		followed_time = int(time.time())
		followed_list.append(x)
		sleep(2)
		print (followed_list)


	with open('info.json', 'w') as outfile:
		json.dump(followed_list, outfile)
	print (len(followed_list))
def unfollow():
	not_followed_back = set(following) - set(followers)

	for x in not_followed_back:
		api.destroy_friendship(x)
		sleep(1)
options()

