import imdb

  

def create_movie_info():
  f=open("./movies-years.txt", "r")   
  
  sentences = f.readlines()
  ia=imdb.IMDb()
  genres={}
  languages={}
  countries={}
  production_comps={}
  casts={}
  movies_write=open("movie-info.txt",'w')
      
  
  for title in sentences:
    

    try:
      title=title.strip("\n")
      movieID=ia.search_movie(title)[0].movieID
      print "movie title is "+ title
      movie=ia.get_movie(movieID)
      genre=map(str,movie["genres"])
      language=map(str,movie["languages"])
      country=map(str,movie["countries"])    
      production_comp=movie["production companies"]
      cast=map(str,movie["cast"])
      for index in range(0,len(genre)):
        genres[genre[index]]=0
    
      for index in range(0,len(language)):
        languages[language[index]]=0

      for index in range(0,len(country)):
        countries[country[index]]=0
 
      for index in range(0, len(production_comp)):
         production_comps[production_comp[index].companyID]=0

      for index in range(0,len(cast)):
         casts[cast[index]]=0
      movie_dict = {}
      movie_object = movie
      movie_dict["cast"]=[]

      for index in range(0,min(10,len(movie_object["cast"]))):
        movie_dict["cast"].append(str(movie_object["cast"][index]))

      movie_dict["director"]=[]
      for index in range(0,len(movie_object["director"])):
        movie_dict["director"].append(str(movie_object["director"][index]))
      movie_dict["producer"]=[]
      for index in range(0,len(movie_object["producer"])):
        movie_dict["producer"].append(str(movie_object["producer"][index]))

      movie_dict["rating"]=movie_object["rating"]
      movie_dict["year"]=movie_object["year"]
      movie_dict["votes"]=movie_object["votes"]
      movie_dict["countries"]=map(str, movie_object["countries"])
      movie_dict["languages"]=map(str, movie_object["languages"])
      movie_dict["genres"]=map(str, movie_object["genres"])

      movie_dict["production companies"]=[]

      for index in range(0,len(movie_object["production companies"])):
        movie_dict["production companies"].append(str(movie_object["production companies"][index]))
     
      ia.update(movie_object, 'business')
      wgross=movie_object["business"]["gross"][0]
      wgross=wgross.split(' ')[0].strip('$')
      wgross=float(wgross.replace(',',''))
      movie_dict["gross"]=wgross
      bget=movie_object["business"]["budget"][0]
      bget=bget.split(' ')[0].strip('$')
      bget=float(bget.replace(',',''))
      movie_dict["budget"]=bget

      info = title;
      for keys,values in movie_dict.items():
        info = info +"\t" + str(keys)+":"+str(values);
      
      movies_write.write(info+"\n")

    except:
      print "exception: "+title


print "starting..."
create_movie_info()  
