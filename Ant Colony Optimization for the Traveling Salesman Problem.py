import random
import math

# Define cities with coordinates
cities = [(0, 0), (1, 5), (5, 2), (6, 6), (8, 3)]
n = len(cities)

# Initialize parameters
ants = 5
iterations = 10
alpha = 1
beta = 2
rho = 0.5
Q = 100

# Calculate distance between cities
distance = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        distance[i][j] = math.dist(cities[i], cities[j])

# Initialize pheromone
pheromone = [[0.1] * n for i in range(n)]

best_route = None
best_distance = float('inf')

print("Cities:", cities)

# ACO algorithm
for iteration in range(iterations):

    routes = []

    # Construct solutions
    for ant in range(ants):

        start = random.randint(0, n - 1)
        route = [start]
        unvisited = list(range(n))
        unvisited.remove(start)

        while unvisited:

            current = route[-1]

            # Calculate probabilities
            weights = [
                (pheromone[current][j] ** alpha) *
                ((1 / distance[current][j]) ** beta)
                for j in unvisited
            ]

            total = sum(weights)
            probabilities = [w / total for w in weights]

            next_city = random.choices(
                unvisited, weights=probabilities
            )[0]

            route.append(next_city)
            unvisited.remove(next_city)

        # Return to starting city
        route.append(start)

        # Calculate total distance
        total_distance = sum(
            distance[route[i]][route[i + 1]]
            for i in range(n)
        )

        routes.append((route, total_distance))

        # Update best solution
        if total_distance < best_distance:
            best_distance = total_distance
            best_route = route.copy()

    # Update pheromones
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - rho)

    for route, dist in routes:
        for i in range(n):
            a = route[i]
            b = route[i + 1]
            pheromone[a][b] += Q / dist
            pheromone[b][a] += Q / dist

    # Display iteration results
    print("\nIteration:", iteration + 1)
    print("Best Route:", best_route)
    print("Shortest Distance:", round(best_distance, 2))

# Final output
print("\nFinal Best Route:", best_route)
print("Final Shortest Distance:", round(best_distance, 2))