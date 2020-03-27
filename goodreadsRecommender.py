import requests
from bs4 import BeautifulSoup


def goodreads_recommender(query):
	name = query
	query = name.replace(" ", "+")
	url = f"https://www.goodreads.com/search?query={query}"
	r = requests.get(url).content
	soup = BeautifulSoup(r, 'html.parser')
	book_link = soup.select(".bookTitle")[0]['href']
	book_link = "https://www.goodreads.com"+book_link
	r = requests.get(book_link).content
	soup = BeautifulSoup(r, 'html.parser')
	similar_link = soup.select(".seeMoreLink")[0]['href']
	r = requests.get(similar_link).content
	soup = BeautifulSoup(r, 'html.parser')
	books = soup.select(".gr-d-lg-none+ div .listWithDividers .gr-h3--noMargin span , .gr-boxBottomDivider .gr-h3--noMargin span")
	book_list = []
	count = 0
	for book in books:
		count += 1
		if count%3 == 1:
			book_list.append(book.text)
			
	return book_list
	
	
#print(goodreads_recommender("ninth house"))
