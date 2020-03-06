from getRecommendation import get_recommendation

from collections import Counter


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
	for i in range(len(books)):
		count += 1
		if count%10 == 1:
			print(count)
		book_recom.extend(get_recommendation("book", books[i]))
	print("books done")
	book_recom = [k for k, v in sorted(Counter(book_recom).items(), key=lambda item: item[1], reverse=True)][:10]
	print(book_recom)
	
def get_movie_recommendation():
	movies = get_movies()	
	count = 0
	movie_recom = []
	for i in range(len(movie)):
		count += 1
		if count%10 == 1:
			print(count)
		movie_recom.extend(get_recommendation("movie", movies[i]))
	print("movis done")
	movie_recom = [k for k, v in sorted(Counter(movie_recom).items(), key=lambda item: item[1], reverse=True)][:10]
	print(movie_recom)
	
def get_show_recommendation():
	shows = get_shows()	
	count = 0
	show_recom = []
	for i in range(len(shows)):
		count += 1
		if count%10 == 1:
			print(count)
		show_recom.extend(get_recommendation("show", shows[i]))
	print("shows done")
	show_recom = [k for k, v in sorted(Counter(show_recom).items(), key=lambda item: item[1], reverse=True)][:10]
	print(show_recom)
	
def get_game_recommendation():
	games = get_games()	
	count = 0
	game_recom = []
	for i in range(len(games)):
		count += 1
		if count%10 == 1:
			print(count)
		game_recom.extend(get_recommendation("game", games[i]))
	print("games done")
	game_recom = [k for k, v in sorted(Counter(game_recom).items(), key=lambda item: item[1], reverse=True)][:10]
	print(game_recom)


def get_all_recommendations():
	get_book_recommendation()
	get_movie_recommendation()
	get_show_recommendation()
	get_game_recommendation()
	
get_show_recommendation()
	