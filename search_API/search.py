import pandas as pd
from datetime import *
import csv

def search(categ):

    data=pd.read_csv('db.csv', header=0, delimiter=",")
    
    data2 = (data[(data.category == categ)])
    data2 = data2.drop(columns=['category', 'quantity', 'price'])
    data2.to_csv('output.csv', index=False)
    return (make_json('output.csv'))


def make_json(csvFilePath):
     
    jsonArray = []
     
    # Open a csv reader called DictReader
    csvf = open(csvFilePath, encoding='utf-8')
    csvReader = csv.DictReader(csvf)

    for row in csvReader:
        jsonArray.append(row)
    
    return jsonArray