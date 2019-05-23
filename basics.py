import requests
from bs4 import BeautifulSoup

quote_page = "https://www.cdnperf.com/"
page = requests.get(quote_page)
soup = BeautifulSoup(page.text, "html.parser")

#name_box = soup.find("ul", attrs={"class" :"dropdown-menu"}).find("li")
#name = name_box
#print (name_box)

print(soup.find_all("ul"))
