import pickle
from scipy import stats
import operator
import mysqlx
import itertools


class Predictor():
    
    
    grm = pickle.load( open( "E:\moviews_recommendations\group_rating_matrix.p", "rb" ) )
    user_rating = pickle.load( open( "E:\moviews_recommendations\user_rating_matrix.p", "rb" ))
                              
    def pearson(self, userId):
        user_sim = {}  
                              
        currentUser = sorted(self.grm[userId].items())
        currentUserValues = [x[1] for x in currentUser]

        for key, value in self.grm.iteritems():

            if key == userId:
                continue
            else:
                st = sorted(value.items())
                st2 = [x[1] for x in st]

                similarity = stats.pearsonr(currentUserValues, st2)[0]

                user_sim[key] = similarity                  
            
        return user_sim


    def predict(self, userId, itemId):

        
        sim_rating_sum = 0
        sim_sum = 0
        


        user_sim = self.pearson(userId)
        
        for key, similarity in user_sim.iteritems():
                              
                
                
                              
                sim_abs = abs(similarity)
                
                

                urm = self.user_rating[key]
                
                

                if itemId in urm:
                    rating = urm[itemId]
                    rs = rating[0]*similarity
                    sim_rating_sum = sim_rating_sum + rs
                    
                    sim_sum = sim_sum + sim_abs
                    

                else:
                    continue


        predicted_rating = sim_rating_sum/sim_sum
        return predicted_rating



    def predictTop(self, userId):
        
        
        cur = self.user_rating[userId]
        curk = cur.keys()
        curs = set(curk)
        urkc = []
        
        user_sim = self.pearson(userId)
        uss = sorted(user_sim.items(), key=operator.itemgetter(1), reverse=True)
        
        for x in uss[:5]:
            ur = self.user_rating[x[0]]
            urk = ur.keys()
            urkc = urkc + urk
        
        urks = set(urkc)
        urks2 = list(curs^urks)
        
        recommendations = urks2
        return  recommendations
    
 
            
            
    


