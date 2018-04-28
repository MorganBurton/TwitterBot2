from time import sleep
import tweepy, json
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
#to follow someone else's followers
def follow():
	copy_name = input("type follower name to copy: ")
	copy_followers = api.followers_ids(copy_name)
	print (user_name)
	#remove ppl already following, need to - whitelisted aswell
	copy_followers_adjusted = set(copy_followers) - set(following)
	with open('info.json', 'wb') as info_file:
		write(copy_followers_adjusted)
		data = json.load(info_file)
		




	




	'''for x in copy_followers_adjusted:
		api.create_friendship(x)
		sleep()

def unfollow():
	not_followed_back = set(following) - set(followers)

	for x in not_followed_back:
		api.destroy_friendship(x)
		sleep(5)'''
options()

