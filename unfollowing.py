#Program 2: To find the ig account which we follow but does not follow us back.

import json
from instapy import InstaPy
#Program 1 creates a JSON file consisting the list of all the followers of the given ig account. Reading the follower data into a variable.
with open('Path of the Json file where followers list is stored') as json_file:
    follower_data = json.load(json_file)

#Program 1 also creates a JSON file consisting the list of all the followering list of the given ig account. Reading the following data into a variable.
with open('Path of the Json file where following list is stored') as json_file:
    following_data = json.load(json_file)

#Finds the ig account which we follow but does not follow us back.
unfollowers_list = list(set(following_data).difference(follower_data))


#Logs in into your instagram
session = InstaPy(username="Your insta account name", password="Your insta account password")
#Logs in.
session.login()
#Unfollowes the user. Delay is provided.
session.unfollow_users(amount=84, custom_list_enabled=True, custom_list=unfollowers_list, custom_list_param="all", style="RANDOM", unfollow_after=55*60*60*2, sleep_delay=600)

