from FinalFlights import genFlightList
from Hotels import generateHotelDict
from Tourist import genTourist
from Geo import nametoLoc
from TSP import mainTSPGE
from flask import Flask, request


app = Flask(__name__)

@app.route("/tripPlan", methods=['POST'])
def returnInfo():
    travelData = request.get_json()
    
    startDate = travelData['StartDate']
    endDate = travelData['EndDate']
    startLoc = travelData['StartLoc']
    endLoc = travelData['EndLoc']
    
    TouristSpots = genTourist(endLoc)
    flightList = genFlightList(startLoc, endLoc, startDate, endDate)
    HotelData = generateHotelDict(endLoc, startDate, endDate)
    
    mainDict = {}
    mainDict['Flights'] = flightList
    mainDict['Hotels'] = HotelData
    mainDict['Tourist Spots'] = TouristSpots
    
    mainDict['Ideal Hotel'] = " "
    mainDict['Ideal Route'] = []
    
    try:
        tourList = []
        hotelList = []
        
        for keys in mainDict['Tourist Spots']:
            tourList.append(keys)
        
        for keys in mainDict['Hotels']:
            hotelList.append(keys)
        
        hotelGeo = nametoLoc(mainDict['Hotels'], endLoc)
        touristGeo = nametoLoc(mainDict['Tourist Spots'], endLoc)

        lookupDict = {}

        #second 0 makes the key the latitude value
        for x in range(len(hotelGeo)):
            lookupDict[hotelGeo[x][0]] = hotelList[x]

        for x in range(len(touristGeo)):
            lookupDict[touristGeo[x][0]] = tourList[x]

        #gets a list of geo-coordinates
        bestPath = mainTSPGE(hotelGeo, touristGeo)
        strLoc = str(lookupDict[bestPath[0][0]])
        
        print("Hotel to stay at: " + strLoc)
        mainDict['Ideal Hotel'] = strLoc
        print("Order to visit places: ")
        for x in range(1, len(bestPath)-1):
            currentLoc = bestPath[x]
            strLoc = str(lookupDict[currentLoc[0]])
            print(strLoc)
            mainDict['Ideal Route'].append(strLoc)
    except:
        print("Error occured while trying to find optimal route")
    
    return str(mainDict)


if __name__ == "__main__":
    app.run(debug=True)


"""
Functions:
        genTourist(City)
        genFlightList(startairport, endairport, startdate, enddate)
        generateHotelDict(location, startdate, enddate)
"""
