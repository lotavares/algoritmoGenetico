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


    def parentSelection(self):
        selecteds = []

        numberOfSelected = randint(self.numberOfIndividuals / 2, self.numberOfIndividuals)
        if ((numberOfSelected % 2) != 0):
            numberOfSelected += 1

        individualsCopy = self.individuals.copy()
        fitnessCopy = self.fitness.copy()

        while (len(selecteds) < numberOfSelected):
            individualsCopy2 = individualsCopy.copy()
            fitnessCopy2 = fitnessCopy.copy()

            participants = []
            participantsFitness = []
        
            numberOfParticipants = randint(1, len(individualsCopy2))

            for i in range(numberOfParticipants):
                posParticipant = randint(0, len(individualsCopy2) - 1)
                participants.append(individualsCopy2[posParticipant])
                participantsFitness.append(fitnessCopy2[posParticipant])
                individualsCopy2.pop(posParticipant)
                fitnessCopy2.pop(posParticipant)
            
            bestFound = participants[0]
            bestFitnessFound = participantsFitness[0]

            for i in range(numberOfParticipants):
                if (participantsFitness[i] > bestFitnessFound):
                    bestFitnessFound = participantsFitness[i]
            
            selecteds.append(bestFound)

            individualsCopy.remove(bestFound)
            fitnessCopy.remove(bestFitnessFound)

        return selecteds


    def crossover(self, selecteds):
        selectedsAfterCrossover = []

        while (len(selecteds) > 0):
            probability = randint(1, 100)

            individual1 = random.choice(selecteds)
            selecteds.remove(individual1)
            individual2 = random.choice(selecteds)
            selecteds.remove(individual2)

            if (probability <= self.crossoverRate):
                tailSize = randint(1, 4)

                tailIndividual1 = individual1[-tailSize:]
                individual1 = individual1[:-tailSize]

                tailIndividual2 = individual2[-tailSize:]
                individual2 = individual2[:-tailSize]

                individual1 += tailIndividual2
                individual2 += tailIndividual1
            
            selectedsAfterCrossover.append(individual1)
            selectedsAfterCrossover.append(individual2)

        return selectedsAfterCrossover


    def mutation(self, selecteds):
        for i in range(len(selecteds)):
            for j in range(5):
                probability = randint(1, 100)
                if (probability <= self.mutationRate):
                    if (selecteds[i][j] == 1):
                        selecteds[i][j] = 0
                    else:
                        selecteds[i][j] = 1

        self.arrangeIntoLimits(selecteds)
        return selecteds


    def arrangeIntoLimits(self, selecteds):
        for i in range(len(selecteds)):
            number = self.convertBinaryToDecimal(selecteds[i])
            limits = range(self.startX, self.endX)

            if (number not in limits):
                selecteds[i] = self.convertDecimalToBinary(randint(-10, 10))
        
        return selecteds


    def findBest(self, currentBest):
        best = currentBest
        for i in range(self.numberOfIndividuals):
            if (self.fitness[i] > best[0]):
                best = (self.fitness[i], self.individuals[i])
        
        return best


    def printPopulation(self):
        for i in range(self.numberOfIndividuals):
            print(self.convertBinaryToDecimal(self.individuals[i]), "  ", self.individuals[i], "  ", self.fitness[i])


    def repopulation(self, selecteds):
        self.individuals.clear()

        self.individuals = selecteds

        for i in range(len(selecteds), self.numberOfIndividuals):
            number = randint(self.startX, self.endX)
            self.individuals.append(self.convertDecimalToBinary(number))


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
