import random


def fitness(x):
    return x * x

n = 10
iterations = 50
w = 0.5
c1 = 1.5
c2 = 1.5

position = [random.uniform(-10, 10) for i in range(n)]
velocity = [random.uniform(-1, 1) for i in range(n)]


pbest = position.copy()


gbest = min(pbest, key=fitness)

for i in range(iterations):

    for j in range(n):

  
        if fitness(position[j]) < fitness(pbest[j]):
            pbest[j] = position[j]

        
        if fitness(pbest[j]) < fitness(gbest):
            gbest = pbest[j]

       
        velocity[j] = (w * velocity[j]
                       + c1 * random.random() * (pbest[j] - position[j])
                       + c2 * random.random() * (gbest - position[j]))

        
        position[j] = position[j] + velocity[j]

    
    print("Iteration:", i + 1,
          "Best Position:", gbest,
          "Best Fitness:", fitness(gbest))

print("\nFinal Best Solution:", gbest)
print("Final Best Fitness:", fitness(gbest))