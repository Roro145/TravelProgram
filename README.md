# Travel Program

General Program Flow:
- User Sends POST request with travel data to the flask server
- Script scrapes flight data during that time, then looks at tourist attractions and hotels in the area
- Uses the name of hotels & tourist attractions to webscrape the address, uses google maps API to get geo-coordinates
- Uses the geo-coordinates of hotels & attractions to determine the best hotel to stay at to visit all the attractions and travel the shortest distance (traveling salesman problem), utilizes a genetic algorithm
- Converts coordinates back to the names of places and presents the information as the name of the place ex: stay at Hotel Name, then visit Attraction1, attraction2, atraction3
- Returns all the information that it gathered about flights (airline & ticket price) and  hotels (price & rating)

Sample Program Run:

Concise Input/output:

input:
{
"StartDate": "January 21st",
"EndDate"  : "January 30th",
"StartLoc" : "Detroit",
"EndLoc"   : "Paris"
}


Output:
{'Flights': {'Multiple airlines 7h 57m+ Connecting': '$789+', 'Turkish Airlines 21h 35m+ Connecting': '$842+', 'Air
France 7h 57m Nonstop': '$1,098+', 'Delta 7h 57m Nonstop': '$1,098+', 'Multiple airlines 7h 57m Nonstop': '$1,098+',
'Other airlines 9h 25m+ Connecting': '$909+', 'Save $120 – Connecting flights from $669 if you fly from Windsor (YQG)':
'h flights+'}, 
'Hotels': {'Grand Hôtel Clichy Paris': ['$97', '4.0'], 'Hôtel A La Villa Des Artistes': ['$109', '4.3'],
'Paris France Hôtel': ['$114', '4.2'], 'Novotel Tour Eiffel Hotel': ['$147', '4.0']}, 
'Tourist Spots': {'Eiffel Tower': 'Landmark 324m-high 19th-century tower', 'Louvre Museum': 'Landmark art museum with vast collection', 'Cathédrale Notre-Dame de Paris': 'Iconic Gothic church with literary link', 'Arc de Triomphe': 'Triumphal arch & national monument'},
'Ideal Hotel': 'Grand Hôtel Clichy Paris', 
'Ideal Route': ['Louvre Museum', 'Eiffel Tower', 'Cathédrale Notre-Dame de Paris']}


Detailed Example:

Input:
//POST request to /tripPlan

{
"StartDate": "January 21st",
"EndDate"  : "January 30th",
"StartLoc" : "Detroit",
"EndLoc"   : "London"
}

Output:
Tourist Locations Complete
Plane Info Complete
Hotel Locations Complete
Address Determined: Holiday Inn Express London - Ealing
Address Determined: Best Western London Peckham Hotel
Address Determined: hub by Premier Inn London Westminster Abbey hotel
Address Determined: Imperial Court Studios
Geo Located: 75 Broadway, Ealing, London W13 9BP, United Kingdom
Geo Located: 110 Peckham Rd, Peckham, London SE15 5EU, United Kingdom
Geo Located: 21 Tothill St, Westminster, London SW1H 9LL, United Kingdom
Geo Located: 77-79 Inverness Terrace, Bayswater, London W2 3JT, United Kingdom
Address Determined: Big Ben
Address Determined: Coca-Cola London Eye
Address Determined: Tower of London
Address Determined: Tower Bridge
Geo Located: Westminster, London SW1A 0AA, United Kingdom
Geo Located: Lambeth, London SE1 7PB, United Kingdom
Geo Located: St Katharine's & Wapping, London EC3N 4AB, United Kingdom
Geo Located: Tower Bridge Rd, London SE1 2UP, United Kingdom
Checking hotel Number: 0
Length of Population List: 5
Length of Population List, Post-Breeding: 2
New best fitness: 152.3480920790701
Best Option: 
X: 51.5098367 Y: -0.3248462
X: 51.5024625 Y: -0.121064
X: 51.5035586 Y: -0.0766852
X: 51.4998403 Y: -0.1246627
X: 40.0428437 Y: -75.38158589999999
X: 51.5098367 Y: -0.3248462
Checking hotel Number: 1
Length of Population List: 5
Length of Population List, Post-Breeding: 8
New best fitness: 0.5308919307766435
Best Option: 
X: 51.5098367 Y: -0.3248462
X: 51.4739724 Y: -0.07541099999999999
X: 51.5035586 Y: -0.0766852
X: 51.5024625 Y: -0.121064
X: 51.4998403 Y: -0.1246627
X: 51.5098367 Y: -0.3248462
Checking hotel Number: 2
Length of Population List: 5
Length of Population List, Post-Breeding: 16
New best fitness: 0.49689704773845234
Best Option: 
X: 51.5098367 Y: -0.3248462
X: 51.4995031 Y: -0.1315233
X: 51.4998403 Y: -0.1246627
X: 51.5035586 Y: -0.0766852
X: 51.5024625 Y: -0.121064
X: 51.5098367 Y: -0.3248462
Checking hotel Number: 3
Length of Population List: 5
Length of Population List, Post-Breeding: 8
Final Best Option: 
X: 51.5098367 Y: -0.3248462
X: 51.4995031 Y: -0.1315233
X: 51.4998403 Y: -0.1246627
X: 51.5035586 Y: -0.0766852
X: 51.5024625 Y: -0.121064
X: 51.5098367 Y: -0.3248462

Hotel to stay at: Holiday Inn Express London - Ealing

Order to visit places: 
Tower of London
Big Ben
Coca-Cola London Eye
Tower Bridge

Data returned:
{'Flights': {'Multiple airlines 7h 25m+ Connecting': '$720+', 'Turkish Airlines 21h 35m+ Connecting': '$785+', 'Air
France 7h 25m Nonstop': '$899+', 'Delta 7h 25m Nonstop': '$899+', 'KLM 7h 25m Nonstop': '$899+', 'Virgin Atlantic 7h 25m Nonstop': '$899+', 'Multiple airlines 7h 25m Nonstop': '$899+', 'Other airlines 7h 25m+ Connecting': '$888+', 'Save $206 – Connecting flights from $514 if you fly from Windsor (YQG)': 'h flights+'}, 

'Hotels': {'Best Western London Peckham Hotel': ['$58', '3.7'], 'hub by Premier Inn London Westminster Abbey hotel': ['$110', '4.6'], 'Holiday Inn Express London - Ealing': ['$62', '4.5'], 'Kensington Suite Hotel': ['$46', '3.0']}, 

'Tourist Spots': {'Big Ben': "London's iconic national timepiece", 'Coca-Cola London Eye': 'Iconic riverside observation wheel', 'Tower of London': 'Medieval castle housing the Crown Jewels', 'Tower Bridge': 'Iconic Victorian turreted bridge'}, 

'Ideal Hotel': 'Best Western London Peckham Hotel', 

'Ideal Route': ['Tower of London', 'Big Ben', 'Coca-Cola London Eye', 'Tower Bridge']}
