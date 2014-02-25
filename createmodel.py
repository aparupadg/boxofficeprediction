import math
import cPickle as pickle

##createvector function creates the vectors for the training dataset

def createmodel():
  from sklearn import linear_model
  import imdb
  ia=imdb.IMDb()

  f_y = open("./movie-info.txt","r")
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

    
##Actor |Director |Producer |Genres |Country |Language |Product_Comp  |Year_of_release (1970-2014) |Rating |Votes 
  N=1+1+lenactor+lendirector+lenproducer+lengenre+lencountry+lenlanguage+1 +lenprod_company
  feature=[]
  feature.append("rating")
  feature.append("votes")
  dict_actor={}
  count=2
  

  dict_lang={}
  for line in language:
    temp=line.strip()
    dict_lang[temp]=count
    feature.append(temp)
    count=count+1

  dict_prod={}
  for line in producer:
    temp=line.strip()
    feature.append(temp)
    dict_prod[temp]=count
    count=count+1

  dict_county={}
  for line in country:
    temp=line.strip()
    feature.append(temp)
    dict_county[temp]=count
    count=count+1
  

  dict_genres={}
  for line in genre:
    temp=line.strip()
    feature.append(temp)
    dict_genres[temp]=count
    count=count+1

  dict_dir={}
  for line in director:
    temp=line.strip()
    feature.append(temp)
    dict_dir[temp]=count
    count=count+1

  for line in actor:
    temp=line.strip()
    feature.append(temp)
    dict_actor[temp]=count
    count=count+1

  dict_prodcomp={}
  for line in prod_company:
    temp=line.strip()
    feature.append(temp)
    dict_prodcomp[temp]=count
    count=count+1
  
  feature.append("year")
  
##Y is the target variable for the training data set
  Y=[]
##Dictionary for budget by movie names as key
  profit={}
  wgross={}
  budget={}
    
##X is the matrix  of feature vectors of all the training movie titles    
  X=[]
  f = open("movie-info.txt","r")
  sentence=f.readlines()
  no_loss=0
  for index in range(0,len(sentence)):
      
     movie_vector=[0]*N
     movie=sentence[index]
     movie=movie.split('\t')
     title=movie[0]
     budget[title]=float(movie[7].split(":")[1])
     wgross[title]=float(movie[11].split(":")[1])
     if wgross[title]-budget[title]>0:
        profit[title]=1
     else:
        profit[title]=0

     if (budget[movie[0]]<= 0) or (wgross[movie[0]]<=0):
        continue

     if profit[movie[0]]==0:
       no_loss=no_loss+1

     Y.append(profit[movie[0]])
     

     j=1  
     
     movie_vector[j-1]=float(movie[j].split(":")[1])
     j=j+1
     movie_vector[j-1]=float(movie[j].split(":")[1])
     j=j+1
###languages
     nlan=len(movie[j].split(":")[1].split(","))
     
     temp=movie[j].split(":")[1].split(",")[0].strip("[,',] ")
    
     if temp in dict_lang.keys():
           movie_vector[dict_lang[temp]]=1

     j=j+1
###Producer
     nprod=len(movie[j].split(":")[1].split(","))
    
     for i in range(0,nprod):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in dict_prod.keys():
           movie_vector[dict_prod[temp]]=1
     j=j+1

###Countries
     ncount=len(movie[j].split(":")[1].split(","))

     for i in range(0,ncount):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
     
       if temp in dict_county.keys():
           movie_vector[dict_county[temp]]=1
     j=j+1

###Genres
     ngenre=len(movie[j].split(":")[1].split(","))

     for i in range(0,ngenre):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in dict_genres.keys():
           movie_vector[dict_genres[temp]]=1
     j=j+2


###Director
     ndict=len(movie[j].split(":")[1].split(","))


     for i in range(0,ndict):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in dict_dir.keys():
           movie_vector[dict_dir[temp]]=1
     j=j+1

###Cast
     ncast=len(movie[j].split(":")[1].split(","))

     for i in range(0,ncast):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
      
       if temp in dict_actor.keys():
           movie_vector[dict_actor[temp]]=1
     j=j+3

###Production Companies
     
     
     npc=len(movie[j].split(":")[1].split(","))

     for i in range(0,npc):
        temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
        if temp in dict_prodcomp.keys():
           movie_vector[dict_prodcomp[temp]]=1
         
     j=j-2
###Year
     
     movie_vector[N-1]=int(float(movie[j].split(":")[1]))
     X.append(movie_vector)
     #Xindex = Xindex+1
  total=len(Y)   
    

  import numpy as np
  
  from sklearn.svm import LinearSVC
  from sklearn.linear_model import LogisticRegression 
  
# svm = LogisticRegression(C=0.5, penalty='l1', dual=False, fit_intercept=True)

  svm = LinearSVC(C=0.15, penalty='l1', loss='l2', dual=False, fit_intercept=True)
  

  n_samples = len(X)  
  #Split data into train and test sets
  X_train, y_train = X[:n_samples*4 / 5], Y[:n_samples*4 / 5]
  X_test, y_test = X[n_samples *4/ 5:], Y[n_samples*4 / 5:]

  svm_model = svm.fit(X_train, y_train) 
  y_pred_svm = svm_model.predict(X_test)
  y_pred_svm_train = svm_model.predict(X_train)
  incorr_pred=abs(y_pred_svm-y_test)
  frac_corr=1-(sum(incorr_pred)*(1.0)/len(y_test))
  per=frac_corr*100
  print "Percentage accuracy on test data: " +str(per)
  pickle.dump(svm, open("svm_model", 'wb'))
   
  numnonzero=0
 
  
"starting..."
createmodel()  
