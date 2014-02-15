import math

def createvector():
  
  actors={}
  directors={}
  producers={}
  genres={}
  countries={}
  languages={}
  countries={}
  companies={}
  f_actor = open("/Users/adas/imdbcode/unionfeatures/actors.txt","w")
  f_dir = open("/Users/adas/imdbcode/unionfeatures/directors.txt","w")
  f_prod = open("/Users/adas/imdbcode/unionfeatures/producers.txt","w")
  f_genres = open("/Users/adas/imdbcode/unionfeatures/genres.txt","w")
  f_county = open("/Users/adas/imdbcode/unionfeatures/countries.txt","w")
  f_lang = open("/Users/adas/imdbcode/unionfeatures/languages.txt","w")
  f_comp = open("/Users/adas/imdbcode/unionfeatures/prodcomps.txt","w")

  f = open("/Users/adas/imdbcode/imdbpy/movie-info.txt","r")
  sentence=f.readlines()

  for index in range(0,len(sentence)):
     movie=sentence[index]
     movie=movie.split('\t')
     j=3
###languages
     nlan=len(movie[j].split(":")[1].split(","))
     temp=movie[j].split(":")[1].split(",")[0].strip("[,',] ")
     #print "lang= " + str(temp)
     if temp in languages.keys():
           languages[temp] = languages[temp] + 1
     else:
           languages[temp] = 1

     j = j+1
###Producer
     nprod=len(movie[j].split(":")[1].split(","))
     for i in range(0,nprod):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',],']")
       if temp in producers.keys():
           producers[temp] = producers[temp] + 1
       else:
           producers[temp] = 1

     j = j+1
###Countries
     ncount=len(movie[j].split(":")[1].split(","))

     for i in range(0,ncount):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in countries.keys():
           countries[temp] = countries[temp] + 1
       else:
           countries[temp] = 1

     j = j+1
###Genres
     ngenre=len(movie[j].split(":")[1].split(","))

     for i in range(0,ngenre):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in genres.keys():
           genres[temp] = genres[temp] + 1
       else:
           genres[temp] = 1


     j = j+1
###Director
     ndict=len(movie[j].split(":")[1].split(","))

     for i in range(0,ndict):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       if temp in directors.keys():
           directors[temp] = directors[temp] + 1
       else:
           directors[temp] = 1

     j = j+1
###Cast
     ncast=len(movie[j].split(":")[1].split(","))

     for i in range(0,ncast):
       temp=movie[j].split(":")[1].split(",")[i].strip("[,',] ")
       
       if temp in actors.keys():
           actors[temp] = actors[temp] + 1
       else:
           actors[temp] = 1

     j = j+2
###Production Companies
     #npc=len(movie[j].split(":")[1].split(","))

     #for i in range(0,npc):
     #  temp=movie[j].split(":")[1].split(",")[i].strip("[,',]")
     temp=movie[j].split(":")[1].split(",")[0].strip("[,',]")
     temp=temp.replace("']\n",'')
   
     if temp in companies.keys():
           companies[temp] = companies[temp] + 1
     else:
           companies[temp] = 1
     
  for i in actors.keys():
     if (actors[i] > 5):
         f_actor.write(i+"\n")
  for i in producers.keys():
     if (producers[i] > 3):
         f_prod.write(i+"\n")
  for i in directors.keys():
     if (directors[i] > 3):
         f_dir.write(i+"\n")
  for i in genres.keys():
     if (genres[i] > 3):
         f_genres.write(i+"\n")
  for i in countries.keys():
     if (countries[i] > 5):
         f_county.write(i+"\n")
  for i in languages.keys():
     if (languages[i] > 5):
         f_lang.write(i+"\n")
  for i in companies.keys():
     if (companies[i] > 5):
         f_comp.write(i+"\n")

print "starting..."
createvector()  
