from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

loc = "London"
start = "January 21st"
end = "January 30th"

def generateHotelDict(location, startDate, endDate):
    google_query = "Hotels in " + location + " from " + startDate + " to " + endDate
    #print("GOOGLE QUERY: " + google_query)
    main_URL = "https://google.com/search?q=" + google_query.replace(" ", "+")
    # print("Final URL: " + main_URL)

    driver = webdriver.Chrome(executable_path = r"/Users/rohitchakravarty/Documents/PersonalProjects/PythonPrograms/TripPlanner/chromedriver")

    driver.get(main_URL)

    data = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div")

    # print(data.text)

    hotelList = data.text.splitlines()
    hotelDict = {}
    for x in range(len(hotelList)):
        if(hotelList[x][0] == "$"):
            hotelDict[hotelList[x+1]] = [hotelList[x], hotelList[x+2]]
    driver.close()

    print("Hotel Locations Complete")
    return hotelDict


#print(generateHotelDict(loc, start, end))
