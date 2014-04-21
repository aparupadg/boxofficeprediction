import math
import cPickle as pickle


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
  feature.append("rating"+",Metric")
  feature.append("votes"+",Metric")
  
  count=2
  

  dict_lang={}
  for line in language:
    temp=line.strip()
    dict_lang[temp]=count
    feature.append(temp+",Language")
    count=count+1

  dict_prod={}
  for line in producer:
    temp=line.strip()
    feature.append(temp+",Producer")
    dict_prod[temp]=count
    count=count+1

  dict_county={}
  for line in country:
    temp=line.strip()
    feature.append(temp+",Country")
    dict_county[temp]=count
    count=count+1
  

  dict_genres={}
  for line in genre:
    temp=line.strip()
    feature.append(temp+",Genre")
    dict_genres[temp]=count
    count=count+1

  dict_dir={}
  for line in director:
    temp=line.strip()
    feature.append(temp+",Director")
    dict_dir[temp]=count
    count=count+1
  
  dict_actor={}
  for line in actor:
    temp=line.strip()
    feature.append(temp+",Actor")
    dict_actor[temp]=count
    count=count+1

  dict_prodcomp={}
  for line in prod_company:
    temp=line.strip()
    feature.append(temp+",Production_Company")
    dict_prodcomp[temp]=count
    count=count+1
  
  feature.append("year"+",Metric")
  Movie_title=[]
  Movie_budget=[]
  Movie_gross=[]
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
 
  
  total_profit=[0]*N
  total_count=[0]*N
  hits=[0]*N

  for index in range(0,len(sentence)):
      
     movie_vector=[0]*N
     movie=sentence[index]
     movie=movie.split('\t')
     title=movie[0]
     Movie_title.append(str(title))
     budget[title]=float(movie[7].split(":")[1])
     wgross[title]=float(movie[11].split(":")[1])
     Movie_budget.append(str(budget[title]))
     Movie_gross.append(str(wgross[title]))
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
                      
           if total_count[dict_lang[temp]]>0:
               total_profit[dict_lang[temp]]=total_profit[dict_lang[temp]]+(wgross[title]-budget[title])
               total_count[dict_lang[temp]]=total_count[dict_lang[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_lang[temp]]=hits[dict_lang[temp]]+1


           else:
               total_profit[dict_lang[temp]]=(wgross[title]-budget[title])
               if (wgross[title]-budget[title])>0:
                  hits[dict_lang[temp]]=1
               total_count[dict_lang[temp]]=1

     j=j+1
###Producer
     nprod=len(movie[j].split(":")[1].split(","))
    
     for i in range(0,nprod):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in dict_prod.keys():
           movie_vector[dict_prod[temp]]=1
           if total_count[dict_prod[temp]]>0:
               total_profit[dict_prod[temp]]=total_profit[dict_prod[temp]]+(wgross[title]-budget[title])
               total_count[dict_prod[temp]]=total_count[dict_prod[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_prod[temp]]=hits[dict_prod[temp]]+1

           else:
               total_profit[dict_prod[temp]]=(wgross[title]-budget[title])
               total_count[dict_prod[temp]]=1
               if (wgross[title]-budget[title])>0:
                   hits[dict_prod[temp]]=1


     j=j+1

###Countries
     ncount=len(movie[j].split(":")[1].split(","))

     for i in range(0,ncount):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
     
       if temp in dict_county.keys():
           movie_vector[dict_county[temp]]=1
           
           if total_count[dict_county[temp]]>0:
               total_profit[dict_county[temp]]=total_profit[dict_county[temp]]+(wgross[title]-budget[title])
               total_count[dict_county[temp]]=total_count[dict_county[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_county[temp]]=hits[dict_county[temp]]+1


           else:
               total_profit[dict_county[temp]]=(wgross[title]-budget[title])
               total_count[dict_county[temp]]=1
               if (wgross[title]-budget[title])>0:
                  hits[dict_county[temp]]=1


     j=j+1

###Genres
     ngenre=len(movie[j].split(":")[1].split(","))

     for i in range(0,ngenre):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in dict_genres.keys():
           movie_vector[dict_genres[temp]]=1
           
           if total_count[dict_genres[temp]]>0:
               total_profit[dict_genres[temp]]=total_profit[dict_genres[temp]]+(wgross[title]-budget[title])
               total_count[dict_genres[temp]]=total_count[dict_genres[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_genres[temp]]=hits[dict_genres[temp]]+1

           else:
               total_profit[dict_genres[temp]]=(wgross[title]-budget[title])
               total_count[dict_genres[temp]]=1
               if (wgross[title]-budget[title])>0:
                  hits[dict_genres[temp]]=1


     j=j+2


###Director
     ndict=len(movie[j].split(":")[1].split(","))


     for i in range(0,ndict):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in dict_dir.keys():
           movie_vector[dict_dir[temp]]=1
           if total_count[dict_dir[temp]]>0:
               total_profit[dict_dir[temp]]=total_profit[dict_dir[temp]]+(wgross[title]-budget[title])
               total_count[dict_dir[temp]]=total_count[dict_dir[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_dir[temp]]=hits[dict_dir[temp]]+1

           else:
               total_profit[dict_dir[temp]]=(wgross[title]-budget[title])
               total_count[dict_dir[temp]]=1
               if (wgross[title]-budget[title])>0:
                  hits[dict_dir[temp]]=1

     j=j+1

###Cast
     ncast=len(movie[j].split(":")[1].split(","))

     for i in range(0,ncast):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
      
       if temp in dict_actor.keys():
           movie_vector[dict_actor[temp]]=1
           if total_count[dict_actor[temp]]>0:
               total_profit[dict_actor[temp]]=total_profit[dict_actor[temp]]+(wgross[title]-budget[title])
               total_count[dict_actor[temp]]=total_count[dict_actor[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_actor[temp]]=hits[dict_actor[temp]]+1

           else:
               total_profit[dict_actor[temp]]=(wgross[title]-budget[title])
               total_count[dict_actor[temp]]=1
               if (wgross[title]-budget[title])>0:
                  hits[dict_actor[temp]]=1

     j=j+3

###Production Companies
     
     
     npc=len(movie[j].split(":")[1].split(","))

     for i in range(0,npc):
        temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
        if temp in dict_prodcomp.keys():
           movie_vector[dict_prodcomp[temp]]=1
           if total_count[dict_prodcomp[temp]]>0:
               total_profit[dict_prodcomp[temp]]=total_profit[dict_prodcomp[temp]]+(wgross[title]-budget[title])
               total_count[dict_prodcomp[temp]]=total_count[dict_prodcomp[temp]]+1
               if (wgross[title]-budget[title])>0:
                  hits[dict_prodcomp[temp]]=hits[dict_prodcomp[temp]]+1

           else:
               total_profit[dict_prodcomp[temp]]=(wgross[title]-budget[title])
               total_count[dict_prodcomp[temp]]=1
               if (wgross[title]-budget[title])>0:
                  hits[dict_prodcomp[temp]]=1

     j=j-2
###Year
     
     movie_vector[N-1]=int(float(movie[j].split(":")[1]))
     
     X.append(movie_vector)
     
  total=len(Y)
  avg=[0]*N   
  for i in range(0,N-1):
       if total_count[i]>0:
           avg[i]=total_profit[i]/total_count[i]
           hits[i]=(hits[i]*1.0)/total_count[i]
  
###Output Y,X in a file for analysis in R
  fR=open('data.txt','w')
  import copy
  line=copy.deepcopy(feature)
  line.insert(0,"hit")
  line.insert(0,"title")
  line.append("budget")
  line.append("gross")

  for i in range(0,len(line)):
      fR.write(line[i]+"\t")

  
  for i in range(0,len(Y)):
      fR.write("\n")
      fR.write(str(Movie_title[i])+"\t")
      fR.write(str(Y[i])+ "\t")
      
      for j in range(0,len(feature)):
           
          fR.write(str(X[i][j])+"\t")
          fR.write(Movie_budget[i]+"\t")
          fR.write(Movie_gross[i])      

  
  
      
  import numpy as np
  
  from sklearn.svm import LinearSVC
  from sklearn.linear_model import LogisticRegression 
  from sklearn.metrics import roc_auc_score
  
  svm = LogisticRegression(C=0.5, penalty='l1', dual=False, fit_intercept=True)

  #svm = LinearSVC(C=0.15, penalty='l1', loss='l2', dual=False, fit_intercept=True)
  
  
  n_samples = len(X)  
 #Split data into train and test sets
  X_train, y_train = X[:n_samples*4 / 5], Y[:n_samples*4 / 5]
  X_test, y_test = X[n_samples *4/ 5:], Y[n_samples*4 / 5:]

  svm_model = svm.fit(X_train, y_train) 

  print "Percentage accuracy on test data: " +str(svm_model.score(X_test,y_test)*100)
  pickle.dump(svm, open("svm_model", 'wb'))
  ypredict=svm_model.predict(X_test)
  y_score=svm_model.decision_function(X_test)
  print "AUC:" + str(roc_auc_score(y_test, y_score))
  
  #itemindex = np.where(svm_model.coef_!=0)
  #coeff=svm_model.coef_[0].tolist()
  #itemindex=itemindex[1]
    
  #imp_feature={} 
  #for i in range(0,len(itemindex)):
  #    imp_feature[feature[itemindex[i]]]=coeff[itemindex[i]]
  
  #for i in range(0,len(coeff)):
      #imp_feature[feature[i]]=coeff[i]
  #fout = open('feat_rank_svc.csv', 'w')
  #fout = open('feat_rank_logistic.csv', 'w') 
  #for key, value in sorted(imp_feature.iteritems(), key=lambda (k,v): (v,k),reverse=True):
      #fout.write( "%s, %s"  % (key, value)+"\n")
  #for i in range(N):
       #fout.write("%s, %s, %s, %s, %s" % (feature[i],coeff[i],avg[i],hits[i],total_count[i])+"\n")
createmodel()  

