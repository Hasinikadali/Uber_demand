import pandas as pd

def preprocess_for_city(path, city_name):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    city_data = df[df['City'] == city_name].copy()
    city_data.set_index('Date', inplace=True)
    return city_data