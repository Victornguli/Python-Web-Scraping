import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)")

try:
	assert(response.status_code == 200), "Error Bad Request"
except:
	print("Could not fetch images from Peter_Jeffrey wiki page")
else:
	soup = BeautifulSoup(response.text, "html.parser")
	images = soup.find_all("img")
	for i in range(len(images)):
		if i < 1:
			continue
		elif i < 6:
			image_src = "https:"+images[i]["src"]
			print ("Image\t{}\t Saving {} ..... ".format(image_src, str(i)+image_src[-4:]))
			image_name = str(i)+image_src[-4:]
			content = requests.get(image_src)
			file = open(image_name, "wb")
			file.write(content.content)					
			i += 1
			file.close()
		else:
			break
		

