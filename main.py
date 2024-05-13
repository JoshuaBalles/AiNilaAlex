import os
import requests
import time
import pandas as pd
from joblib import load

nodeMCU_ip = '192.168.100.176'
variables = ['temp_val', 'moist_val', 'n_val', 'p_val', 'k_val']

# Load the model and scaler
model = load("svm_model.joblib")
scaler = load("scaler.joblib")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear command prompt
    values = {}  # Dictionary to store values

    for variable_name in variables:
        response = requests.get(f'http://{nodeMCU_ip}/{variable_name}')
        variable = float(response.text)
        values[variable_name] = variable

    # Print all values at once
    for variable_name, value in values.items():
        print(f'{variable_name}: {value}')

    # Convert the values dictionary to a DataFrame
    input_values = pd.DataFrame([values])

    # Scale the features using the loaded scaler
    input_values_scaled = scaler.transform(input_values)

    # Make a prediction using the loaded model
    predicted_cured = model.predict(input_values_scaled)

    # Output the result
    print("Predicted 'cured' status:", "Yes" if predicted_cured[0] else "No")

    time.sleep(2)  # Pause for one second
