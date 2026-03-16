#haversine.py formula calculates distance
#From https://gist.github.com/rochacbruno/2883505?permalink_comment_id=2615334
import math

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0 

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference in coordinates
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate distance
    distance = R * c
    return distance

# Define the coordinates (in degrees)
#lat1, lon1 = 40.7128, -74.0060  # New York City
#lat2, lon2 = 34.0522, -118.2437 # Los Angeles
lat1,lon1 = -26.757766, 153.12497
lat2, lon2 = -26.757768, 153.12499


distance = haversine(lat1, lon1, lat2, lon2)
print(f"Distance: {distance:.10f} km")
