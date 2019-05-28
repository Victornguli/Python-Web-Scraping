import requests
from bs4 import BeautifulSoup

try:
	response = requests.get("https://www.imdb.com/chart/top?ref_=nv_mv_250")
except requests.exceptions.RequestException as e:
	print(e)

else:
	soup = BeautifulSoup(response.text, "html.parser")

	movies = soup.find_all("tr")
	fl = open("movies.txt", "w")
	for movie in movies:
		title_info = movie.find("td", {"class":"titleColumn"})
		rating_info = movie.find("td", {"class":"ratingColumn"})
		if title_info is not None and rating_info is not None:
			title = title_info.a.text
			rating = rating_info.strong.text
			release_date = title_info.span.text
			director = title_info.a["title"].split(",")[0][:-6]
			actors = " ".join(str(title_info.a["title"]).split(",")[1:])		

			fl.write("{} rated {} released on {} directed by{} and acted by {} \n\n".format(title,rating,release_date,director, actors))

	fl.close()


		#movie_name = movie.a.text
		#release_date = movie.span.text
		#rating = movies.
		#director = movie.a["title"].split(",")[0][:-6]
		#actors = " ".join(str(movie.a["title"]).split(",")[1:])
		#print("{}\n Release date: {} \tDirector:{} \tActors:{} \n".format(movie_name,release_date,director,actors,))
