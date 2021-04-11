# Project for finding similar movies based on cosine similarities


An interacive solution to fetch similar movies based on cosine similarities. The implementation does not use any database. Instead fetches all the data through API calls. For fetching
the movie details such as posters, cast & crew details, genre and reviews through making api calls to https://www.themoviedb.org in realtime.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, , and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using `beautifulsoup4` and performed sentiment analysis on those reviews.


Movie database sources:
1. Kaggle
2. wikiedia
3. https://www.themoviedb.org
