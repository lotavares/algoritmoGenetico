# GA()
#     initialize population
#     find fitness of population
   
#     while (termination criteria is reached) do
#         parent selection
#         crossover with probability pc
#         mutation with probability pm
#         decode and fitness calculation
#         survivor selection
#         find best
#     return best

from population import Population
import math

def geneticAlgorithm(population, numberOfGenerations):
    # (fitness value, binary number)
    best = (-math.inf, [])

    for i in range(numberOfGenerations):
        population.crossover()
        population.mutation()
        population.calculateFitness()
        population.selection()
        best = population.findBest(best)
    
    return best

def main():
    population = Population(-10, 10, 30, 70, 1)
    population.generateInicialPopulation()

    numberOfGenerations = 20
    
    print(geneticAlgorithm(population, numberOfGenerations))

if __name__ == "__main__":
    main()