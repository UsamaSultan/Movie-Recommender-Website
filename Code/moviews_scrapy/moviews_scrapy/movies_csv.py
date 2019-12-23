import json
import csv

with open('movies.json') as f:
    data = json.load(f)
    
    
f = csv.writer(open("movies.csv", "wb+"))


for x in data:
    f.writerow([
    
        
                x["movie_id"],
                x["description"],
                x["writers"],
                x["stars"],
                x["director"],
                x["runtime"],
                x["images"]
               
               
               
               
               
               ])
    

        
    