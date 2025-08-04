import pandas as pd

def load_precipitation(file_path):
    try:
        df = pd.read_csv(file_path, encoding="shift_jis")
        return df
    except Exception as e:
        print(f"Failed to load precipitation data: {e}")
        return pd.DataFrame()

def load_temperature(min_temp_path, max_temp_path):
    try:
        min_df = pd.read_csv(min_temp_path, encoding="shift_jis")
        max_df = pd.read_csv(max_temp_path, encoding="shift_jis")
        return pd.concat([min_df, max_df], ignore_index=True)
    except Exception as e:
        print(f"Failed to load temperature data: {e}")
        return pd.DataFrame()

def load_wind(max_wind_path, inst_wind_path):
    try:
        max_df = pd.read_csv(max_wind_path, encoding="shift_jis")
        inst_df = pd.read_csv(inst_wind_path, encoding="shift_jis")
        return pd.concat([max_df, inst_df], ignore_index=True)
    except Exception as e:
        print(f"Failed to load wind data: {e}")
        return pd.DataFrame()
