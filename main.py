from population import Population
import math

def geneticAlgorithm(population, numberOfGenerations):
    # (fitness value, binary number)
    bestSoFar = (-math.inf, [])

    for i in range(numberOfGenerations):
        selecteds = population.parentSelection()
        selecteds = population.crossover(selecteds)
        selecteds = population.mutation(selecteds)
        population.repopulation(selecteds)
        population.calculateFitness()

        best = population.findBest(bestSoFar)
        if (best > bestSoFar):
            bestSoFar = best
    
    print("Populacao final: ")
    population.printPopulation()

    return best


def main():
    population = Population(-10, 10, 30, 70, 1)

    numberOfGenerations = 20

    population.generateInicialPopulation()

    print("Populacao inicial: ")
    population.printPopulation()

    print("Melhor solucao: ", geneticAlgorithm(population, numberOfGenerations))


if __name__ == "__main__":
    main()