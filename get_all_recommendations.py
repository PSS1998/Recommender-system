from getRecommendation import get_recommendation

from collections import Counter
from collections import defaultdict


def get_books():
	with open('books.txt') as f:
		books = f.read().splitlines()
	for i, book in enumerate(books):
		temp = book.split("(")
		if(len(temp) > 1):
			books[i] = temp[0][:-1]
	return books

def get_movies():
	with open('movies.txt') as f:
		movies = f.read().splitlines()
	for i, movie in enumerate(movies):
		temp = movie.split("(")
		if(len(temp) > 1):
			movies[i] = temp[0][:-1]
	return movies

def get_shows():
	with open('tvshows.txt') as f:
		shows = f.read().splitlines()
	for i, show in enumerate(shows):
		temp = show.split("(")
		if(len(temp) > 1):
			shows[i] = temp[0][:-1]
	return shows

def get_games():
	with open('games.txt') as f:
		games = f.read().splitlines()
	for i, game in enumerate(games):
		temp = game.split("(")
		if(len(temp) > 1):
			games[i] = temp[0][:-1]
	return games
	
def get_book_recommendation():
	books = get_books()	
	count = 0
	book_recom = []
	book_recom_based = defaultdict()
	for i in range(len(books)):
		count += 1
		if count%10 == 1:
			print(count)
		else:
			print(count)
		recommendations = get_recommendation("book", books[i])
		book_recom.extend(recommendations)
		book_recom_based[books[i]] = recommendations
	print("books done")
	book_recom = [x for x in book_recom if x not in books]
	book_recom_part2 = []
	for i in range(len(book_recom)):
		temp = book_recom[i].split("(")
		if len(temp) > 1:
			book_recom[i] = temp[0][:-1]
			book_recom_part2.append([temp[0][:-1], temp[1]])
	book_recom = [{k:v} for k, v in sorted(Counter(book_recom).items(), key=lambda item: item[1], reverse=True)]
	for i in range(len(book_recom)):
		for j in range(len(book_recom_part2)):
			for key in book_recom[i]:
				if key == book_recom_part2[j][0]:
					book_recom[i][key+" ("+book_recom_part2[i][1]] = book_recom[i].pop(key)
	recom_based = []
	for i in range(len(book_recom)):
		temp = []
		for k,v in book_recom_based.items():
			for key in book_recom[i]:
				if key in v:
					temp.append(k)
		recom_based.append(temp)
	for i in range(len(book_recom)):
		book_recom[i].update({'similar':recom_based[i]})
	with open('book_recommmendation.txt', 'w') as f:
		for item in book_recom:
			f.write("%s\n" % item)
	
def get_movie_recommendation():
	movies = get_movies()	
	count = 0
	movie_recom = []
	movie_recom_based = defaultdict()
	for i in range(len(movies)):
		count += 1
		if count%10 == 1:
			print(count)
		recommendations = get_recommendation("movie", movies[i])
		movie_recom.extend(recommendations)
		movie_recom_based[movies[i]] = recommendations
	print("movis done")
	movie_recom = [x for x in movie_recom if x not in movies]
	movie_recom_part2 = []
	for i in range(len(movie_recom)):
		temp = movie_recom[i].split("(")
		if len(temp) > 1:
			movie_recom[i] = temp[0][:-1]
			movie_recom_part2.append([temp[0][:-1], temp[1]])
	movie_recom = [{k:v} for k, v in sorted(Counter(movie_recom).items(), key=lambda item: item[1], reverse=True)]
	for i in range(len(movie_recom)):
		for j in range(len(movie_recom_part2)):
			for key in movie_recom[i]:
				if key == movie_recom_part2[j][0]:
					movie_recom[i][key+" ("+movie_recom_part2[i][1]] = show_recom[i].pop(key)
	recom_based = []
	for i in range(len(movie_recom)):
		temp = []
		for k,v in movie_recom_based.items():
			for key in movie_recom[i]:
				if key in v:
					temp.append(k)
		recom_based.append(temp)
	for i in range(len(movie_recom)):
		movie_recom[i].update({'similar':recom_based[i]})
	with open('movie_recommmendation.txt', 'w') as f:
		for item in movie_recom:
			f.write("%s\n" % item)
	
def get_show_recommendation():
	shows = get_shows()	
	count = 0
	show_recom = []
	show_recom_based = defaultdict()
	for i in range(len(shows)):
		count += 1
		if count%10 == 1:
			print(count)
		recommendations = get_recommendation("show", shows[i])
		show_recom.extend(recommendations)
		show_recom_based[shows[i]] = recommendations
	print("shows done")
	show_recom = [x for x in show_recom if x not in shows]
	show_recom_part2 = []
	for i in range(len(show_recom)):
		temp = show_recom[i].split("(")
		if len(temp) > 1:
			show_recom[i] = temp[0][:-1]
			show_recom_part2.append([temp[0][:-1], temp[1]])
	show_recom = [{k:v} for k, v in sorted(Counter(show_recom).items(), key=lambda item: item[1], reverse=True)]
	for i in range(len(show_recom)):
		for j in range(len(show_recom_part2)):
			for key in show_recom[i]:
				if key == show_recom_part2[j][0]:
					show_recom[i][key+" ("+show_recom_part2[i][1]] = show_recom[i].pop(key)
	recom_based = []
	for i in range(len(show_recom)):
		temp = []
		for k,v in show_recom_based.items():
			for key in show_recom[i]:
				if key in v:
					temp.append(k)
		recom_based.append(temp)
	for i in range(len(show_recom)):
		show_recom[i].update({'similar':recom_based[i]})
	with open('show_recommmendation.txt', 'w') as f:
		for item in show_recom:
			f.write("%s\n" % item)
	
def get_game_recommendation():
	games = get_games()	
	count = 0
	game_recom = []
	game_recom_based = defaultdict()
	for i in range(len(games)):
		count += 1
		if count%10 == 1:
			print(count)
		recommendations = get_recommendation("game", games[i])
		game_recom.extend(recommendations)
		game_recom_based[games[i]] = recommendations
	print("games done")
	game_recom = [x for x in game_recom if x not in games]
	game_recom_part2 = []
	for i in range(len(game_recom)):
		temp = game_recom[i].split("(")
		if len(temp) > 1:
			game_recom[i] = temp[0][:-1]
			game_recom_part2.append([temp[0][:-1], temp[1]])
	game_recom = [{k:v} for k, v in sorted(Counter(game_recom).items(), key=lambda item: item[1], reverse=True)]
	for i in range(len(game_recom)):
		for j in range(len(game_recom_part2)):
			for key in game_recom[i]:
				if key == game_recom_part2[j][0]:
					game_recom[i][key+" ("+game_recom_part2[i][1]] = game_recom[i].pop(key)
	recom_based = []
	for i in range(len(game_recom)):
		temp = []
		for k,v in game_recom_based.items():
			for key in game_recom[i]:
				if key in v:
					temp.append(k)
		recom_based.append(temp)
	for i in range(len(game_recom)):
		game_recom[i].update({'similar':recom_based[i]})
	with open('game_recommmendation.txt', 'w', encoding="utf-8") as f:
		for item in game_recom:
			f.write("%s\n" % item)


def get_all_recommendations():
	get_game_recommendation()
	get_show_recommendation()
	get_movie_recommendation()
	get_book_recommendation()
	
	
	
get_all_recommendations()
	