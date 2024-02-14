import requests
from datetime import datetime
import json
from bs4 import BeautifulSoup
from lxml import html
                
def get_weather(enlem, boylam):
	bugun = datetime.now().strftime("%Y-%02m-%02d")
	response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{enlem}%2C{boylam}/{bugun}/{bugun}?unitGroup=metric&include=current&key=YRFBF5BURG5ELTAAXVRPAPANR&contentType=json")

	if response.status_code==200:
		soup = BeautifulSoup(response.text, "html.parser")
		root = html.fromstring(str(soup))

		jsonData = response.json()
		print(jsonData)

	else:
		print(f"Hata: {response.status_code}")

	# Parse the results as JSON
			
get_weather(40.4321, 29.434321)