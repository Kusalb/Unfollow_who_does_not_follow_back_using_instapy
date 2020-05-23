#Program 1: Logs in and gets the follower and following list.
from instapy import InstaPy
#Logs in into your instagram
session = InstaPy(username="Your insta account name", password="Your insta account password")
#Logs in.
session.login()
#Gets the follower list and store in the instapy folder
follower_list = session.grab_followers(username='nepvent',live_match=False, store_locally=True ,amount='full')
#Gets the following list and store in the instapy folder
following_list = session.grab_following(username='nepvent', live_match=False, store_locally=True, amount='full')


