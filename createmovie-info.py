import imdb

def create_dict(movie_object):
  movie_object = movie
  movies_write=open("./movie-info.txt",'w')
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

  info = movie_title;
  for keys,values in movie_dict.items():
    info = info +"\t" + str(keys)+":"+str(values);
  
  movies_write.write(info+"\n")


def union():
  f = open("./movies.txt","r")
  sentences = f.readlines()
  ia=imdb.IMDb()
  genres={}
  languages={}
  countries={}
  production_comps={}
  movies_write=open("movie-info.txt",'w')
  genres_write=open("genres.txt",'w')
  languages_write=open("languages.txt",'w')
  countries_write=open("countries.txt",'w')
  production_comps_write=open("production_comp.txt",'w')
  count=0
  for line in sentences[1:]:
  
    try:
      title=line.split("\t")[1]
      movieID=ia.search_movie(title)[0].movieID
      print "movieID is "+str(movieID)
      movie=ia.get_movie(movieID)
      genre=map(str,movie["genres"])
      language=map(str,movie["languages"])
      country=map(str,movie["countries"])    
      production_comp=movie["production companies"]
      for index in range(0,len(genre)):
        genres[genre[index]]=0
    
      for index in range(0,len(language)):
        languages[language[index]]=0

      for index in range(0,len(country)):
        countries[country[index]]=0
 
      for index in range(0, len(production_comp)):
         production_comps[production_comp[index].companyID]=0

      count=count+1
      print count
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

      info = title;
      for keys,values in movie_dict.items():
        info = info +"\t" + str(keys)+":"+str(values);
      
      movies_write.write(info+"\n")




    except:
      print "exception: "+line

  for keys,values in genres.items():
    genres_write.write(keys+"\n")

  for keys,values in languages.items():
    languages_write.write(keys+"\n") 
  for keys,values in countries.items():
    countries_write.write(keys+"\n")
  for keys,values in production_comps.items():
    production_comps_write.write(str(keys+"\n"))
    


print "starting..."
union()  
