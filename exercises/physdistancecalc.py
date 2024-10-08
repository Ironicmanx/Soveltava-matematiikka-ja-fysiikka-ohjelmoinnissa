
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import math

# Path to the CSV file
path = '/home/arttu/Python files/FALL2024 | MATH AND PHYSICS/Soveltava-matematiikka-ja-fysiikka-ohjelmoinnissa/Location GPS 2024-09-22 20-48-12/Raw Data.csv'

# Read the data
df = pd.read_csv(path)

# Clean up column names
df.columns = df.columns.str.strip().str.replace('"', '')

# Print the column names to verify
print("Column names:", df.columns)

# Check the data types of the DataFrame
print("Data types:\n", df.dtypes)

# Convert 'Time (s)' to numeric directly (assuming it's in correct format)
#df['Time (s)'] = pd.to_numeric(df['Time (s)'].str.replace(',', '.'), errors='coerce')

# Ensure latitude and longitude are numeric (you may want to keep these just in case)
df['Latitude (°)'] = pd.to_numeric(df['Latitude (°)'], errors='coerce')
df['Longitude (°)'] = pd.to_numeric(df['Longitude (°)'], errors='coerce')

# Calculate mean latitude and longitude
lat_mean = df['Latitude (°)'].mean()
long_mean = df['Longitude (°)'].mean()

# Create a Folium map centered at the mean latitude and longitude
my_map = folium.Map(location=[lat_mean, long_mean], zoom_start=14)

# Add a polyline to the map using the latitude and longitude columns
folium.PolyLine(df[['Latitude (°)', 'Longitude (°)']].values.tolist(), color='blue', opacity=1).add_to(my_map)

# Save the map as an HTML file
my_map.save('map.html')

# Check if 'Signal' column exists, if not create a dummy column
if 'Signal' not in df.columns:
    df['Signal'] = np.random.uniform(low=0, high=10, size=len(df))  # Dummy signal values

# Plot the signal vs time
plt.plot(df['Time (s)'], df['Signal'])
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.title('Signal vs Time (s)')
plt.show()

# Define Haversine formula to calculate the distance between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r  # Result in kilometers

# Calculate total distance traveled
total_distance = 0
df['dist'] = np.zeros(len(df))  # Initialize distance column

for i in range(len(df) - 1):
    distance = haversine(df.at[i, 'Latitude (°)'], df.at[i, 'Longitude (°)'],
                         df.at[i + 1, 'Latitude (°)'], df.at[i + 1, 'Longitude (°)'])
    df.at[i, 'dist'] = distance
    total_distance += distance

# Print the total distance traveled
print(f'Total distance traveled: {total_distance:.2f} km')

import webbrowser
webbrowser.open('map.html')