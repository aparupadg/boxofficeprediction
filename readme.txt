There are four .py files:
1) createmovie-info.py reads movies title from movies-years.txt, looks up IMDB using the imdbpy library, and saves the corresponding features for the movie in movie-info.txt
2) createunionfrommovie-info.py reads from the file movie-info.txt and creates the union set of all actors, directors, countries, genres, languages, producers, production company etc. and writes them in .txt files with the corresponding name of the feature
3) createmodel.py reads the training dataset from movie-info.txt and creates the model 
4) predict_movie.py takes the title of the movie from the user creates the corresponding feature vector, uses the model for predicting box-office success

RUN the file predict_movie.py with the name of the movie to obtain the prediction (HIT or FLOP)
