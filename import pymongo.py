import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb+srv://utermas:Pa260603@cluster0.nkjbc.mongodb.net/testdata?retryWrites=true&w=majority")
json_path = 'J:/Downloads/Загрузки Opera GX/contracts_44fz_202110-20211123.jsonl'
db = client["testdata"]
collection = db["testcoll"]
requesting = []

file = open(json_path, 'r+', encoding='utf-8')


'''with open(r"E:\proekt999\contracts_44fz_202110-20211123.jsonl") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))'''



for jsonObj in file:
    #print(jsonObj)
    myDict = json.loads(jsonObj)
    requesting.append(InsertOne(myDict))


result = collection.bulk_write(requesting)
client.close()