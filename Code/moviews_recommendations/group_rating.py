import mysqlx
import pickle


class group_rating_matrix:
    
    
    
        
    user_rating = pickle.load( open( "E:\moviews_recommendations\user_rating_matrix.p", "rb" ) )
    genre_groups = pickle.load( open( "E:\moviews_recommendations\genre_groups.p", "rb" ) )
        
        
    def group_ratings(self, userId):

        user_movie_rating = {}
        user_group_rating = {}




      
        values = self.user_rating[userId]
        
        #key = movie id -- value = rating
        for key, value in values.iteritems():
            
            
            user_movie_rating[key] = value[0]




       
         # key = genre -- value = list of movies
        for key, value in self.genre_groups.iteritems():

            sum_rating = 0
            genre_list = value

            user_rated = list(set(user_movie_rating.keys()) & set(genre_list))

            for movie in user_rated:
                sum_rating = sum_rating + user_movie_rating[movie]



            if len(user_rated) != 0:
                avg_rating = sum_rating/len(user_rated)
            else:
                avg_rating=0

            user_group_rating[key] = avg_rating

        
        return user_group_rating
    
