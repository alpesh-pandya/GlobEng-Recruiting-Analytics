import os
import pandas as pd
import pandas_schema as schema
from config import INPUT_DATA_PATH,WEEKLY_SCHEMA,HISTORICAL_SCHEMA

def enrich_historical_data(historical_data):
    if 'Version' not in historical_data.columns:
        historical_data['Version']=0
    if 'Version Date' not in historical_data.columns:
        historical_data['Version Date']=historical_data['Updated']
    if 'Version Reason' not in historical_data.columns:
        historical_data['Version Reason']=''
    
    return historical_data

def historical_data(historical_data_file_name):
    historical_data_path = os.path.join(INPUT_DATA_PATH, historical_data_file_name)
    historical_data = pd.read_csv(historical_data_path)
    if 'Labels.1' in historical_data.columns: ## This due to JIRA bug of adding duplicate columns
        historical_data=historical_data.drop('Labels.1',1) 
    historical_data=enrich_historical_data(historical_data)
    errors = [ error.__str__() for error in HISTORICAL_SCHEMA.validate(historical_data)]
    if len(historical_data.index)<1000:
        errors.append('Insufficient historical data. Please download historical data CSV file from JIRA.')
    if len(errors)>0:
        err_msg=''.join(errors)
        raise Exception(err_msg)
    else:
        return historical_data

def weekly_data(weekly_data_file_name):
    weekly_data_path = os.path.join(INPUT_DATA_PATH, weekly_data_file_name)
    weekly_data = pd.read_csv(weekly_data_path)
    if 'Labels.1' in weekly_data.columns: ## This due to JIRA bug of adding duplicate columns
        weekly_data=weekly_data.drop('Labels.1',1) 
    errors = [error.__str__() for error in WEEKLY_SCHEMA.validate(weekly_data)]
    if len(weekly_data.index)<1:
        errors.append('No records to process from weekly data')
    if len(errors)>0:
        err_msg=''.join(errors)
        raise Exception(err_msg)
    else:
        return weekly_data
