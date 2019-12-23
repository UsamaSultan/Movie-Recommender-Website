import json
import csv

with open('celebs.json') as f:
    data = json.load(f)
    
    
    
for d in data:
    print d