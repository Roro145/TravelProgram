import numpy
import random

#HotelList = [[51.5018592, -0.2126455], [51.4739724, -0.07541099999999999], [51.5098367, -0.3248462], [51.4189637, -0.1987]]
#TouristList = [[51.4998403, -0.1246627], [51.5024625, -0.121064], [40.0428437, -75.38158589999999], [51.5035586, -0.0766852]]

class Point:
    def __init__(self, coords):
        self.X = coords[0]
        self.Y = coords[1]

    def printCoords(self):
        print(self.X)
        print(self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

#Requires: list of potential routes for the tourist to travel
#Modifies: Nothing
#Effects: Returns the list of potential routes without any duplicates
def checkIdenticalSequences(masterList):
    filteredMasterList = []
    for x in range(len(masterList)):
        if(masterList[x] not in filteredMasterList):
            filteredMasterList.append(masterList[x])
    return filteredMasterList

#Requires: A possible sequence and the starting location
#Modifies: Nothing
#Effects: checks whether it's a valid possible sequence - only hotel appears twice
def checkValidity(fullSequence):
    #Checks to start and end at hotel
    if(fullSequence[0] != fullSequence[-1]):
        return False
    #checks to make sure it doesn't visit the hotel during the day
    if(fullSequence[0] in fullSequence[1:-1]):
        return False
    
    #Makes sure there are no repeats
    fullSequence = fullSequence[1:-1]
    newSequence = []
    for seq in fullSequence:
        if seq in newSequence:
            return False
        else:
            newSequence.append(seq)
    return True


#Requires: Two point objects
#Modifies: Nothing
#Effects: returns the distance between two 2-dimensional points
def determineDistance(p1, p2):
    distance = (p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2
    distance = distance ** 0.5
    return distance

#Requires: HotelLoc is a singular Points & TourList is a list of Points
#Modifies: Nothing
#Effects: Calculates the total cost associated with the given path
def calculateFitness(HotelLoc, TourList):
    totalDistance = 0
    #First goes from hotel to first tourist destination
    totalDistance += determineDistance(HotelLoc, TourList[0])
    
    #Travels from the first tourist location to the second, third etc.
    for x in range(len(TourList)-1):
        totalDistance += determineDistance(TourList[x], TourList[x+1])

    #Travels from the last tourist destination back to the hotel
    totalDistance += determineDistance(TourList[-1], HotelLoc)
    return totalDistance

#Requires: TourList is a list of Points
#Modifies: Nothing
#Effects: Returns an array where each element is a possible order
def generatePopulation(TourList, quantity, HotelLoc):
    #Generates X individuals in the population
    currentTour = []
    masterList = []
    for x in range(quantity):
        currentTour = TourList.copy()
        baseList = []
        while(len(currentTour) != 0):
            currentInt = numpy.random.randint(0, len(currentTour))
            baseList.append(currentTour[currentInt])
            del currentTour[currentInt]
        #Ensures that the hotel is the first and last stop
        baseList.append(HotelLoc)
        baseList.insert(0, HotelLoc)
        masterList.append(baseList)

    finalList = checkIdenticalSequences(masterList)
    return finalList

#Requires: Poplist is the population array with each element being a tourist Point
#Modifies: Nothing
#Effects: Returns a list of the two sequences with the lowest fitness
def parentSelection(popList, hotelLoc):
    distanceList = []
    for individualSequence in popList:
        distanceList.append(calculateFitness(hotelLoc, individualSequence))
    # print("Distances: " + str(distanceList))
    #passes through the entire array only once
    currentMin = 100000
    currentSecondMin = 100000
    currentMinIndex = 0
    currentSecondMinIndex = 0
    for x in range(len(distanceList)):
        if distanceList[x] < currentSecondMin:
            if distanceList[x] < currentMin:
                currentMin = distanceList[x]
                currentMinIndex = x
            else:
                currentSecondMin = distanceList[x]
                currentSecondMinIndex = x
    return [popList[currentMinIndex], popList[currentSecondMinIndex]]

#Requires: two parents - the two sequences with the lowest fitness score
#Modifies: Nothing
#Effects: returns a new population set, filtered to remove duplicates
def Breed(parent1, parent2, TourList, hotelLoc):
    newPopulation = []
    #Number of 'children'/new population generated
    for x in range(100000):
        currentSequence = []
        #Starts at 1 since first element is already the hotel, ends before since only
        #require the middle elements of TourList, last element is also hotel
        for x in range(len(TourList)):
            currentChoice = random.random()
            if(currentChoice < 0.45):
                currentSequence.append(parent1[x])
            elif(currentChoice < 0.9):
                currentSequence.append(parent2[x])
            #Inserts a random mutation
            else:
                randInt = random.randrange(1, len(TourList)-1)
                currentSequence.append(TourList[randInt])
        currentSequence.insert(0, hotelLoc)
        currentSequence.append(hotelLoc)
        if(checkValidity(currentSequence)):
            newPopulation.append(currentSequence)
    return checkIdenticalSequences(newPopulation)



def mainTSPGE(HotelList, TouristList):
    #Converts the X-Y coordinates given for each hotel into point objects
    HotelPoints = []
    for x in range (len(HotelList)):
        HotelPoints.append(Point(HotelList[x]))
    #print("X: " + str(HotelPoints[x].getX()) + " Y: " + str(HotelPoints[x].getY()))

    #Converts the X-Y coordinates given for each tourist spot into point objects
    TouristPoints = []
    for x in range (len(TouristList)):
        TouristPoints.append(Point(TouristList[x]))
        #print("X: " + str(TouristPoints[x].getX()) + " Y: " + str(TouristPoints[x].getY()))
    
    BestFitness = 10000

    for x in range(len(HotelPoints)):
        print("Checking hotel Number: " + str(x))
        #generates the first population randomly
        PopulationList = generatePopulation(TouristPoints, 5, HotelPoints[x])

        #Uses the genetic algorithm to determine the best possible sequences
        for x in range(1):
            print("Length of Population List: " + str(len(PopulationList)))
            returnList = parentSelection(PopulationList, HotelPoints[0])
            currentParent1 = returnList[0]
            currentParent2 = returnList[1]
            PopulationList = Breed(currentParent1, currentParent2, TouristPoints, HotelPoints[0])

        print("Length of Population List, Post-Breeding: " + str(len(PopulationList)))
        #Iterates through the best choices & calculates their fitness scores
        fitnessList = []
        for seq in PopulationList:
            fitnessList.append(calculateFitness(HotelPoints[0], seq[1:-1]))

        currentMinFitnessLevel = min(fitnessList)

        if(currentMinFitnessLevel < BestFitness):
            BestFitness = currentMinFitnessLevel
            bestChoice = fitnessList.index(min(fitnessList))
            bestRoute = PopulationList[bestChoice]
            print("New best fitness: " + str(BestFitness))
            print("Best Option: ")
            for points in PopulationList[bestChoice]:
                print("X: " + str(points.getX()) + " Y: " + str(points.getY()))

    print("Final Best Option: ")
    standardArray = []
    for points in bestRoute:
        print("X: " + str(points.getX()) + " Y: " + str(points.getY()))
        standardArray.append([points.getX(), points.getY()])


    return standardArray



#mainTSPGE(HotelList, TouristList)
