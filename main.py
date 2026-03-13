from src.collect_data import get_followers , get_follower_count
from src.save_data import save_username_to_csv , save_count_to_csv
from config import TARGET_USERNAME

def start():
    username = TARGET_USERNAME
    """
    username = input("Enter the Instagram username: ")
    followers = get_followers(username)
    print(f"Total Followers  {len(username)}:")
    
    save_username_to_csv(followers, username)
    print("Data collection and saving completed.") 
    
    """
    count = get_follower_count(username)
    if count is not None:
        save_count_to_csv(count, username)
    else:
        print("Failed to retrieve follower count.")
    
if __name__ == "__main__":
    start()