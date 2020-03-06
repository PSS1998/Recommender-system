import requests
import json

import config


#type = music, movies, shows, podcasts, books, authors, games
def tastedive_recommender(type, name):
	query = name.replace(" ", "+")
	url = f"https://tastedive.com/api/similar?k={config.TASTEDIVE_API}&type={type}&q={query}"
	r = requests.get(url)
	list_book = []
	book_dict = json.loads(r.text)
	for book in book_dict['Similar']['Results']:
		list_book.append(book['Name'])
	return list_book



#print(tastedive_recommender("movies", "Pulp fiction"))
