def get_temperature_range(df_min, df_max, station_id: str):
    filtered_min = df_min[df_min['station_id'] == station_id]
    filtered_max = df_max[df_max['station_id'] == station_id]

    if filtered_min.empty or filtered_max.empty:
        return None, None

    min_temp = filtered_min['temperature'].min()
    max_temp = filtered_max['temperature'].max()
    return round(min_temp, 2), round(max_temp, 2)
