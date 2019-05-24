from bs4 import BeautifulSoup
import requests

#Request and Download robots.txt for wikipedia into robots.txt in your file directory
response = requests.get("https://en.wikipedia.org/robots.tt")

try:
	assert(response.status_code == 200), "Error Occured"

except:
	print("Robots.txt did not donwload")

else:
	robots_text = response.text
	with open("robots.txt" ,"w") as file:
                file.write(robots_text)

