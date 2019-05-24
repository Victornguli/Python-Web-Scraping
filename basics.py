"""
	Beautiful Soup4 web scraping >> v3ctor
"""

import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names  were </p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, "html.parser") #BeautifulSoup(markuplink, parser=>html parser)

	"""
	Tags
	"""

tag = soup.b #soup.tagname
print(tag) #Prints out `<b>The Dormouse's story</b>`
print(tag.name) #Print out u`b`

#Assign a diffrent tag
tag.name = "blockquote"
print(tag) #<blockquote>The Dormouse's story</blockquote>
tag.name = "b" #Reverse tagname to bold tag


	"""
	Tag Attributes
	"""
print(tag["id"]) #tag["attribute"] eg tag["class"]. This prints none since the bold tag contains no attributes

tag["id"] = "boldest" #assigns b tag a `boldest` id
print (tag.attrs) # {"id": "boldest"}
tag["class"] = "bold-text"
print (tag.attrs) # {"class": "bold-text", "id":"boldest"}

del tag["id"] #deletes id attribute 








print(soup.head.title.text) #Text in the title tag inside head tag
print(soup.find_all("a"))	# Finds all anchor(a) elements

print(len(list(soup.descendants))) #Recursive  count of all children of children of the markup
print(len(list(soup.children))) #Length of all children of the markup

#Explicitly convert list_iterator item generated by soup.children to a list

