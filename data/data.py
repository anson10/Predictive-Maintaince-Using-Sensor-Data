# import kagglehub
import pandas as pd

# # Download latest version
# path = kagglehub.dataset_download("behrad3d/nasa-cmaps")

# print("Path to dataset files:", path)

column_names = [
    'engine_id', 'cycle', 'op_setting_1', 'op_setting_2', 'op_setting_3',
    'sensor_1', 'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 'sensor_6',
    'sensor_7', 'sensor_8', 'sensor_9', 'sensor_10', 'sensor_11', 'sensor_12',
    'sensor_13', 'sensor_14', 'sensor_15', 'sensor_16', 'sensor_17', 'sensor_18',
    'sensor_19', 'sensor_20', 'sensor_21'
]

train_data = pd.read_csv('test_data.csv', header=None, names=column_names)
train_data.to_csv('test_dataH.csv', index=False)