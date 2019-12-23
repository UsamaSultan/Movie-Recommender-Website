import pandas
import cPickle as pickle
from collections import defaultdict

chunksize = 10

user_movie_matrix = defaultdict(dict)



for chunk in pandas.read_csv('ratings.csv', chunksize=chunksize):
    
    for row in chunk.itertuples():
        user_id = row[0]
        movie_id = row[1]
        rating = row[2]
        
        print(user_id, movie_id, rating)
        
        user_movie_matrix[user_id][movie_id] = rating
        
      
pickle.dump( user_movie_matrix, open( "user_movie_matrix.p", "wb" ) )    
print("All Done!");    
