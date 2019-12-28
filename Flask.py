from FinalFlights import genFlightList
from Hotels import generateHotelDict
from Tourist import genTourist
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
    
    return str(mainDict)


if __name__ == "__main__":
    app.run(debug=True)


"""
Functions:
        genTourist(City)
        genFlightList(startairport, endairport, startdate, enddate)
        generateHotelDict(location, startdate, enddate)
"""
