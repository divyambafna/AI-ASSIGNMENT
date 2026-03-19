graph = {
    "Delhi": {"Jaipur": 281, "Agra": 233, "Chandigarh": 244},
    "Jaipur": {"Delhi": 281, "Ahmedabad": 657, "Udaipur": 394},
    "Agra": {"Delhi": 233, "Lucknow": 335, "Gwalior": 121},
    "Lucknow": {"Agra": 335, "Varanasi": 320},
    "Ahmedabad": {"Jaipur": 657, "Mumbai": 524},
    "Mumbai": {"Ahmedabad": 524, "Pune": 148},
    "Pune": {"Mumbai": 148, "Hyderabad": 560},
    "Hyderabad": {"Pune": 560, "Bangalore": 570},
    "Bangalore": {"Hyderabad": 570, "Chennai": 346},
    "Chennai": {"Bangalore": 346},
    "Chandigarh": {"Delhi": 244},
    "Udaipur": {"Jaipur": 394},
    "Gwalior": {"Agra": 121},
    "Varanasi": {"Lucknow": 320}
}

def dijkstra_algo(graph, start_node):
    distances = {city: float('inf') for city in graph}
    visited_nodes = set()
    distances[start_node] = 0

    while len(visited_nodes) < len(graph):
        current_city = None
        min_distance = float('inf')
        
        for city in graph:
            if city not in visited_nodes and distances[city] < min_distance:
                min_distance = distances[city]
                current_city = city
                
        visited_nodes.add(current_city)
        
        for neighbor, weight in graph[current_city].items():
            new_distance = distances[current_city] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                
    return distances

print("Shortest distances from Pune:")
print(dijkstra_algo(graph, "Pune"))
