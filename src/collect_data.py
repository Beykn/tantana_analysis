import instaloader
bot = instaloader.Instaloader()

def get_followers(username):
    follower_list = []
    profile = instaloader.Profile.from_username(bot.context, username)
    for f in profile.get_followers():
        follower_list.append(f.username)
        return follower_list
        
def get_follower_count(username):
    
    try:
        profile = instaloader.Profile.from_username(bot.context,username)
        return profile.followers
    except Exception as e:
        print(f"Error fetching follower count for {username}: {e}")
        return None