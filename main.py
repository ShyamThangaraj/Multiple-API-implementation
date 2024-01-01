import json
import os
import requests
import urllib

def weatherAPI():
  Zip = input("Hey! what is your zip code?(for the weather information!): ")
  my_secret = os.environ['weatherAPIkey']
  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + Zip + ",&appid=" + my_secret
  req = requests.get(url)
  weatherInfo = req.json()
  main=weatherInfo.get("main")
  #Kelvins into Fahrenheit degrees is (K − 273.15) × 9/5 + 32 = °F.
  temp = main["temp"]
  tempf = ((temp) - 273.15) * (9/5) + 32.0
  print("Current temperature: " + str(tempf))

def NameAPI():
  Name = input("Please enter a name here (To predict their nationality!): ")
  urlName = "https://api.nationalize.io/?name=" + Name
  reqs = requests.get(urlName)
  NameInfo = reqs.json()
  results = NameInfo.get("country")
  for data in results:
    print("Country 1: " + data.get("country_id") + ", Probability: " + str(data.get("probability")))

def CountryPublicHolidays ():
  print("Please refer to this link below find your country's abbrevation:")
  print("https://date.nager.at/Home/Countries")
  print("After finding your country's code please enter that data here below")
  Country = input("Please enter the country's abbrevation (to search public holidays): ")
  Year = input("Please enter the year (to search public holidays in that year): ")
  urlCountry = "https://date.nager.at/api/v3/PublicHolidays/" + Year + "/" + Country
  reqsCountry = requests.get(urlCountry)
  CountryInfo = reqsCountry.json()
  for CountryData in CountryInfo:
    resultsCountry = CountryData.get("localName")
    resultsDataCountry = CountryData.get("date")
    print("Holiday: " + resultsCountry + "; Date: " + str(resultsDataCountry))

def Bored():
  print("This will help you coming up with activities to do when you are bored")
  Participants = input("Please enter the number of participants for the activity (1-5): ")
  while int(Participants)<1 or int(Participants)>5:
    print("Oops that's invalid; please enter a number from (1-5)")
    Participants = input("Please enter the number of participants for the activity (1-5): ")
  urlBored = "https://www.boredapi.com/api/activity?participants=" + Participants 
  requestBored = requests.get(urlBored)
  BoredInfo = requestBored.json()
  boredActivity = BoredInfo.get("activity")
  boredActivityType = BoredInfo.get("type")
  print("Activity type: " + boredActivityType + "; Activity: " + boredActivity)

print("Please choose from the follow: ")
print("Input'W' for checking weather")
print("Input'C' for checking specific country's public holidays")
print("Input'N' for predicting a person's nationality based on their name")
print("Input'A' for finding an activity to do (when bored)")
print("Input 'Exit' to exit code!")
while True:
  ChoiceActivity = input("Please enter a code for the activity from the key above: ")
  if ChoiceActivity == "W":
    weatherAPI()
    print("")
  elif ChoiceActivity == "C":
    CountryPublicHolidays()
    print("")
  elif ChoiceActivity == "N":
    NameAPI()
    print("")
  elif ChoiceActivity == "A":
    Bored()
    print("")
  elif ChoiceActivity == "Exit":
    break
  else:
    print("Invalid, please input the correct options")
    print("")