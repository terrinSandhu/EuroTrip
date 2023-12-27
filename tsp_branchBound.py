import itertools
import random

# Define cities
cities = ["London", "Paris", "Barcelona", "Madrid", "Lisbon"]

# Generate probable travel costs (e.g., based on distance)
travel_costs = {}
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            # Assuming cost is some function of distance (e.g., 100 to 900)
            travel_costs[(city1, city2)] = random.randint(100, 900)

# Generate probable hotel costs per night for each city (e.g., 50 to 300)
hotel_costs = {city: random.randint(50, 300) for city in cities}

# Branch and Bound Algorithm Implementation
def tsp_branch_and_bound(cities, travel_costs, hotel_costs):
    best_route = None
    best_cost = float('inf')

    # Initial bound (e.g., using some heuristic like the minimum spanning tree cost, etc.)
    initial_bound = 0  # Replace with an actual initial bound calculation

    # Define a recursive function to explore each branch
    def visit_city(visited, current_city, current_cost, current_route):
        nonlocal best_route, best_cost

        # Base case: if all cities are visited, return to the starting city
        if len(visited) == len(cities):
            return_to_start_cost = travel_costs[(current_city, current_route[0])]
            total_cost = current_cost + return_to_start_cost
            if total_cost < best_cost:
                best_cost = total_cost
                best_route = current_route + [current_route[0]]
            return

        # Recursive case: visit the next city
        for next_city in cities:
            if next_city not in visited:
                next_cost = current_cost + travel_costs[(current_city, next_city)] + hotel_costs[next_city]
                if next_cost < best_cost:  # Bound
                    visit_city(visited | {next_city}, next_city, next_cost, current_route + [next_city])

    # Start the recursion from each city
    for start_city in cities:
        visit_city({start_city}, start_city, hotel_costs[start_city], [start_city])

    return best_route, best_cost

# Solve the TSP with Branch and Bound
best_route, best_cost = tsp_branch_and_bound(cities, travel_costs, hotel_costs)

print("Best route:", best_route)
print("Best cost:", best_cost)
