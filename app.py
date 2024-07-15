#IMPORTING LIBRARIES
from email import message
from tracemalloc import start
from flask import Flask, flash, render_template, request, jsonify,redirect
from numpy import zeros
from shapely.geometry import Point,Polygon

import pandas as pd




import folium
from datetime import date, datetime,time
from geopy.geocoders import Nominatim
from time import sleep, strftime
import csv

#######################################################################################################################
'''
READING COORDINATES FROM NAME
'''
# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="my_geocoder_app") # Function to get coordinates for a given place
def get_coordinates(place):
   location = geolocator.geocode(place)
   if location:
        return (location.latitude, location.longitude)
   else:
        raise Exception(f"Could not get coordinates for {place}")
# Places to geocode


app = Flask(__name__)
app.secret_key = 'your_secret_key'
i=0
C=[]
list_of_C=[]
map_instance = folium.Map(location=(10.800874457768161, 76.78083325901277), zoom_start=12)
# Sample vehicle details

#*******READING TOLL ZONE************************
# Define the corners of the toll area
toll_area_coords = [(10.800874457768161, 76.78083325901277
), (10.799205197444179, 76.78144017364988
), (10.825256523519297, 76.81391010673558
), (10.8361,76.867)]

vehicle={}
toll_polygon = Polygon(toll_area_coords)
toll_start=(10.80013677469304, 76.78150921255425)
toll_end =(10.799346364106235, 76.74865751636764)
coordinates_r =[]

#**********************************************************************************************************************
'''
STORING 
DATA
TO A
CSV FILE
'''
# CSV file path
data_file = 'login_data.csv'
csv_file='vehicle_data.csv'
try:
    # Try to load existing data
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    # If file does not exist, create an empty DataFrame
    df = pd.DataFrame(columns=['Starting Location', 'Ending Location', 'Time', 'Date','Tax Amount','Balance'])
def get_real_time_data(sn,e,t,b):
    data = {
        'Starting Location': sn,
        'Ending Location': e,
        'Time': datetime.now().strftime("%H:%M:%S"),
        'Date': datetime.now().strftime("%Y-%m-%d"),
        'Tax Amount':t,
        'Balance':b        
    }
    return data

def collect_and_store_data(sn,e,t,b):
    try:
        # Try to load existing data
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        # If file does not exist, create an empty DataFrame
        df = pd.DataFrame(columns=['Starting Location', 'Ending Location', 'Time', 'Date','Tax Amount','Balance'])

    # Get real-time data
    data_to_append = get_real_time_data(sn,e,t,b)
    # Convert the dictionary to a DataFrame
    new_data = pd.DataFrame([data_to_append])
    # Append the new data to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    # Save the updated DataFrame to the CSV file
    df.to_csv(csv_file, index=False)
#*****************************************************************************************************************
flag=0
# map_instance = folium.Map(location=road_start, zoom_start=12)
'''
FUNCTION TO DETERMINE PEAK TIME
'''
def simulate(coordinates_road):
    global coordinates_r
    coordinates_r=coordinates_road#value globally assigned 
def get_time_type(current_time):
    # Define the time ranges and their labels
    time_ranges = [
        ((7, 0), (9, 0), "Peak Time"),
        ((16, 0), (18, 0), "Peak Time"),
        ((9, 0), (16, 0), "Non-Peak Time"),
        ((18, 0), (23, 59), "Non-Peak Time"),
        ((0, 0), (7, 0), "Off-Peak Time"),
    ]

    # Convert current_time to time object for comparison
    current_time_obj = current_time.time()

    # Check current_time against defined time ranges
    for start, end, label in time_ranges:
        start_time = time(*start)
        end_time = time(*end)
        
        if start_time <= current_time_obj <= end_time:
            return label

    return "Unknown Time"
def fetch_vehicle_data(username):
         try:
            df=pd.read_csv(csv_file)
            user_data=df[df['Username'] == username].iloc[0]
            vehicle_type=user_data['Vehicle Type']
            balance=float(user_data['Balance'])
            return vehicle_type,balance
         except Exception as e:
            print(f"Error Fetching Vehicle Data: {e}")
            return None,None
############################################################################ 
@app.route('/')
def index1():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register_submit():
    # Fetch form data
    global Balance
    name = request.form['name']
    reg_number = request.form['reg_number']
    Username = request.form['Username']
    vehicle_type = request.form['vehicle_type']
    Balance = request.form['Balance']

    # Prepare data to append to CSV
    data = {
        'Name': name,
        'Registration Number': reg_number,
        'Username': Username,
        'Vehicle Type': vehicle_type,
        'Balance': Balance
    }

    # Append data to CSV
    with open(data_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()  # Write header only if file is empty
        writer.writerow(data)

    # Redirect back to login page after successful registration
    return render_template('login.html')

# Function to check if username exists in CSV file
def check_username(username):
    try:
        with open(data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    return True
        return False
    except FileNotFoundError:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global start_location,end_location
        username = request.form['username']
        start_location = request.form['start_location']
        end_location = request.form['end_location']
        global z,y,vehicle
        z = get_coordinates(start_location)
        print(f"Coordinates of 0{'start_point'}: {z}")
        sleep(1)  # Sleep for 1 second to avoid hitting rate limits
        y = get_coordinates(end_location)
        print(f"Coordinates of {'end_point'}: {y}")
        # Get coordinates with a delay to avoid hitting usage limits
        vehicle_type,balance=fetch_vehicle_data(username)
        if vehicle_type is not None and balance is not None:
            vehicle ={
                'type':vehicle_type,
                'balance':balance
            }

    if check_username(username):    
            return render_template('index.html',map=map_instance._repr_html_(),start_point=z,end_point=y)
    else:
            # Handle invalid username (e.g., show error message)
            flash('Your Username is Invalid..Try Again')
            return render_template('register.html', message="Error")

# @app.route('/process', methods=['POST'])
# def process(): 
#     global start_location,end_location
#     start_location = request.form['start_location']
#     end_location = request.form['end_location']
#     balance = request.form['balance']
#     vehicle_type = request.form['vehicle-select']
#     recharge_amount = request.form.get('recharge', 0)  # Default to 0 if not provided

#     # Process the data
#     processed_data = process_data( balance, vehicle_type, recharge_amount)
#     print(processed_data)

    # Render the result page and pass processed data
    # return render_template('result.html', data=processed_data)
@app.route('/index')
def index():
    # Render the index.html template with the map instance
    return render_template('index.html', map=map_instance._repr_html_(),start_point=(9.6287383, 76.64553257390992),end_point=(-1.87534,87.876545))

@app.route("/page2")
def page2():
    
    # Render another HTML file with the same map instance
    return render_template('page2.html',map=map_instance._repr_html_(),start_point=toll_start,end_point=toll_end)

@app.route('/save_coordinates_route1', methods=['POST'])  
def save_coordinates_route1():

    data_road = request.json
    coordinates_road = data_road.get('coordinates')
    simulate(coordinates_road)
    # Process the received coordinates for Route 1
    #print('Received coordinates for ROAD:', coordinates_road)
    # Example response
    
    return jsonify(status='success', message='Received coordinates for Route 1')


@app.route('/save_coordinates_route2', methods=['POST'])
def save_coordinates_route2():
    
    data_toll = request.json
    #print(type(data_toll)) dict
    return jsonify(status='success', message='Received coordinates for Route 2')


@app.route("/page3")
def page3():
    #define the list of tuples here !!!!!!!!!
    #coordinates_r=simulate()#check for toll zones and convert list of dict into list of tuples and pass to next html file
    global flag
   
    #print("CCCCC=",coordinates_r)
    vehicle_df = pd.DataFrame(coordinates_r)
    vehicle_geometry = [Point(xy) for xy in zip(vehicle_df['lat'], vehicle_df['lng'])]
    
    inside_toll_zone=[] 
    for i in vehicle_geometry:
        if toll_polygon.contains(i):
            inside_toll_zone.append(i)
            flag=1
            # Optionally, print or log a message
            # print(f"The point {i} is inside the toll zone")
        else:
            # Optionally, print or log a message
            # print(f"The point {i} is outside the toll zone.")
            pass
    coordinates_tuples = [(point.x, point.y) for point in inside_toll_zone]
# Convert to list of tuples
    
    # Render another HTML file with the same map instance
    return render_template('page3.html',map=map_instance._repr_html_(),start_point=coordinates_tuples[0],end_point=coordinates_tuples[-1])

@app.route('/save_coordinates_route3', methods=['POST'])
def save_coordinates_route3():
    global tax,B
    tax=0
    B=vehicle['balance']
    data_travelled = request.json
    # print(type(data_toll)) dict
    summary=data_travelled.get('summary') 
    print(summary)
    if flag==1:
        # Get the current time
        current_time =datetime.now()
        global time_type
# Determine the type of time
        time_type = get_time_type(current_time)
        #Determining base rate on the basis of vehicle
        T='Car'
        D=summary['totalDistance']/1000
        print("Distance in kms=",D)
        base_rate = {
         'Car': 0.65,
         'Jeep': 0.65,
         'Van': 0.65,
         'Light motor vehicle': 0.65,
         'Light commercial vehicle': 1.05,
         'Light goods vehicle': 1.05,
         'Mini bus': 1.05,
         'Bus': 2.2,
         'Truck': 2.2,
         'Others': 3.39
         }
       
        #tax calculation 
     
        B=vehicle['balance']
    
        if T in base_rate:
           tax=base_rate[T] * D
           if time_type=="Peak Time":
              B=B-5
        if tax<B:
            B=B-tax
            print("Total amount=",tax)
            print("Balance=",B)
            vehicle['balance']=B
        else:
            flash("Not Enough Balance")
            print(tax-B,"more needed")

    collect_and_store_data(z,y,tax,B)  

    # Example response
    return jsonify(status='success', message='Received coordinates for Route 2')
@app.route('/receipt')
def receipt():
 
    try:
        df=pd.read_csv(csv_file)
        if df.empty:
            print("No transactions found in the DataFrame.")
    # Process the latest transaction
        else:
          latest_transaction = df.tail(1).iloc[0]
          return render_template('receipt.html',start_location=start_location,end_location=end_location,date=datetime.now().strftime("%Y-%m-%d"),time=datetime.now().strftime("%H:%M:%S"),t=tax,balance=B)
        
    except FileNotFoundError:
        return render_template(receipt.html)

# Route to display transaction history
@app.route('/transaction_history')
def transaction_history():
    try:
        df = pd.read_csv(csv_file)
        transactions = df.to_dict('records')  # Convert DataFrame to list of dictionaries
        return render_template('transaction_history.html', transactions=transactions)
    except FileNotFoundError:
        flash("No transactions found.")
        return render_template('transaction_history.html')

if __name__ == '__main__':
    app.run(debug=True)
