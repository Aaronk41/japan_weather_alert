from data_loader import load_precipitation, load_wind_speed, load_temperature
from precipitation import get_total_precipitation_last_24h
from wind import get_max_instant_wind_speed, get_max_wind_speed
from temperature import get_temperature_range

def main():

    precipitation_file = '../data/all_elements_of_precipitation.csv'
    max_instant_wind_file = '../data/maximum_instantaneous_wind_speed.csv'
    max_wind_file = '../data/maximum_wind_speed.csv'
    min_temp_file = '../data/minimum_temperature.csv'
    max_temp_file = '../data/highest_temperature.csv'

    precipitation_df = load_precipitation(precipitation_file)
    max_instant_wind_df = load_wind_speed(max_instant_wind_file)
    max_wind_df = load_wind_speed(max_wind_file)
    min_temp_df = load_temperature(min_temp_file)
    max_temp_df = load_temperature(max_temp_file)

  
    station_id = '12345'

    precip_24h = get_total_precipitation_last_24h(precipitation_df, station_id)
    max_instant_wind = get_max_instant_wind_speed(max_instant_wind_df, station_id)
    max_wind = get_max_wind_speed(max_wind_df, station_id)
    min_temp, max_temp = get_temperature_range(min_temp_df, max_temp_df, station_id)

    print(f"Station {station_id}:")
    print(f"  24h Precipitation: {precip_24h} mm")
    print(f"  Max Instantaneous Wind Speed: {max_instant_wind} m/s")
    print(f"  Max Wind Speed: {max_wind} m/s")
    print(f"  Temperature Range: {min_temp}°C to {max_temp}°C")

if __name__ == "__main__":
    main()
