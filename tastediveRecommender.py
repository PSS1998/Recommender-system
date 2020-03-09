import requests
import json

import config


#type = music, movies, shows, podcasts, books, authors, games
def tastedive_recommender(type, name):
	query = name.replace(" ", "+")
	url = f"https://tastedive.com/api/similar?k={config.TASTEDIVE_API}&type={type}&q={query}"
	r = requests.get(url)
	list_items = []
	item_dict = json.loads(r.text)
	for item in item_dict['Similar']['Results']:
		list_items.append(item['Name'])
	return list_items



#print(tastedive_recommender("movies", "Pulp fiction"))
