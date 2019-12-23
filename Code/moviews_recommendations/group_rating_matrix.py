import pickle
from group_rating import group_rating_matrix


user_rating = pickle.load( open( "E:\moviews_recommendations\user_rating_matrix.p", "rb" ) )

grmd = {}

grm = group_rating_matrix()

for user in user_rating:
    ugl = grm.group_ratings(user)
    
    grmd[user] = ugl
    
    
    
pickle.dump( grmd, open( "group_rating_matrix.p", "wb" ) )   
print("Done!")