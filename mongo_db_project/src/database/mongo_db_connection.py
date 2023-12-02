from pymongo import MongoClient, ReadPreference
from src.database.properties import MONGO_DB_ATLAS_CONNECTION_STRING

class MongoDBConnection:
    def __init__(self):
        connection_string = MONGO_DB_ATLAS_CONNECTION_STRING
        database_name = "student_points_database"
        try:
            self.__connection = MongoClient(connection_string)
            self.__database = self.__connection[database_name]
        except Exception as e:
            print("***FALHA AO SE CONECTAR AO BANCO DE DADOS***")


    def get_collection(self, collection_name):
        try:
            return self.__database[collection_name]
        except Exception as e:
            print("[Error to connect database]\n" + e)