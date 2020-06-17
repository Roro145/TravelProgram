import requests
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

City = "London"

HotelDict = {'Kensington Suite Hotel':
['$50', '3.0'], 'Best Western London Peckham Hotel': ['$58', '3.7'], 'Holiday Inn Express London - Ealing': ['$59',
                                                                                                         '4.5'], 'Premier Inn London Wimbledon (Broadway) hotel': ['$48', '4.6']}

TourismDict = {'Big Ben': "London's iconic national timepiece", 'Coca-Cola London Eye': 'Iconic riverside observation wheel', 'Tower of London': 'Medieval castle housing the Crown Jewels', 'Tower Bridge': 'Iconic Victorian turreted bridge'}

#Requires: List of places, the city that they're in & hotel or tourist spot
#Modifies: Nothing
#Effects: Returns the latitude & longitude coordinates of each place
def nametoLoc(infoDict, city):
    driver = webdriver.Chrome(executable_path = r"/Users/rohitchakravarty/Documents/PersonalProjects/PythonPrograms/TripPlanner/chromedriver")
    nameList = []
    for keys in infoDict:
        nameList.append(keys)
    
    
    xPath = "/html/body/div[8]/div[3]/div[10]/div[1]/div[3]/div/div[1]"

    addressList = []
    for place in nameList:
        google_query = place + " " + city
        mainURL = "https://google.com/search?q=" + google_query.replace(" ", "+")
        try:
            driver.get(mainURL)
            data = driver.find_element_by_xpath(xPath)
            locAddress = returnAddress(data.text)
            addressList.append(locAddress)
            print("Address Determined: " + place)
        except:
            print("Unable to locate: " + place)


    geoCoords = []
    for address in addressList:
        if address is not None:
            try:
                currentURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address.replace(" ", "+") + "&key=REMOVED_KEY"
                data = requests.get(currentURL).json()
                coords = data['results'][0]['geometry']['location']
                geoCoords.append([coords['lat'], coords['lng']])
                print("Geo Located: " + str(address))
            except:
                print("Failed Geo Locate: " + str(address))
        else:
            print("Address is None")
    
    driver.close()
    return geoCoords


#Given the data scraped by xPath, finds the address
def returnAddress(mainStr):
    data1 = mainStr.splitlines()
    for line in data1:
        if("Address" in line):
            #Everything after the "Address: "
            return line[9:]

