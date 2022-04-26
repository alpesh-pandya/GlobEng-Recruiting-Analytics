import argparse
from data.load import historical_data,weekly_data
from data.transform import get_new_rows, get_updated_rows
from data.serve import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--historical', type=str, required=True)
    parser.add_argument('-w','--weekly', type=str, required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':  
    args = parse_args()
    # load
    historical_df=historical_data(args.historical)
    weekly_df=weekly_data(args.weekly)
    # prepare
    new_rows=get_new_rows(historical_df,weekly_df)
    updated_rows = get_updated_rows(historical_df, weekly_df)
    print(updated_rows)
    # calculate insights
    update_insights = get_update_insights(updated_rows)
    update_counts=get_counts(updated_rows,['Custom field (Epic Link)','Status','Labels'])
    print(new_rows.columns)
    new_counts=get_counts(new_rows,['Custom field (Epic Link)','Status','Labels'])
    merged_df=merge_dataframes(historical_df,new_rows,updated_rows)
    latest_snapshot=get_latest_snapshot(merged_df)
    total_counts=get_counts(latest_snapshot,['Custom field (Epic Link)','Status','Labels'])
    persist_insights(update_insights,new_counts,total_counts,merged_df)

    
