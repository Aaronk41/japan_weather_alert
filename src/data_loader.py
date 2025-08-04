import pandas as pd

def load_precipitation(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
   
    df.rename(columns={
        '観測所番号': 'station_id',
        '降水量(ｍｍ)': 'precipitation',
        '観測時間': 'observation_time'
    }, inplace=True)
    df['observation_time'] = pd.to_datetime(df['observation_time'], errors='coerce')
    return df

def load_wind_speed(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df.rename(columns={
        '観測所番号': 'station_id',
        '最大瞬間風速(m/s)': 'max_instant_wind_speed',
        '最大風速(m/s)': 'max_wind_speed',
        '観測時間': 'observation_time'
    }, inplace=True)
    df['observation_time'] = pd.to_datetime(df['observation_time'], errors='coerce')
    return df

def load_temperature(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df.rename(columns={
        '観測所番号': 'station_id',
        '気温(℃)': 'temperature',
        '観測時間': 'observation_time'
    }, inplace=True)
    df['observation_time'] = pd.to_datetime(df['observation_time'], errors='coerce')
    return df
