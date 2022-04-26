import os
from pathlib import Path
from datetime import datetime
from config import OUTPUT_PATH

def get_counts(dataframe, groupby_columns):
    group_df = dataframe.groupby(groupby_columns).size().reset_index(name='counts')
    return group_df

def merge_dataframes(historical_df,new_df,updated_df):
    merged_df=historical_df.copy(deep=True)
    return merged_df.append(new_df).append(updated_df)

def get_update_insights(updated_df):
    return updated_df.groupby(['Custom field (Epic Link)','Version Reason']).size().reset_index(name='counts')

def get_latest_snapshot(merged_df):
    latest_idx=merged_df.groupby(['Issue key'])['Version'].transform(max) == merged_df['Version']
    latest_merged_data=merged_df[latest_idx]
    return latest_merged_data

def persist_insights(update_insights,new_counts,total_counts,merged_df):
    date_folder_name=datetime.today().strftime('%Y%m%d')
    Path(os.path.join(OUTPUT_PATH,date_folder_name)).mkdir(parents=True, exist_ok=True)
    
    update_insights.to_csv(os.path.join(OUTPUT_PATH,date_folder_name, 'what_changed.csv'))
    new_counts.to_csv(os.path.join(OUTPUT_PATH,date_folder_name, 'new_candidates.csv'))
    total_counts.to_csv(os.path.join(OUTPUT_PATH,date_folder_name, 'latest_snapshot.csv'))
    merged_df.to_csv(os.path.join(OUTPUT_PATH,date_folder_name, 'latet_historical_data.csv'))
