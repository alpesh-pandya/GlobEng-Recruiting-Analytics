from data.load import historical_data,weekly_data

def test_historical_data():
    assert len(historical_data('hiring_dashboard_historical_good.csv'))==1000
    
    try:
        historical_data('hiring_dashboard_historical_small.csv')
    except Exception as ex:
        assert ex.__str__()=='Insufficient historical data. Please download historical data CSV file from JIRA.'

    try:
        historical_data('hiring_dashboard_historical_validations.csv')
        assert False
    except Exception as ex:
        print(ex.__str__())
        assert True

def test_weekly_data():
    assert len(weekly_data('hiring_dashboard_weekly_good.csv'))==56

    try:
        weekly_data('hiring_dashboard_weekly_empty.csv')
    except Exception as ex:
        assert ex.__str__()=='No records to process from weekly data'

    try:
        weekly_data('hiring_dashboard_weekly_validations.csv')
        assert False
    except Exception as ex:
        print(ex.__str__())
        assert True