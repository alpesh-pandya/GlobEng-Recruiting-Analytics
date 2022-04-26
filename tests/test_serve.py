import pandas as pd
from data.serve import get_counts, get_update_insights, merge_dataframes,get_latest_snapshot

def test_get_counts():
    data = [
        ['HR-11', '03/APR/21 2:34 PM','Recruiter Screen','ML Eng','TH']
        , ['HR-99', '23/Aug/21 10:11 AM','Onsite','App Eng','Hired']
        , ['HR-03', '29/Dec/21 5:10 PM','Onsite','ML Eng','LinkedIn']
        , ['HR-23', '21/Dec/21 5:10 PM','Rejected','App Eng','TH']
        , ['HR-70', '07/Feb/22 5:10 PM','Offer Accepted','Front End Eng','TH']
        , ['HR-900', '07/Feb/22 5:10 PM','Onsite','App Eng','LinkedIn']
        , ['HR-732', '07/Feb/22 5:10 PM','Tech Screen','App Eng','LinkedIn']
        , ['HR-159', '29/Dec/21 5:10 PM','Tech Screen','ML Eng','TH']
        ,['HR-113', '03/APR/21 2:34 PM','Recruiter Screen','ML Eng','LinkedIn']
    ]
    dataframe = pd.DataFrame(data, columns = ['Issue key', 'Updated','Status','Custom field (Epic Link)','Labels'])
    result=get_counts(dataframe, ['Custom field (Epic Link)','Status'])
    assert len(result)==7

def test_merge_dataframes():
    data1=[['a',0,'b',1]]
    data2=[['c',2,'d',3]]
    data3=[['e',4,'f',5]]
    df1=pd.DataFrame(data1, columns=['name1','number1','name2','number2'])
    df2=pd.DataFrame(data2, columns=['name1','number1','name2','number2'])
    df3=pd.DataFrame(data3, columns=['name1','number1','name2','number2'])
    merged_df = merge_dataframes(df1,df2,df3)
    assert len(merged_df)==3
    assert len(df1)==1

def test_get_update_insights():
    updated_data=[
        ['EMEA Data Eng SM','Tech Screen -> Onsite']
        ,['APAC APP Eng','Recruiter Screen -> Tech Screen']
        ,['AMER Infra Eng','Onsite -> Leadership']
        ,['EMEA App Eng','Leadership -> Rejected']
        ,['APAC Data Eng','Leadership -> Offer']
        ,['AMER Data Eng','Offer -> Accepted']
        ,['APAC APP Eng','Tech Screen -> Onsite']
        ,['AMER Infra Eng','Leadership -> Rejected']
        ,['EMEA App Eng','Leadership -> Accepted']
        ,['APAC Data Eng','Onsite -> Leadership']
        ,['AMER Data Eng','Recruiter Screen -> Tech Screen']
        ,['APAC APP Eng','Tech Screen -> Onsite']
        ,['AMER Infra Eng','Leadership -> Rejected']
        ,['EMEA App Eng','Leadership -> Offer']
        ,['APAC Data Eng','Offer -> Accepted']
        ,['AMER Data Eng','Recruiter Screen -> Tech Screen']
        ,['APAC APP Eng','Tech Screen -> Rejected']
        ,['AMER Infra Eng','Tech Screen -> Onsite']
        ,['EMEA App Eng','Onsite -> Leadership']
        ,['APAC Data Eng','Leadership -> Offer']
        ,['AMER Data Eng','Offer -> Accepted']
    ]
    updated_df=pd.DataFrame(updated_data, columns=['Custom field (Epic Link)','Version Reason'])
    insights = get_update_insights(updated_df)
    assert len(insights)==16

def test_get_latest_snapshot():
    data=[
        ['001',0],['002',0],['003',0],['004',0]
        ,['001',2],['002',1],['003',1],['004',1]
        ,['001',3],['002',2]
    ]
    df=pd.DataFrame(data, columns=['Issue key','Version'])
    latest_snapshot=get_latest_snapshot(df)
    assert len(latest_snapshot)==4