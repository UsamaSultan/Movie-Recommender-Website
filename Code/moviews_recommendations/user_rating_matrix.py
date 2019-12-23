import mysqlx
from collections import defaultdict
import pickle


    
user_rating = defaultdict(dict)

session = mysqlx.get_session({
    'host': 'localhost',
    'port': 33060,
    'user': 'root',
    'password': 'abcd123'
})


schema = session.get_schema('moviews')

ratings = schema.get_table('user_ratings')

rows = ratings.select('userId', 'rating', 'movieId').execute().fetch_all()



for row in rows:

    uid = row['userId']
    movie_id = row['movieId']
    rating = row['rating']

    user_rating[uid][movie_id] = rating




pickle.dump( user_rating, open( "user_rating_matrix.p", "wb" ) )   
print("Done!")    



    


