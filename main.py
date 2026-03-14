from src.collect_data import get_followers , get_follower_count
from src.save_data import save_username_to_csv , save_count_to_csv
from config import TARGET_USERNAME
from src.report_generator import generate_weekly_report
from src.data_cleaning import remove_duplicates

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
        remove_duplicates("data/tantanacilar.jazz_follower_history.csv")
        
    else:
        print("Failed to retrieve follower count.")
        
def report():    
    report = generate_weekly_report()
    if report:
        
        
        print(report)
    else:
        print("Failed to generate the weekly report.")
    
if __name__ == "__main__":
    start()
    report()