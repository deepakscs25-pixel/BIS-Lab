import random

# Fitness function
def fitness(x):
    return x * x

# Initialize parameters
population_size = 6
mutation_rate = 0.1
generations = 10

# Initialize population
population = [random.randint(0, 31) for i in range(population_size)]

# Print initial population
print("Initial Population:", population)

for g in range(generations):

    print("\nGeneration:", g + 1)

    # Evaluate fitness
    population.sort(key=fitness, reverse=True)

    # Selection
    p1 = population[0]
    p2 = population[1]

    # Convert to binary
    b1 = format(p1, '05b')
    b2 = format(p2, '05b')

    # Crossover
    point = random.randint(1, 4)
    child = b1[:point] + b2[point:]

    # Mutation
    child = list(child)
    for i in range(5):
        if random.random() < mutation_rate:
            child[i] = '1' if child[i] == '0' else '0'

    # Gene expression
    child = int(''.join(child), 2)

    # Replace weakest chromosome
    population[-1] = child

    # Display results
    best = max(population, key=fitness)

    print("Selected Parents:", p1, p2)
    print("New Child:", child)
    print("Best Solution:", best)
    print("Best Fitness:", fitness(best))

# Final output
print("\nFinal Best Solution:", best)
print("Final Best Fitness:", fitness(best))