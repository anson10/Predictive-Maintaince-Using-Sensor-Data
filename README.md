# Predictive Maintenance Using Sensor Data

This project aims to predict the Remaining Useful Life (RUL) of machines using sensor data. The solution leverages LSTM (Long Short-Term Memory) networks, a type of recurrent neural network, to process time-series sensor data and predict when a machine is likely to fail. This can significantly reduce maintenance costs by allowing for proactive maintenance rather than reactive repairs.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Data Description](#data-description)
6. [Model](#model)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

Predictive maintenance aims to predict when equipment will fail so that maintenance can be performed just in time to address the issue before a breakdown occurs. This project predicts the Remaining Useful Life (RUL) of industrial engines using historical sensor data collected during operation.

The project uses an LSTM neural network model trained on time-series sensor data to predict RUL. The solution allows users to upload a CSV or TXT file containing sensor data, and the model will output the predicted RUL for each engine.

---

## Technologies Used

- **Python** 3.x
- **TensorFlow** for model training and prediction
- **Streamlit** for creating an interactive web application
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Scikit-learn** for data preprocessing (scaling)
- **Matplotlib** for visualization (optional)

---

## Setup Instructions

### Prerequisites

1. Python 3.x installed on your machine.
2. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Required Libraries

- TensorFlow
- Streamlit
- Pandas
- NumPy
- Scikit-learn

To install the dependencies:

```bash
pip install tensorflow streamlit pandas numpy scikit-learn
```

---

## Usage

### 1. Start the Streamlit Web Application

To run the application, execute the following command:

```bash
streamlit run app.py
```

This will start a local web server, and the Streamlit interface will be available in your browser at `http://localhost:8501`.

### 2. Upload Test Data

- The app will prompt you to upload a CSV or TXT file containing the sensor data.
- Use the **Window Size** slider to choose the window size for the LSTM model.
- Once the data is uploaded, the model will make predictions and display them.

### 3. View Results and Download

After the predictions are made, the results will be displayed on the interface. You can download the predictions as a CSV file by clicking the **Download Predictions** button.

---

## Data Description

The dataset consists of multiple time-series data of sensors from engines. The columns in the dataset are:

- **engine_id**: Unique identifier for each engine.
- **cycle**: Cycle number (incremental for each engine).
- **op_setting_1, op_setting_2, op_setting_3**: Operational settings of the engine.
- **sensor_1 to sensor_21**: Sensor readings related to engine conditions.
- **RUL (Remaining Useful Life)**: The number of remaining cycles until failure (calculated in preprocessing).

You can upload your own dataset in the required format or use the provided example datasets.

---

## Model

### Preprocessing
1. **Feature Engineering**: The remaining useful life (RUL) of each engine is computed based on the maximum cycle number for each engine.
2. **Data Windowing**: To make the data suitable for LSTM, a sliding window approach is used to extract sequences of sensor data (with a given window size).

### Model Architecture
- **LSTM** (Long Short-Term Memory) network is used for time-series prediction.
- The model consists of one or more LSTM layers, followed by Dense layers for final output prediction.

### Model Training
The model is trained using historical sensor data, and the model weights are saved to a `.h5` file (`best_model.h5`).

### Model Prediction
When a test dataset is uploaded, the model makes predictions for the RUL of each engine.

---

## Results

The predicted RUL values will be shown in a table, and you can download the predictions as a CSV file for further analysis.

**Example Output**:

| Engine ID | Cycle | Predicted RUL | Actual RUL |
|-----------|-------|---------------|------------|
| 1         | 100   | 15            | 18         |
| 2         | 150   | 12            | 10         |
| 3         | 200   | 6             | 5          |

---

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Clone your forked repository to your local machine.
3. Create a new branch (`git checkout -b feature-branch`).
4. Make your changes and commit (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

