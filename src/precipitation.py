import pandas as pd

def get_total_precipitation_last_24h(df: pd.DataFrame, station_id: str) -> float:
    from datetime import datetime, timedelta
    now = datetime.now()
    since = now - timedelta(hours=24)
    filtered = df[(df['station_id'] == station_id) & (df['observation_time'] >= since)]
    total_precip = filtered['precipitation'].sum()
    return round(total_precip, 2)
