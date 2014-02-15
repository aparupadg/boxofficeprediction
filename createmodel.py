import math
import cPickle as pickle

## createvector function creates the vectors for the training dataset

def createvector():
  from sklearn import linear_model
  import imdb
  ia=imdb.IMDb()

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
  
## Y is the target variable for the training data set
  Y=[]
##Dictionary for budget by movie names as key
  profit={}
  wgross={}
  budget={}
  for i in range(1,lenbudget):
    title=y_budget[i].strip().split("\t")[1] 
    gross=y_budget[i].strip().split("\t")[4].strip("$")
    bget=y_budget[i].strip().split("\t")[2].strip("$")
    gross=float(gross.replace(',',''))
    bget=float(bget.replace(',',''))
    wgross[title]=gross
    budget[title]=bget
    temp=gross-bget
    if temp>0:
      profit[title]=1
    else:
      profit[title]=0
   
   
    
    
  #Xmovienames={}
  #Xindex=0
  # X is the matrix  of feature vectors of all the training movie titles     
  X=[]
  f = open("movie-info.txt","r")
  sentence=f.readlines()
  no_loss=0
  for index in range(0,len(sentence)):
  
     movie_vector=[0]*N
     movie=sentence[index]
     movie=movie.split('\t')
   
     if (budget[movie[0]]<= 0) or (wgross[movie[0]]<=0):
        continue

     if profit[movie[0]]==0:
       no_loss=no_loss+1

     Y.append(profit[movie[0]])
     #Xmovienames[Xindex] = movie[0]

     j=1  
     
     movie_vector[0]=float(movie[j].split(":")[1])
     j=j+1
     movie_vector[1]=float(movie[j].split(":")[1])
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
     j=j+1


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
     j=j+1

###Production Companies
     j=j+1
     
     npc=len(movie[j].split(":")[1].split(","))

     for i in range(0,npc):
        temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
        if temp in dict_prodcomp.keys():
           movie_vector[dict_prodcomp[temp]]=1
         
     j=j-1
###Year
     
     movie_vector[N-1]=int(float(movie[j].split(":")[1]))
     X.append(movie_vector)
     #Xindex = Xindex+1
  total=len(Y)   
  fr=float(no_loss)/total  
  #print "fraction loss : " + str(fr)
  #print "loss :" + str(no_loss) 
  #print "total :" + str(total)     
  

  import numpy as np
  from sklearn.linear_model import Lasso
  from sklearn.linear_model import LogisticRegression
  from sklearn.svm import LinearSVC
  from sklearn.svm import SVC 
  
  #lasso = Lasso(alpha=0.03, normalize=True, fit_intercept=True, max_iter=100000)
  #svm = LinearSVC(C=0.5, penalty='l2', loss='l2', dual=False, fit_intercept=True)
  svm = LinearSVC(C=0.15, penalty='l1', loss='l2', dual=False, fit_intercept=True)
  #svm = LogisticRegression(C=0.5, penalty='l2', dual=False, fit_intercept=True)
  #svm = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, verbose=False)

  n_samples = len(X)  
  #Split data into train and test sets
  X_train, y_train = X[:n_samples*4 / 5], Y[:n_samples*4 / 5]
  X_test, y_test = X[n_samples *4/ 5:], Y[n_samples*4 / 5:]

  svm_model = svm.fit(X_train, y_train) 
  y_pred_svm = svm_model.predict(X_test)
  y_pred_svm_train = svm_model.predict(X_train)
  pickle.dump(svm, open("svm_model", 'wb'))
   
  numnonzero=0
 
  
"starting..."
createvector()  
