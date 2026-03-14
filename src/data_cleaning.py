#if we run code multiple time in a day we want to eliminate the duplicates
import pandas as pd

def remove_duplicates(file_path):
    #Read the CSV filie into DataFrame
    df = pd.read_csv(file_path)
    #Remove duplicates based on all columns 
    df_cleaned = df.drop_duplicates(subset=['date'] , keep='first')
    #Save the cleaned DataFrame back to CSV
    df_cleaned.to_csv(file_path, index=False)
    
     
