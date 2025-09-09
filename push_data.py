import os
import sys
import logging
import pymongo
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import json
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,file_path): #This function converts a CSV file into a list of JSON records (dictionaries).
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = data.to_dict(orient="records")
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def insert_data_mongodb(self,records,database,collections):
        try:
            self.records = records
            self.database = database
            self.collections = collections

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collections = self.database[self.collections]
            self.collections.insert_many(self.records)

            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__=="__main__":
    File_path = "Network_Data\phisingData.csv"
    database = "phisingData"
    collections = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(file_path=File_path)
    no_of_records = networkobj.insert_data_mongodb(records,database,collections)
    print(no_of_records)