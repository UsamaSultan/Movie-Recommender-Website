import pandas

movies = pandas.read_csv("movies.csv")

genres = movies.genres

genre_list = []

for genre in genres:
    
    genre_split = genre.split("|")
    
    for genre2 in genre_split:
        
        genre_list.append(genre2)
    


genre_set = set(genre_list)
genre_set.remove("(no genres listed)")

with open('genres.txt', 'w') as f:
    for item in genre_set:
        f.write("%s\n" % item)

                   