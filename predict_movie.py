import math
import cPickle as pickle
import imdb
from sklearn import linear_model
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
ia=imdb.IMDb()

N=0
dict_actor={}
dict_lang={}
dict_prod={}
dict_county={}
dict_genres={}
dict_dir={}
dict_prodcomp={}

#initialize function assigns an index to each feature.  

def initialize():
 
  f_y = open("./movies.txt","r")
  f_actor = open("./actors.txt","r")
  f_dir = open("./directors.txt","r")
  f_prod = open("./producers.txt","r")
  f_genres = open("./genres.txt","r")
  f_county = open("./countries.txt","r")
  f_lang = open("./languages.txt","r")
  f_prodcomp=open("./prodcomps.txt","r")

  actor=f_actor.readlines()
  lenactor=len(actor) 
  director=f_dir.readlines()
  lendirector=len(director)
  producer=f_prod.readlines()
  lenproducer=len(producer)
  genre=f_genres.readlines()
  lengenre=len(genre)
  country=f_county.readlines()
  lencountry=len(country)
  language=f_lang.readlines()
  lenlanguage=len(language)
  prod_company=f_prodcomp.readlines()
  lenprod_company=len(prod_company)  
  y_budget=f_y.readlines()
  lenbudget=len(y_budget)  

## Feature Vector Components    
## Rating | Votes | Languages |Producer | Country | Genres |Directors | Actors | Product_Comp  |Year_of_release (1970-2014)  
  global N
  N=1+1+lenactor+lendirector+lenproducer+lengenre+lencountry+lenlanguage+lenprod_company+1
  
  index=2
  
  for line in language:
    temp=line.strip()
    dict_lang[temp]=index
    index=index+1

 
  for line in producer:
    temp=line.strip()
    dict_prod[temp]=index
    index=index+1

 
  for line in country:
    temp=line.strip()
    dict_county[temp]=index
    index=index+1
  

  for line in genre:
    temp=line.strip()
    dict_genres[temp]=index
    index=index+1

 
  for line in director:
    temp=line.strip()
    dict_dir[temp]=index
    index=index+1

  for line in actor:
    temp=line.strip()
    dict_actor[temp]=index
    index=index+1

 
  for line in prod_company:
    temp=line.strip()
    dict_prodcomp[temp]=index
    

 # index N-1 is for the feature corresponding to "year" 
    
# create function creates the feature vector by taking the title of a movie     
def create(title):    
    
 
  # X is the feature vector corresponding to the movie "title"
  X=[0]*N
  
  try:
      movieID=ia.search_movie(title)[0].movieID 
      movie=ia.get_movie(movieID)
      print "closest match for movie found: " + str(movie)
      year=movie["year"]
      votes=movie["votes"]
      ratings=movie["rating"]
      genre=map(str,movie["genres"])
      language=map(str,movie["languages"])
      country=map(str,movie["countries"])
      production_comp=movie["production companies"]
      actors=movie["cast"]
      directors=movie["director"]
      producers=movie["producer"]

  except:
      print "exception: "+ title + " is not available in IMDb database"
      return(0)

  
  
 
     
  X[0]=float(movie["rating"])
 
  X[1]=float(movie["votes"])
 

###languages
  
  temp=str(movie["languages"][0])

  if temp in dict_lang.keys():
           X[dict_lang[temp]]=1

 

###Producer
  nprod=len(movie["producer"])
   
  for i in range(0,nprod):
       temp=str(movie["producer"][i])
       if temp in dict_prod.keys():
           X[dict_prod[temp]]=1
 

###Countries
  temp=map(str,movie["countries"])
  ncount=len(temp)

  for i in range(0,ncount):
       county=temp[i]
       if county in dict_county.keys():
           X[dict_county[county]]=1
 

###Genres
  temp=map(str,movie["genres"])
  ngenre=len(temp)

  for i in range(0,ngenre):
       tp=temp[i]
       if tp in dict_genres.keys():
           X[dict_genres[tp]]=1
 


###Director
  
  ndict=len(movie["director"])
  for i in range(0,ndict):
       temp=str(movie["director"][i])
       if temp in dict_dir.keys():
           X[dict_dir[temp]]=1
 

###Cast
  ncast=len(movie["cast"])

  for i in range(0,ncast):
       temp=str(movie["cast"][i])
       
       if temp in dict_actor.keys():
           X[dict_actor[temp]]=1
 

###Production Companies
 
     
  npc=len(movie["production companies"])

  for i in range(0,npc):
      temp=str(movie["production companies"][i])
      if temp in dict_prodcomp.keys():
           X[dict_prodcomp[temp]]=1
         
 
###Year
     
  X[N-1]=movie["year"]

 

  return(X) 


## main function takes a movie title from the user and prints the box-office prediction "HIT" or "FLOP" 
def main():
  model = pickle.load(open("svm_model", 'rb'))
  initialize()

  while True:
    user_input = raw_input("Enter movie title for prediction or enter 'quit' to exit:")
    if user_input == "quit":
        break
    X=create(user_input)
    if X==0:
        continue
    ypred = model.predict(X)
  
    if ypred==0:
      print "FLOP"
    elif ypred==1:
      print "HIT"


"starting..."
main()  
