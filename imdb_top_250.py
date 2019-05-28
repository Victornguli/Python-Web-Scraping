import requests
from bs4 import BeautifulSoup

try:
	response = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")
except requests.exceptions.RequestException as e:
	print(e)

else:
	soup = BeautifulSoup(response.text, "html.parser")
	#movies = soup.find_all("td", class_="titleColumn")
	movies = soup.find_all("td", class_="titleColumn")
	release_date = soup.table.tbody.tr.find("td", class_="titleColumn").span.text
	people = soup.table.tbody.tr.find("td", class_="titleColumn").a["title"]
	for movie in movies:
		movie_name = movie.a.text
		release_date = movie.span.text
		director = movie.a["title"].split(",")[0][:-6]
		actors = " ".join(str(movie.a["title"]).split(",")[1:])
		print("{} released on {} directed by {} acted by {}".format(movie_name,release_date,director,actors,))

	
