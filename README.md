# Recommender System
This program will scrape your movie from letterboxd.com, your tv shows from tvtime.com, your books from goodreads.com and your games from myvideogamelist.com and write the to files.<br />
if you dont have account in those sites you can add your list manually to the text file.<br />
then it can give you recommendation on all those files with running get_all_recommendations() function in get_all_recommendation.py file.<br />
additionaly you can get recommendation on a single movie, tv show, book or game with running get_recommendation function in getRecommendation.py file<br />
For a simple API, WebApp and App based on this projects, visit https://github.com/PSS1998/Recommender-API repository.<br />

## Recommendation system
the Recommender System for books will give you recommendation based on goodreads site similar recommendation, tastedive site and "goodbooks-10k" dataset.<br />
for movies will give recommendation based on tastedvie and "The Movies Dataset" dataset and for tv shows and games will only give recommendation based on tastedive.<br />

## how to run
first you need to download the following datasets:<br />
https://www.kaggle.com/rounakbanik/the-movies-dataset<br />
https://www.kaggle.com/zygmunt/goodbooks-10k<br />
then you needd to change config.py.sample to config.py and fill in the variables<br />
after that you have to run the for files named *-scraper.py<br />
and then call get_all_recommendations() function in get_all_recommendation.py file.<br />

