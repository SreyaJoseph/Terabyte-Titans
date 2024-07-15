## Team Terabyte-Titans
## GPS TOLL-BASED SYSTEM SIMULATION USING PYTHON

## Introduction

This project simulates a GPS-based toll collection system for vehicles. The system collects and stores real-time data, including vehicle information, journey details and payment status for tolls. The project is implemented in Python and uses a structured approach to manage and process vehicle data efficiently.

## Features

- **Real-time data collection**: Tracks vehicle journey in real-time.
- **Data Storage**: Stores vehicle data such as vehicle number, type, start and end points,balance, journey date, and payment status.
- **User Management**: Associates vehicle details with user IDs and extract relevant information when a journey starts.
- **Toll Payment Status**: Manages and updates the payment status for each journey.

## Technologies Used 

- `HTML`
- `CSS`
- `Javascript`
- `Leaflet`
- `Python`

## Implementation


To begin, you'll need to set up your Python environment with essential libraries.Once your environment is configured, the next step involves loading geographic data that defines the toll zones and possibly road networks.With the geographic data loaded, you can visualize the toll zones and road networks to ensure they are correctly defined. Visualization can be done using plotting libraries like Folium for interactive maps.

Toll Zone Detection approaches we adopted are:

Approach 1 : We simulated vehicle movement and toll zone entry using Python libraries like geopandas. Each vehicle has a starting point, destination, and balance. We calculated distances and apply taxes based on vehicle type and distance traveled within toll zones. Flags and functions manage zone entry checks and balance deductions during simulation.
The limitation of this approach in our GPS Toll system simulation project using Python is that since the vehicle moves irregularly, not following a continuous path along the desired points from the starting point to the ending point, toll zones cannot be reliably detected along the route.The irregular movement of vehicles in your GPS Toll system simulation project is due to using a mathematical formula that places the next points randomly after the starting point. This approach disrupts continuous movement, affects distance calculation, and results in inaccurate movements, ultimately leading to unreliable detection of toll zones along the route.


Approach 2 :Our second approach for the GPS toll system simulation using Python involves creating an interactive map with Leaflet and integrating it with Python code using Flask. We begin by passing coordinates entered by the user to the Python script and then to an HTML file, which then displays these coordinates correctly on the map. As the coordinates are processed, we calculate the toll rate based on the distance travelled and time taken, providing detailed summaries.  We check if the road coordinates intersect with toll zone coordinates. If a vehicle enters a toll zone, we record the coordinates as long as they remain within the zone.The limitation in this approach is that, even if a toll zone is located between the starting and ending coordinates, the coordinates are displayed as non-intersecting lines due to the marking format in Leaflet. Leaflet represents them as two separate lines, even when the starting and ending coordinates are the same, resulting in no coinciding points. Our concept relies on identifying intersecting points, and since there are none, it impairs our ability to accurately calculate distances along the route.

Final Approach :Our project involves simulating a GPS toll system using Python. We began by obtaining the vehicle's start and end coordinates. Using Leaflet, we integrated these coordinates into a map to generate intermediate points along the route. These points were then compiled into a Python dictionary and processed by a Python script. By comparing these coordinates to the predefined toll zone polygons, we could accurately calculate the actual distance traveled by the vehicle.
\newline Now, simulate vehicle movement and toll transactions. You can generate synthetic or real-world-like routes using libraries for graph-based road networks or simply by defining waypoints and paths manually. Each vehicle movement should include details such as vehicle ID, timestamp of entry and exit from toll zones, and potentially GPS coordinates (simulated or real-time).

Vehicle Detection has been implemented using computer vision.Implement data structures to store this information efficiently. Use dictionaries, lists, or pandas DataFrames depending on the complexity and volume of data you're handling. For example, maintain a list of vehicles with their routes and timestamps, and another structure to track toll transactions including vehicle ID, toll zone entered, exit time, and calculated toll fee.Calculate toll fees based on predetermined rules such as vehicle type (e.g., car, truck), distance traveled through toll zones, or fixed rates per entry/exit. This calculation involves checking when a vehicle enters and exits a toll zone, computing the distance traveled if applicable, and applying the appropriate toll fee calculation logic.

Ensure the accuracy of toll collection by validating GPS coordinates against the predefined toll zone boundaries. This step ensures that toll fees are accurately applied only when a vehicle enters a designated toll zone.Finally, visualize the simulated data and toll revenues. Use plotting libraries to create graphs showing traffic patterns, toll transactions over time, and revenues generated. Alternatively, use interactive mapping libraries like Folium to create dynamic maps that illustrate vehicle movements and toll transactions spatially.By simulating the GPS toll collection system in this manner, you can thoroughly test its functionality, efficiency, and accuracy before deploying it in real-world scenarios. This simulation approach allows for iterative improvements and optimizations to ensure smooth operation and effective toll management.

Assumption : In our GPS toll system simulation using Python, we operate under the assumption that real-time GPS data provides accurate location updates, where the endpoint signifies the vehicle's stationary position upon completion of the journey. Users specify both the starting and ending locations, ensuring consistency in the vehicle's route. Our system relies on the reliability of user inputs to facilitate seamless navigation and toll processing.


 The real time data collection is initiated through the code chunck <https://github.com/SreyaJoseph/Terabyte-Titans/blob/main/data_collection.py>
 Data storage is achieved through the following code chunk <https://github.com/SreyaJoseph/Terabyte-Titans/blob/main/data_collection.py>
 User management is being done by the code chunk <https://github.com/SreyaJoseph/Terabyte-Titans/blob/main/data_collection.py>
 Users can access their payment history and this is initiated through the code chunk <https://github.com/SreyaJoseph/Terabyte-Titans/blob/main/data_collection.py>
 
## Results and Findings

Our GPS Toll System Simulation App is a comprehensive solution developed to simulate toll collection using GPS technology. The application leverages the power of Python for backend processing, ensuring efficient and accurate toll calculations based on real-time GPS data.

Front End Development:The front end of our GPS Toll System Simulation App is designed with a focus on simplicity and user experience. HTML and CSS were utilized to create a responsive and visually appealing interface.

Back End Development:The backend is powered by Python, handling the core functionalities such as GPS data processing, toll calculations, and data management.Leaflet provides continuous coordinates and generates maps. Python robust libraries and frameworks ensure the app performs efficiently and accurately under various conditions.

## Team Terabyte Titans

- Sreya Anna Joseph <https://github.com/SreyaJoseph>
- Sethunath A <https://github.com/sethunath2003>
- Marianna Martin <https://github.com/Marianna-Martin>
- Rizia Sara Prabin




 

