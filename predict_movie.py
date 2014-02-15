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
#profit={}
#wgross={}
#budget={}

def initialize():
  #from sklearn import linear_model
 
  #ia=imdb.IMDb()

  f_y = open("/Users/adas/imdbcode/training/movies.txt","r")
  f_actor = open("/Users/adas/imdbcode/unionfeatures/actors.txt","r")
  f_dir = open("/Users/adas/imdbcode/unionfeatures/directors.txt","r")
  f_prod = open("/Users/adas/imdbcode/unionfeatures/producers.txt","r")
  f_genres = open("/Users/adas/imdbcode/unionfeatures/genres.txt","r")
  f_county = open("/Users/adas/imdbcode/unionfeatures/countries.txt","r")
  f_lang = open("/Users/adas/imdbcode/unionfeatures/languages.txt","r")
  f_prodcomp=open("/Users/adas/imdbcode/unionfeatures/prodcomps.txt","r")

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

    
##Actor |Director |Producer |Genres |Country |Language |Product_Comp  |Year_of_release (1970-2014) |Rating |Votes 
  global N
  N=1+1+lenactor+lendirector+lenproducer+lengenre+lencountry+lenlanguage+1 +lenprod_company
  
  count=2
  

  #dict_lang={}
  for line in language:
    temp=line.strip()
    dict_lang[temp]=count
    #feature.append(temp)
    count=count+1

  #dict_prod={}
  for line in producer:
    temp=line.strip()
    #feature.append(temp)
    dict_prod[temp]=count
    count=count+1

  #dict_county={}
  for line in country:
    temp=line.strip()
    #feature.append(temp)
    dict_county[temp]=count
    count=count+1
  

  #dict_genres={}
  for line in genre:
    temp=line.strip()
    #feature.append(temp)
    dict_genres[temp]=count
    count=count+1

  #dict_dir={}
  for line in director:
    temp=line.strip()
    #feature.append(temp)
    dict_dir[temp]=count
    count=count+1

  for line in actor:
    temp=line.strip()
    #feature.append(temp)
    dict_actor[temp]=count
    count=count+1

  #dict_prodcomp={}
  for line in prod_company:
    temp=line.strip()
    #feature.append(temp)
    dict_prodcomp[temp]=count
    count=count+1
  
    
     
def create(title):    
    
 
  Xindex=0   
  X=[]

  movie_vector=[0]*N
  
  try:
      movieID=ia.search_movie(title)[0].movieID
      #print "movieID is "+str(movieID)
      movie=ia.get_movie(movieID)
      print "movie found: " + str(movie)
      year=movie["year"]
      votes=movie["votes"]
      ratings=movie["rating"]
      genre=map(str,movie["genres"])
      #print "genre" + str(genre)
      language=map(str,movie["languages"])
      #print "language" + str(language)
      country=map(str,movie["countries"])
      #print "movie2" + str(movie)
      #print "country" + str(country)
      production_comp=movie["production companies"]
      #print "production_comp" + str(production_comp)
      actors=movie["cast"]
      directors=movie["director"]
      producers=movie["producer"]

  except:
      print "exception: "+ title + " is not available in IMDb database"
      return(0)

  
  
  j=1  
     
  movie_vector[j-1]=float(movie["rating"])
  j=j+1
  movie_vector[j-1]=float(movie["votes"])
  j=j+1

###languages
  #nlan=len(movie["languages"].split(":")[1].split(","))
  #for i in range(0,nlan):
  temp=str(movie["languages"][0])

  if temp in dict_lang.keys():
           movie_vector[dict_lang[temp]]=1

  j=j+1

###Producer
  nprod=len(movie["producer"])
   
  for i in range(0,nprod):
       temp=str(movie["producer"][i])
       if temp in dict_prod.keys():
           movie_vector[dict_prod[temp]]=1
  j=j+1

###Countries
  temp=map(str,movie["countries"])
  ncount=len(temp)

  for i in range(0,ncount):
       county=temp[i]
       if county in dict_county.keys():
           movie_vector[dict_county[county]]=1
  j=j+1

###Genres
  temp=map(str,movie["genres"])
  ngenre=len(temp)

  for i in range(0,ngenre):
       tp=temp[i]
       if tp in dict_genres.keys():
           movie_vector[dict_genres[tp]]=1
  j=j+1


###Director
  
  ndict=len(movie["director"])
  for i in range(0,ndict):
       temp=str(movie["director"][i])
       if temp in dict_dir.keys():
           movie_vector[dict_dir[temp]]=1
  j=j+1

###Cast
  ncast=len(movie["cast"])

  for i in range(0,ncast):
       temp=str(movie["cast"][i])
       
       if temp in dict_actor.keys():
           movie_vector[dict_actor[temp]]=1
  j=j+1

###Production Companies
  j=j+1
     
  npc=len(movie["production companies"])

  for i in range(0,npc):
      temp=str(movie["production companies"][i])
      if temp in dict_prodcomp.keys():
           movie_vector[dict_prodcomp[temp]]=1
         
  j=j-1
###Year
     
  movie_vector[N-1]=movie["year"]

  X=movie_vector

  return(X) 



def main():
  model = pickle.load(open("svm_model", 'rb'))
  initialize()

  while True:
    user_input = raw_input("Enter something:")
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
