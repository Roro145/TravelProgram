from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

mainCity = "Zurich"

def genTourist(City):
    google_query = "Tourist attractions in " + City
    main_URL = "https://google.com/search?q=" + google_query.replace(" ", "+")

    driver = webdriver.Chrome(executable_path = r"/Users/rohitchakravarty/Documents/PersonalProjects/PythonPrograms/TripPlanner/chromedriver")
    
    driver.get(main_URL)
    
    data = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div")

    dataList = data.text.splitlines()
    dataList = dataList[1:len(dataList)-1]
    dataDict = {}
    for x in range(0, len(dataList), 2):
        dataDict[dataList[x]] = dataList[x+1]
    
    driver.close()

    print("Tourist Locations Complete")
    #print(dataDict)
    return dataDict

#print(genTourist(mainCity))
