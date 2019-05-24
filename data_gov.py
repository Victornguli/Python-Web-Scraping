import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.data.gov/")

try: 
	assert (response.status_code == 200), "Error occured"
except: 
	print ("Could not get the datasets")
else:
	soup = BeautifulSoup(response.text, "html.parser")
	link = soup.find("a", href="/metrics")
	dataset = link.text.split(" ")
	print ("Current number of datasets from data.gov is " + dataset[0] + " Datasets ")
