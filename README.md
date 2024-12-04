Project goals: Clearly define the project's objectives - 
Simulating Evacuation Planning: The main goal is to create a simulation that helps identify the closest shelters and evacuation locations to the hurricane's current location to allow faster decision making in disaster management.
Resource Allocation Based on Proximity: The project seeks to allocate evacuation resources (shelters and evacuation points) efficiently by calculating the proximity of those resources to a given location, in this case, a hurricane.
Optimizing Disaster Response: By providing a simple model for determining which resources to prioritize, the system can aid in optimizing disaster response efforts, ensuring safety and efficiency.

Significance and novelty of the project: Background information and Why the project is meaningful and novel.
Background Information
Disaster management, especially in response to hurricanes, often requires rapid decisions on which shelters and evacuation points to prioritize. In real-world scenarios, emergency responders need to quickly assess which facilities are closest to a hurricane's path to evacuate people in a timely manner. This involves real-time distance calculations, geographical data, and a need for dynamic decision-making.

Why the Project is Meaningful and Novel
The project provides a foundation for simulating evacuation planning using geographic data, which is crucial in minimizing risk and loss during a natural disaster like a hurricane. Although many advanced systems exist for resource allocation in emergencies, this project offers a novel, lightweight solution by applying simple distance metrics (absolute differences in latitude and longitude) to simulate the selection of evacuation points and shelters.

The approach is novel in that it demonstrates how simple algorithms can be used to achieve meaningful outcomes in disaster planning, making the project both accessible and adaptable for further extensions or real-world applications.



 Installation and usage instructions: Provide clear instructions for installing and using the software.


 Code structure : explanations.
Defining Locations: The script starts by defining the geographic coordinates for the shelters, evacuation points, and the hurricane’s current position.
Distance Calculation: The simple_distance() function calculates the absolute difference in latitude and longitude between the hurricane and each resource (shelter or evacuation point).
Identifying Closest Resources: The find_closest_resources() function calculates and sorts the distances to find the closest two shelters and evacuation points.
Simulating Resource Allocation: The allocate_resources() function outputs the closest shelters and evacuation points with their calculated distances.
Displaying Results: Finally, the script prints the results in a readable format for easy interpretation.

List of functionalities and verification results: Describe the functionalities and present testing results for verification.
Functionalities
Distance Calculation:
The program calculates simple distances between the hurricane's position and each resource using the absolute differences in latitude and longitude.
Sorting and Selecting Closest Resources:
The program finds and displays the two closest shelters and evacuation points by sorting the calculated distances.
Resource Allocation Simulation:
Based on the closest shelters and evacuation points, the program allocates resources in a way that prioritizes proximity to the hurricane.
Test Case 1: Hurricane at (25.6, -80.0)
Closest Shelters:
Shelter 3: 0.00 (Simple Distance) (Exact match, since it’s the hurricane's current position)
Shelter 1: 4.60 (Simple Distance)
Closest Evacuation Points:
Evacuation Point 3: 0.10 (Simple Distance)
Evacuation Point 2: 0.30 (Simple Distance)
Test Case 2: Hurricane at (30.0, -85.0)
Closest Shelters:
Shelter 2: 4.40 (Simple Distance)
Shelter 3: 5.40 (Simple Distance)
Closest Evacuation Points:
Evacuation Point 1: 6.00 (Simple Distance)
Evacuation Point 4: 6.80 (Simple Distance)

 Showcasing the achievement of project goals: Provide some execution results and discuss your result on how your project achieves the project goal
Output - 


Achievement of Goals
Evacuation Planning: The simulation identifies the closest shelters and evacuation points, directly fulfilling the evacuation planning goal.
Resource Allocation: It allocates resources based on the proximity of shelters and evacuation points to the hurricane, allowing for efficient disaster management.
Distance Calculation: The simple distance metric allows for rapid, albeit basic, proximity calculations.
Optimizing Disaster Response: The output clearly helps prioritize evacuation points and shelters, aiding timely decision-making in disaster management.

 Discussion and Conclusions: Address project issues, limitations, and how your course learning were applied.
Issues and Limitations
Simplistic Distance Metric:

The use of absolute differences in latitude and longitude is an oversimplification. In real-world applications, this would need to be replaced with more accurate geographic distance calculations, such as the Haversine formula or geodesic distance, to account for the Earth's curvature.
Static Data:

The locations of shelters, evacuation points, and the hurricane are predefined and static. Real-time data would enhance the model’s applicability for actual hurricane scenarios.
Routing Considerations:

The model does not account for infrastructure or evacuation routes, such as roads, traffic, or transportation capacity, which are critical factors in real-life evacuation scenarios.
Scalability:

The project can be extended to handle a larger dataset, such as dynamically adding shelters or evacuation points as needed, integrating real-time hurricane tracking, or considering more complex factors like population density.

