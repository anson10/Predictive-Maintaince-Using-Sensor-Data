import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf

def preprocess_data_without_scaling(data, window_size):
    data['RUL'] = data.groupby('engine_id')['cycle'].transform('max') - data['cycle']

    X, y = [], []
    for engine_id in data['engine_id'].unique():
        sensor_columns = [col for col in data.columns if isinstance(col, str) and 'sensor' in col]
        engine_data = data[data['engine_id'] == engine_id][sensor_columns].values
        engine_rul = data[data['engine_id'] == engine_id]['RUL'].values
        for i in range(len(engine_data) - window_size):
            X.append(engine_data[i:i + window_size])
            y.append(engine_rul[i + window_size])

    X = np.array(X)
    y = np.array(y)

    return X, y

# Load trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('../models/best_model.h5')

# Streamlit UI
st.title("Predictive Maintenance Using LSTM")

st.write("Upload a test data file to get started!")

# File uploader
file = st.file_uploader("Upload test data file", type=['csv', 'txt'])
window_size = st.slider("Window Size", 10, 50, 30, 5)

if file is not None:
    # Load and display uploaded data
    test_data = pd.read_csv(file, sep=r'\s+', header=None)  
    test_data = test_data.dropna(axis=1, how='all')  # Drop empty columns
    num_columns = test_data.shape[1]

    # Dynamically assign column names
    column_names = ['engine_id', 'cycle', 'op_setting_1', 'op_setting_2', 'op_setting_3',
                    'sensor_1', 'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 'sensor_6',
                    'sensor_7', 'sensor_8', 'sensor_9', 'sensor_10', 'sensor_11', 'sensor_12',
                    'sensor_13', 'sensor_14', 'sensor_15', 'sensor_16', 'sensor_17', 'sensor_18',
                    'sensor_19', 'sensor_20', 'sensor_21']
    test_data.columns = column_names[:num_columns] 

    # Display the uploaded data
    st.write("Uploaded Data Sample:")
    st.write(test_data.head())

    # Load model
    model = load_model()

    # Preprocess data without scaling
    try:
        X_test, y_test = preprocess_data_without_scaling(test_data, window_size)
    except Exception as e:
        st.error(f"Error during preprocessing: {e}")
        st.stop()

    # Make predictions
    predictions = model.predict(X_test)

    # Display results
    st.write("### Predictions (RUL)")
    results = pd.DataFrame({
        'Predicted RUL': predictions.flatten(),
        'Actual RUL': y_test
    })
    st.write(results.head())

    # Download results
    csv = results.to_csv(index=False)
    st.download_button(
        label="Download Predictions as CSV",
        data=csv,
        file_name="predicted_rul.csv",
        mime="text/csv"
    )
