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
    best = (-math.inf, [])

    for i in range(numberOfGenerations):
        population.individuals = population.crossover()
        break
        population.mutation()
        population.calculateFitness()
        population.selection()
        best = population.findBest(best)
    
    return best

def main():
    population = Population(-10, 10, 30, 70, 1)
    population.generateInicialPopulation()

    numberOfGenerations = 20

    population.printPopulation()

    print(geneticAlgorithm(population, numberOfGenerations))

    population.printPopulation()

    # individual1 = [1, 2, 3, 4, 5]
    # individual2 = [6, 7, 8, 9, 10]

    # tailSize = randint(1, 4)

    # tailIndividual1 = individual1[-tailSize:]
    # individual1 = individual1[:-tailSize]

    # tailIndividual2 = individual2[-tailSize:]
    # individual2 = individual2[:-tailSize]

    # print(individual1)
    # print(tailIndividual1)
    # print(individual2)
    # print(tailIndividual2)

    # individual1 += tailIndividual1
    # print(individual1)


if __name__ == "__main__":
    main()