import pandas as pd
from datetime import datetime

# Simulate data generation (replace with actual data retrieval logic)
def get_real_time_data():
    data = {
        'start_place': " ",
        'end_place': " ",
        'balance': 0.0,
        'real_time': datetime.now().strftime("%H:%M:%S"),
        'date': datetime.now().strftime("%Y-%m-%d"),
        'status': " "
    }
    return data

# CSV file path
csv_file = 'vehicle_data.csv'

def collect_and_store_data():
    # Initialize pandas DataFrame
    try:
        # Try to load existing data
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        # If file does not exist, create an empty DataFrame
        df = pd.DataFrame(columns=['number_plate_no', 'vehicle_type', 'balance', 'real_time', 'date'])

    # Get real-time data
    data_to_append = get_real_time_data()
    # Convert the dictionary to a DataFrame
    new_data = pd.DataFrame([data_to_append])
    # Append the new data to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    # Save the updated DataFrame to the CSV file
    df.to_csv(csv_file, index=False)
