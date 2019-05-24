from bs4 import BeautifulSoup
import requests

robots = requests.open("https://en.wikipedia.org/robots.txt")

print(robots.text)
