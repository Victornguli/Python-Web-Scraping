import requests
import json
from bs4 import BeautifulSoup

try:
	response = requests.get("https://analytics.usa.gov/data/live/realtime.json")
	realtime_info = json.loads(response.text)
	print ("Number of users currently visiting all US government sites {}".format(realtime_info["data"][0]["active_visitors"]))

except requests.exceptions.RequestException as e:
	print (e)

	
