import requests
import json


#type = music, movies, shows, podcasts, books, authors, games
def tastedive_recommender(type, name):
	query = name.replace(" ", "+")
	url = f"https://tastedive.com/api/similar?k=299635-tasterec-LXG98JWS&type={type}&q={query}"
	r = requests.get(url)
	list_items = []
	item_dict = json.loads(r.text)
	for item in item_dict['Similar']['Results']:
		list_items.append(item['Name'])
	return list_items



#print(tastedive_recommender("movies", "Pulp fiction"))
