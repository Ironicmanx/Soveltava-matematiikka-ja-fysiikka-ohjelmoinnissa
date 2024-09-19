
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

lat_mean = df['Latitude'].mean()
long_mean = df['Longitude'].mean()


my_map = folium.Map(location = [lat_mean, long_mean], zoom_start=14)

folium.Polyline(df[['Latitude ()', 'Longitude']], color='blue', opacity = 1 ).add_to(my_map)

my_map.save('map.html')
my_map