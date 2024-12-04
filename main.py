import math 
# Step 1: Define locations for shelters and evacuation points (latitude, longitude)
shelters = {
    "Shelter 1": (25.0, -80.5),
    "Shelter 2": (25.5, -80.7),
    "Shelter 3": (26.0, -81.0),
    "Shelter 4": (26.5, -81.3)
}

evacuation_points = {
    "Evacuation Point 1": (25.2, -80.6),
    "Evacuation Point 2": (25.8, -80.8),
    "Evacuation Point 3": (26.2, -81.1),
    "Evacuation Point 4": (26.6, -81.4)
}

# Step 2: Hurricane's position (simulating movement over time)
hurricane_position = (25.4, -80.9)  # Current position of the hurricane

# Step 3: Simple distance calculation using absolute differences in latitude and longitude
def simple_distance(lat1, lon1, lat2, lon2):
    return abs(lat2 - lat1) + abs(lon2 - lon1)

# Step 4: Find closest shelters and evacuation points to the hurricane
def find_closest_resources(hurricane_position, shelters, evacuation_points):
    shelter_distances = {}
    for shelter, location in shelters.items():
        shelter_distances[shelter] = simple_distance(hurricane_position[0], hurricane_position[1], location[0], location[1])

    evacuation_distances = {}
    for point, location in evacuation_points.items():
        evacuation_distances[point] = simple_distance(hurricane_position[0], hurricane_position[1], location[0], location[1])

    # Sort the dictionaries based on distance and get the closest 2 shelters and evacuation points
    closest_shelters = sorted(shelter_distances.items(), key=lambda x: x[1])[:2]  # Top 2 closest shelters
    closest_evacuations = sorted(evacuation_distances.items(), key=lambda x: x[1])[:2]  # Top 2 closest evacuation points

    return closest_shelters, closest_evacuations

# Step 5: Simulate resource allocation
def allocate_resources(shelters, evacuation_points, hurricane_position):
    closest_shelters, closest_evacuations = find_closest_resources(hurricane_position, shelters, evacuation_points)
    
    print("Closest Shelters to the Hurricane:")
    for shelter, dist in closest_shelters:
        print(f"{shelter}: {dist:.2f} (Simple Distance)")

    print("\nClosest Evacuation Points to the Hurricane:")
    for point, dist in closest_evacuations:
        print(f"{point}: {dist:.2f} (Simple Distance)")

# Step 6: Main function to execute the simulation
if __name__ == "__main__":
    print("Simulating Resource Allocation and Evacuation Planning for Hurricane...\n")
    allocate_resources(shelters, evacuation_points, hurricane_position)
