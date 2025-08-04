import os
import pandas as pd
from data_loader import (
    load_precipitation,
    load_temperature,
    load_wind
)

# Automatically detect the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def main():
    # Paths to the CSV files
    precipitation_file = os.path.join(DATA_DIR, "all_elements_of_precipitation.csv")
    daily_precip_file = os.path.join(DATA_DIR, "daily_precipitation.csv")
    max_temp_file = os.path.join(DATA_DIR, "highest_temperature.csv")
    min_temp_file = os.path.join(DATA_DIR, "minimum_temperature.csv")
    max_wind_speed_file = os.path.join(DATA_DIR, "maximum_wind_speed.csv")
    max_instant_wind_speed_file = os.path.join(DATA_DIR, "maximum_instantaneous_wind_speed.csv")

    # Load data using helper functions
    precipitation_df = load_precipitation(precipitation_file)
    daily_precip_df = load_precipitation(daily_precip_file)
    temperature_df = load_temperature(min_temp_file, max_temp_file)
    wind_df = load_wind(max_wind_speed_file, max_instant_wind_speed_file)

    # Show summaries
    print("\n📊 All Elements of Precipitation:")
    print(precipitation_df.head())

    print("\n🌧️ Daily Precipitation:")
    print(daily_precip_df.head())

    print("\n🌡️ Temperature Data:")
    print(temperature_df.head())

    print("\n🌬️ Wind Data:")
    print(wind_df.head())

if __name__ == "__main__":
    main()

