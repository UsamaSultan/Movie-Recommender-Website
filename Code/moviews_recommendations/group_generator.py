import mysqlx
from collections import defaultdict
import pickle

genre_groups = defaultdict(list)

session = mysqlx.get_session({
    'host': 'localhost',
    'port': 33060,
    'user': 'root',
    'password': 'abcd123'
})

schema = session.get_schema('moviews')

movies = schema.get_table('movie_data')

rows = movies.select('movieId', 'genres').execute().fetch_all()

for row in rows:
    genres = row['genres']
    genre_split = genres.split("|")
    
    for genre in genre_split:
        genre_groups[genre].append(row['movieId'])
        
        
        
pickle.dump( genre_groups, open( "genre_groups.p", "wb" ) )   
print("Done!")
        
        


