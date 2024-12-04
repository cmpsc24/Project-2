import math 
#locations for shelters and evacuation points (latitude, longitude)
shelters = {
    "Shelter 1": (20.0, -90.5),
    "Shelter 2": (30.5, -90.7),
    "Shelter 3": (25.6, -80.0),
    "Shelter 4": (19.0, -79.3)
}

evacuation_points = {
    "Evacuation Point 1": (29.2, -79.6),
    "Evacuation Point 2": (28.8, -80.3),
    "Evacuation Point 3": (29.1, -80.1),
    "Evacuation Point 4": (27.7, -82.5)
}

# Hurricane's position 
hurricane_position = (25.6, -80.0)  #Current position of the hurricane

# distance calculation using absolute differences in latitude and longitude
def simple_distance(lat1, lon1, lat2, lon2):
    return abs(lat2 - lat1) + abs(lon2 - lon1)

# Find closest shelters and evacuation points to the hurricane
def find_closest_resources(hurricane_position, shelters, evacuation_points):
    shelter_distances = {}
    for shelter, location in shelters.items():
        shelter_distances[shelter] = simple_distance(hurricane_position[0], hurricane_position[1], location[0], location[1])

    evacuation_distances = {}
    for point, location in evacuation_points.items():
        evacuation_distances[point] = simple_distance(hurricane_position[0], hurricane_position[1], location[0], location[1])

    # Sort the dictionaries based on distance and get the closest 2 shelters and evacuation points
    closest_shelters = sorted(shelter_distances.items(), key=lambda x: x[1])[:2]  
    closest_evacuations = sorted(evacuation_distances.items(), key=lambda x: x[1])[:2]  
    return closest_shelters, closest_evacuations

# Simulate resource allocation
def allocate_resources(shelters, evacuation_points, hurricane_position):
    closest_shelters, closest_evacuations = find_closest_resources(hurricane_position, shelters, evacuation_points)
    
    print("Closest Shelters to the Hurricane:")
    for shelter, dist in closest_shelters:
        print(f"{shelter}: {dist:.2f} (Simple Distance)")

    print("\nClosest Evacuation Points to the Hurricane:")
    for point, dist in closest_evacuations:
        print(f"{point}: {dist:.2f} (Simple Distance)")

# To execute the simulation
if __name__ == "__main__":
    print("Simulating Resource Allocation and Evacuation Planning for Hurricane...\n")
    allocate_resources(shelters, evacuation_points, hurricane_position)
