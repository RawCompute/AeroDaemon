import pandas as pd
from pathlib import Path

def load_cmapss_data(file_path):
    # NASA's 26 columns
    columns = [
        'engine_id', 'cycle', 'setting_1', 'setting_2', 'setting_3', 
        'sensor_1', 'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 
        'sensor_6', 'sensor_7', 'sensor_8', 'sensor_9', 'sensor_10', 
        'sensor_11', 'sensor_12', 'sensor_13', 'sensor_14', 'sensor_15', 
        'sensor_16', 'sensor_17', 'sensor_18', 'sensor_19', 'sensor_20', 'sensor_21'
    ]
    
    # Load 
    df = pd.read_csv(file_path, sep=r'\s+', header=None, names=columns)
    return df

data_file = Path(__file__).resolve().parent.parent / 'data' / 'train_FD001.txt'
df = load_cmapss_data(data_file)

# Calculate Remaining Useful Life (RUL)
df['RUL'] = df.groupby('engine_id')['cycle'].transform('max') - df['cycle']

print(df[['engine_id', 'cycle', 'RUL']].head())