from random import randint
import random
import math

class Population:
    def __init__(self, startX, endX, numberOfIndividuals, crossoverRate, mutationRate):
        self.startX = startX
        self.endX = endX
        self.numberOfIndividuals = numberOfIndividuals
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate
        self.individuals = []
        self.fitness = []


    def generateInicialPopulation(self):
        for i in range(self.numberOfIndividuals):
            number = randint(self.startX, self.endX)
            self.individuals.append(self.convertDecimalToBinary(number))
            self.fitness.append(self.calculateFitnessOfOneIndividual(number))


    def crossover(self):
        individualsAfterCrossover = []
        individualsCopy = self.individuals.copy()

        while (len(individualsCopy) > 0):
            probability = randint(0, 100)

            individual1 = random.choice(individualsCopy)
            individualsCopy.remove(individual1)
            individual2 = random.choice(individualsCopy)
            individualsCopy.remove(individual2)

            if (probability < self.crossoverRate):
                tailSize = randint(1, 4)

                tailIndividual1 = individual1[-tailSize:]
                individual1 = individual1[:-tailSize]

                tailIndividual2 = individual2[-tailSize:]
                individual2 = individual2[:-tailSize]

                individual1 += tailIndividual2
                individual2 += tailIndividual1
            
            individualsAfterCrossover.append(individual1)
            individualsAfterCrossover.append(individual2)

        return individualsAfterCrossover


    def mutation(self):
        return self


    def selection(self):
        return self


    def findBest(self, currentBest):
        best = currentBest
        for i in range(self.numberOfIndividuals):
            if (self.fitness[i] > best[0]):
                best = (self.fitness[i], self.individuals[i])
        
        return best


    def printPopulation(self):
        for i in range(self.numberOfIndividuals):
            print(self.convertBinaryToDecimal(self.individuals[i]), "  ", self.individuals[i], "  ", self.fitness[i])


    def calculateFitness(self):
        for i in range(self.numberOfIndividuals):
            number = self.convertBinaryToDecimal(self.individuals[i])
            self.fitness[i] = self.calculateFitnessOfOneIndividual(number)


    def calculateFitnessOfOneIndividual(self, number):
        return (number ** 2) - (3 * number) + 4


    def convertDecimalToBinary(self, decimal):
        binary = bin(decimal)

        if (decimal < 0):
            binary = binary[3:]
            binary = '1' + binary
        else:
            binary = binary[2:]
            binary = '0' + binary

        binaryList = [0] * 5
        binaryList[0] = int(binary[0])
        initialPos = 5 - (len(binary) - 1)
        binaryPos = 1
        for i in range(initialPos, 5):
            binaryList[i] = (int(binary[binaryPos]))
            binaryPos += 1

        return binaryList


    def convertBinaryToDecimal(self, binary):
        signal = binary[0]
        decimal = 0
        binary.pop(0)
        binary.reverse()

        for i in range(4):
            if binary[i] == 1:
                decimal = decimal + (2 ** i)

        if (signal == 1):
            decimal *= -1

        binary.reverse()
        binary.insert(0, signal)

        return decimal
