def get_max_instant_wind_speed(df, station_id: str) -> float:
    filtered = df[df['station_id'] == station_id]
    if filtered.empty:
        return 0.0
    max_speed = filtered['max_instant_wind_speed'].max()
    return round(max_speed, 2)

def get_max_wind_speed(df, station_id: str) -> float:
    filtered = df[df['station_id'] == station_id]
    if filtered.empty:
        return 0.0
    max_speed = filtered['max_wind_speed'].max()
    return round(max_speed, 2)
