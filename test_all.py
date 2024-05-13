# import os
# import requests
# import time

# nodeMCU_ip = '192.168.100.176'
# variables = ['temp_val', 'moist_val', 'n_val', 'p_val', 'k_val']

# while True:
#     os.system('cls' if os.name == 'nt' else 'clear')  # Clear command prompt
#     for variable_name in variables:
#         response = requests.get(f'http://{nodeMCU_ip}/{variable_name}')
#         variable = float(response.text)
#         print(f'{variable_name}: {variable}')
#     time.sleep(1)  # Pause for one second

import os
import requests
import time

nodeMCU_ip = '192.168.100.176'
variables = ['temp_val', 'moist_val', 'n_val', 'p_val', 'k_val']

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
    
    time.sleep(1)  # Pause for one second
