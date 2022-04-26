import pandas as pd
from data.transform import get_new_rows, get_updated_rows

def test_get_new_rows():
    historical_data = [['HR-1', '03/APR/21 2:34 PM',0], ['HR-99', '21/Aug/21 10:11 AM',76], ['HR-03', '13/Dec/21 5:10 PM',302]]
    weekly_data = [['HR-11', '10/Mar/22 1:29 PM',100], ['HR-99', '21/Aug/21 10:11 AM',76], ['HR-33', '18/Jan/22 8:12 PM',302]]
    historical_df = pd.DataFrame(historical_data, columns = ['Issue key', 'Updated','count'])
    weekly_df = pd.DataFrame(weekly_data, columns = ['Issue key', 'Updated','count'])
    new_df = get_new_rows(historical_df,weekly_df)
    assert len(new_df)==2
    assert 'Version' in new_df.columns

def test_get_updated_rows():
    historical_data = [
        ['HR-1', '03/APR/21 2:34 PM','Recruiter Screen','ML Eng','TH',0,'03/APR/21 2:34 PM','']
        , ['HR-99', '21/Aug/21 10:11 AM','Tech Screen','App Eng','Hired',0,'21/Aug/21 10:11 AM','']
        , ['HR-03', '13/Dec/21 5:10 PM','Onsite','Data Eng','LinkedIn',0,'13/Dec/21 5:10 PM','']
        , ['HR-23', '23/Nov/21 5:10 PM','Rejected','Infra Eng','',0,'23/Nov/21 5:10 PM','']
        , ['HR-7', '07/Feb/22 5:10 PM','Offer Accepted','Front End Eng','TH',0,'07/Feb/22 5:10 PM','']
    ]
    weekly_data = [
        ['HR-11', '03/APR/21 2:34 PM','Recruiter Screen','ML Eng','TH']
        , ['HR-99', '23/Aug/21 10:11 AM','Onsite','App Eng','Hired']
        , ['HR-03', '29/Dec/21 5:10 PM','Onsite','ML Eng','LinkedIn']
        , ['HR-23', '21/Dec/21 5:10 PM','Rejected','Infra Eng','TH']
        , ['HR-70', '07/Feb/22 5:10 PM','Offer Accepted','Front End Eng','TH']
    ]
    historical_df = pd.DataFrame(historical_data, columns = ['Issue key', 'Updated','Status','Custom field (Epic Link)','Labels'
        ,'Version','Version Date','Version Reason'])
    weekly_df = pd.DataFrame(weekly_data, columns = ['Issue key', 'Updated','Status','Custom field (Epic Link)','Labels'])
    updated_df = get_updated_rows(historical_df,weekly_df)
    print(updated_df)
    assert len(updated_df)==3
    assert updated_df['Status'].iloc[0]=='Onsite'
    assert updated_df['Custom field (Epic Link)'].iloc[1]=='ML Eng'
    assert updated_df['Labels'].iloc[2]=='TH'
    assert updated_df['Version'].iloc[0]==1
    

    