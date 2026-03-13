import pandas as pd 
from datetime import datetime
import os 
from config import TARGET_USERNAME

def save_username_to_csv(username_list, target_account = TARGET_USERNAME):
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    data = {
        'date': [current_date] * len(username_list),
        'username': username_list
    }
    
    df = pd.DataFrame(data)
    filename = f"data/{target_account}_followers_{current_date}.csv"
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data saved to {filename}")
    
def save_count_to_csv(count, target_account = TARGET_USERNAME):
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    data = {
        'date': [current_date],
        'follower_count': [count]
    }
    
    df = pd.DataFrame(data)
    filename = f"data/{target_account}_follower_history.csv"
    
    if not os.path.exists('data'):
        os.makedirs('data')
        
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False, encoding='utf-8')
    else:
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8')    
    print(f"Follower count saved to {filename}")