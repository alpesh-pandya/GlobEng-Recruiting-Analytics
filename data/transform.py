import copy
import pandas as pd
from config import COLUMNS_TO_COMPARE

def get_new_rows(historical_df,weekly_df):
    merged_df = weekly_df.merge(historical_df.drop_duplicates(), on=['Issue key'], 
                   how='left', indicator=True)
    new_df= merged_df.loc[merged_df['_merge'] == 'left_only']
    new_df = new_df.drop(columns=['Issue id_y', 'Summary_y', 'Reporter_y', 'Reporter Id_y',
       'Priority_y', 'Status_y', 'Created_y', 'Updated_y', 'Creator_y',
       'Creator Id_y', 'Custom field (Epic Link)_y', 'Labels_y'])
    new_df = new_df.set_axis(['Issue key', 'Issue id', 'Summary', 'Reporter', 'Reporter Id',
       'Priority', 'Status', 'Created', 'Updated', 'Creator',
       'Creator Id', 'Custom field (Epic Link)', 'Labels','Version',
       'Version Date', 'Version Reason', '_merge'], axis=1, inplace=False)
    new_df['Version']=0
    new_df['Version Date']=new_df['Updated']
    new_df['Version Reason']=''
    return new_df.drop('_merge',1)

def get_updated_rows(historical_df,weekly_df):
    updated_rows=pd.DataFrame().reindex(columns=historical_df.columns)
    merged_df = weekly_df.merge(historical_df.drop_duplicates(), on=['Issue key'], 
                   how='left', indicator=True)
    updated_df =merged_df.loc[merged_df['_merge'] == 'both']
    latest_idx=historical_df.groupby(['Issue key'])['Version'].transform(max) == historical_df['Version']
    latest_historical_data=historical_df[latest_idx]
    for issue_key in updated_df['Issue key']:
        updated=False
        reason=''
        if issue_key in historical_df['Issue key'].unique():
            historical_row = historical_df[historical_df['Issue key'] == issue_key].iloc[0]
            new_row=copy.deepcopy(historical_row)
            weekly_row = weekly_df.loc[weekly_df['Issue key'] == issue_key].iloc[0]
            for column in COLUMNS_TO_COMPARE:
                if historical_row[column]!=weekly_row[column]:
                    if column=='Status':
                        reason='{0} -> {1}'.format(new_row[column],weekly_row[column])
                    else:
                        reason='NA'
                    new_row[column]=weekly_row[column]
                    updated=True
            if updated:
                current_version = latest_historical_data[latest_historical_data['Issue key'] == issue_key].iloc[0]['Version']
                new_row['Version']=current_version+1
                new_row['Version Date']=weekly_row['Updated']
                new_row['Version Reason']=reason
                updated_rows.loc[len(updated_rows)] = new_row
    return updated_rows
        
