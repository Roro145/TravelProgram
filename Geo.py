import requests
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

City = "London"

HotelDict = {'Best Western London Peckham Hotel': ['$53', '3.7'], 'hub by Premier Inn London Westminster Abbey hotel': ['$111', '4.6'], 'Holiday Inn Express London - Ealing': ['$59', '4.5'], 'Citadines Trafalgar Square London (Apart Hotel London)': ['$152', '4.3']}

TourismDict = {'Big Ben': "London's iconic national timepiece", 'Coca-Cola London Eye': 'Iconic riverside observation wheel', 'Tower of London': 'Medieval castle housing the Crown Jewels', 'Tower Bridge': 'Iconic Victorian turreted bridge'}

driver = webdriver.Chrome(executable_path = r"/Users/rohitchakravarty/Documents/PersonalProjects/PythonPrograms/TripPlanner/chromedriver")

#Requires: List of places, the city that they're in & hotel or tourist spot
#Modifies: Nothing
#Effects: Returns the latitude & longitude coordinates of each place
def nametoLoc(nameList, city):
    xPath = "/html/body/div[8]/div[3]/div[10]/div[1]/div[3]/div/div[1]"

    addressList = []
    for place in nameList:
        google_query = place + " " + city
        mainURL = "https://google.com/search?q=" + google_query.replace(" ", "+")
        try:
            driver.get(mainURL)
            data = driver.find_element_by_xpath(xPath)
            addressList.append(returnAddress(data.text))
            print("Located: " + place)
        except:
            print("Unable to locate: " + place)


    geoCoords = []
    for address in addressList:
        currentURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address.replace(" ", "+") + "&key=AIzaSyDARwDR9pYqIDIQrD5yYNtitLkrPQr58wU"
        data = requests.get(currentURL).json()
        coords = data['results'][0]['geometry']['location']
        geoCoords.append([coords['lat'], coords['lng']])
    return geoCoords


#Given the data scraped by xPath, finds the address
def returnAddress(mainStr):
    data1 = mainStr.splitlines()
    for line in data1:
        if("Address" in line):
            #Everything after the "Address: "
            return line[9:]


HotelPlaces = []
for keys in HotelDict:
    HotelPlaces.append(keys)

TourPlaces = []
for keys in TourismDict:
    TourPlaces.append(keys)

HotelCoords = nametoLoc(HotelPlaces, City, "Hotel")
TourismCoords = nametoLoc(TourPlaces, City, "Tourism")
print(HotelCoords)
print(TourismCoords)
driver.close()
