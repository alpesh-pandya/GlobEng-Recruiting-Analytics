import os
from pandas_schema import Column, Schema, validation

INPUT_DATA_PATH=os.environ['INPUT_DATA_PATH']
OUTPUT_PATH=os.environ['OUTPUT_DATA_PATH']

weekly_columns=[
    Column('Issue key',[],False)
    ,Column('Issue id')
    ,Column('Summary',[],False)
    ,Column('Reporter',[],False)
    ,Column('Reporter Id')
    ,Column('Priority')
    ,Column('Status',[],False)
    ,Column('Created',[validation.DateFormatValidation('%d/%b/%y %I:%M %p')],False)
    ,Column('Updated',[validation.DateFormatValidation('%d/%b/%y %I:%M %p')],False)
    ,Column('Creator',[],False)
    ,Column('Creator Id')
    ,Column('Custom field (Epic Link)',[],False)
    ,Column('Labels')
]
additional_historical_columns=[
    Column('Version',[],False)
    ,Column('Version Date',[validation.DateFormatValidation('%d/%b/%y %I:%M %p')],False)
    ,Column('Version Reason')
]

WEEKLY_SCHEMA = Schema(weekly_columns)
HISTORICAL_SCHEMA = Schema(weekly_columns+additional_historical_columns)

COLUMNS_TO_COMPARE=['Status','Custom field (Epic Link)','Labels']