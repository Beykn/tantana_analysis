import instaloader
bot = instaloader.Instaloader()
from config import TARGET_USERNAME

def get_followers(username = TARGET_USERNAME):
    follower_list = []
    profile = instaloader.Profile.from_username(bot.context, username)
    for f in profile.get_followers():
        follower_list.append(f.username)
        return follower_list
        
def get_follower_count(username = TARGET_USERNAME):
    
    try:
        profile = instaloader.Profile.from_username(bot.context,username)
        return profile.followers
    except Exception as e:
        print(f"Error fetching follower count for {username}: {e}")
        return None