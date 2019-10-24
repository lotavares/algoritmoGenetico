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
from random import randint

def geneticAlgorithm(population, numberOfGenerations):
    # (fitness value, binary number)
    bestSoFar = (-math.inf, [])

    for i in range(numberOfGenerations):
        selecteds = population.parentSelection()
        selecteds = population.crossover(selecteds)
        selecteds = population.mutation(selecteds)
        # selecteds = population.arrangeIntoLimits(selecteds)
        population.repopulation(selecteds)
        population.calculateFitness()

        best = population.findBest(bestSoFar)
        if (best > bestSoFar):
            bestSoFar = best
    
    return best

def main():
    population = Population(-10, 10, 30, 70, 1)
    population.generateInicialPopulation()

    numberOfGenerations = 20

    print(geneticAlgorithm(population, numberOfGenerations))


if __name__ == "__main__":
    main()