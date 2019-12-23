import pandas

chunksize = 10000000


for chunk in pandas.read_csv('ratings.csv', chunksize=chunksize):
    
    index = chunk.loc[chunk['userId'] == 1]
    print index

