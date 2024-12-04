Project goals: Clearly define the project's objectives - 
Simulating Evacuation Planning: The main goal is to create a simulation that helps identify the closest shelters and evacuation locations to the hurricane's current location to allow faster decision making in disaster management.
Resource Allocation: The project aims to allocate evacuation resources (shelters and evacuation locations) by calculating their distance of those resources to a given location of hurricane.
Managing Disaster: By providing a model for determining which resources to prefer, the system can aid in managing disaster response efforts, ensuring safety and efficiency.

Significance and novelty of the project: Background information and Why the project is meaningful and novel - 
Background Information: Disaster management in response to hurricanes, sometimes requires quick decisions on which shelters and evacuation locations to manage. In real-world scenarios, emergency responders need to quickly assess which facilities are closest to a hurricane's path to evacuate people in a timely manner. This involves real-time distance calculations, data, and a requirement for dynamic decision-making.

Why the Project is Meaningful and Novel: The project provides a basis for simulating evacuation planning using geographic data, which is critical in reducing risk and loss during a natural disaster such as hurricane. Although there are many advanced systems exist for resource allocation in emergencies, but this project provides a novel, lightweight solution by using distance formula (absolute differences in latitude and longitude) to simulate the selection of evacuation points and shelters.
The approach is novel in that it demonstrates how simple algorithms can be used to achieve meaningful outcomes in disaster planning, making the project accessible for real-world applications.


 Installation and usage instructions: Provide clear instructions for installing and using the software.


 Code structure : explanations.
Defining Locations: First it defines the geographic coordinates for the shelters, evacuation points, and the hurricane’s current position.
Then, Distance Calculation: The simple_distance() function calculates the absolute difference in latitude and longitude between the hurricane and each resource (shelter or evacuation point).
Identifying Closest Resources: The find_closest_resources() function calculates and sorts the distances to find the closest two shelters and evacuation points.
Simulating Resource Allocation: The allocate_resources() function outputs the closest shelters and evacuation points with their calculated distances.
Displaying Results: Lastly, it prints the results in a readable format for easy interpretation.

List of functionalities and verification results: Describe the functionalities and present testing results for verification.
Functionalities - 
Distance Calculation:
The program calculates distances between the hurricane's position and each resource using the absolute differences in latitude and longitude.
Sorting and Selecting Closest Resources:
The program finds and displays the two closest shelters and evacuation points by sorting the calculated distances.
Resource Allocation Simulation:
Based on the closest shelters and evacuation points, the program allocates resources in a way that is closest to the hurricane.
Test Case 1: Hurricane at (25.6, -80.0)
Closest Shelters:
Shelter 3: 0.00 (Distance) 
Shelter 1: 4.60 (Distance)
Closest Evacuation Points:
Evacuation Point 3: 0.10 (Distance)
Evacuation Point 2: 0.30 (Distance)

Showcasing the achievement of project goals: Provide some execution results and discuss your result on how your project achieves the project goal - 
Output - 
Simulating Resource Allocation and Evacuation Planning for Hurricane 

Closest Shelters to the Hurricane:
Shelter 3: 0.00 (Simple Distance)
Shelter 4: 7.30 (Simple Distance)

Closest Evacuation Points to the Hurricane:
Evacuation Point 2: 3.50 (Simple Distance)
Evacuation Point 3: 3.60 (Simple Distance)

Achievement of Goals - 
Evacuation Planning: The simulation identifies the closest shelters and evacuation points.
Resource Allocation: It allocates resources based on the closeness of shelters and evacuation points to the hurricane, allowing for efficient disaster management.
Distance Calculation: The simple distance formula allows for easy, basic, and closet calculations.
Managing Disaster: The output clearly helps classify evacuation points and shelters, leads to timely decision-making in disaster management.

 Discussion and Conclusions: Address project issues, limitations, and how your course learning were applied.
Issues and Limitations - 
Distance Formula:
The use of absolute differences in latitude and longitude is an oversimplification. In real-world applications, this would need to be replaced with more accurate geographic distance calculations.
Static Data:
The locations of shelters, evacuation points, and the hurricane are static. Real-time data would increase the model’s applicability for actual hurricane scenarios.
Scalability:
The project can be extended to handle a larger dataset, such as dynamically adding shelters or evacuation points as needed, integrating real-time hurricane tracking, or considering more complex factors like population density.

Conclusion -
This project provides a useful simulation for evacuation planning, demonstrating how basic algorithms can be used to manage disaster response in the context of hurricanes. The simplicity of the system allows for easy implementation and serves as a basis that can be extended for real-world applications. Although there are limitations in terms of distance accuracy, static data, and scalability, but the project is meeting its objectives and provides an advanced and dynamic disaster management tools.
