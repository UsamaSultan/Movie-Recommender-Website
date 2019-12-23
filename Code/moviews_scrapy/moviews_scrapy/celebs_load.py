import json
import mysqlx


session = mysqlx.get_session({
    'host': 'localhost',
    'port': 33060,
    'user': 'root',
    'password': 'abcd123'
})

schema = session.get_schema('moviews')

celebs = schema.get_table('celebs')





with open('celebs.json') as f:
    data = json.load(f)
    
for d in data:
    path = d['images'][0]['path']
    name = d['name']
    desc = d['desc']
    
    row = celebs.insert('name','images','description').values(name,path,desc).execute()
    
    
    
    
    
    