RUN file predict_movie.py

predict_movie.py  ###  Takes movie name as input, builds the corresponding feature vector, and uses the fitted logistic regression or SVM model to predict the box office success 

createmovie-info.py  ###Reads the names of movies collected from wikipedia and saved in movie_names.txt.  For each movie it collects information from IMDB database and saves in movie-info.txt

createunionfrommovie-info.py  ###Reads the movies from movie-info.txt  and the corresponding information about features to create a list of features comprising names of actors, directors, producers, genres, countries, languages, and production companies. Saves the features in the corresponding file names.Ex: “actor.txt” contains names of all actors who appear as predictors in the model.


createmodel.py ###Builds the logistic regression and linear SVM model after performing cross validation



