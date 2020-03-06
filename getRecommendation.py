from goodreadsRecommender import goodreads_recommender
from tastediveRecommender import tastedive_recommender


#type = book, movie, show, game
#for book start all words capital
def get_recommendation(type, name):
	recommendations = []
	if type == "book":
		from goodreadsContentBasedBookRecommendation import corpus_recommendations
		try:
			recommendations.extend(goodreads_recommender(name))
		except Exception: 
			pass
		try:
			recommendations.extend(tastedive_recommender("books", name))
		except Exception: 
			pass
		try:
			recommendations.extend(corpus_recommendations(name))
		except Exception: 
			pass
	elif type == "movie":
		from movieRecommenderSystems import hybrid_recommender
		try:
			recommendations.extend(tastedive_recommender("movies", name))
		except Exception: 
			pass
		try:
			recommendations.extend(hybrid_recommender(name))
		except Exception: 
			pass
	elif type == "show":
		try:
			recommendations.extend(tastedive_recommender("shows", name))
		except Exception: 
			pass
	elif type == "game":
		try:
			recommendations.extend(tastedive_recommender("games", name))
		except Exception: 
			pass
	return recommendations


#print(get_recommendation("movie", "Taken"))