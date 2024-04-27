#Karina Washington
#Module 4 CRUD
# April 5, 2024

from pymongo import MongoClient
class CRUD(object): 
    def __init__(self):
        #intialize MongoDB connection 
        self.client = MongoClient('mongodb://aacuser:SNHU1234@nv-desktop-services.aporto.com:31580')
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
    def create(self, data):
        #method to insert a documento into a specefied MongoDB database and collection
        try:
            result = self.collection.insert_one(data)
            return True if result.acknowledged else False
        except Exception as e:
            print(f"An error occurred while inserting docuemnt: {e}")
            return False
    def read(self, query):
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print(f"An error occurred while reading documents: {e}")
            return []
        
    def update(self, query, new_values):
        #mehtod to query for and update in a specefied MongoDB databese and collection
        try:
            result = self.collection.update.many(query,new_values)
            return result.modified_count
        except Exception as e:
            print(f"An error occurred while updating docuemnts: {e}")
            return 0
    def delete (self, query):
        # Method to query for and delete documents MONGODB database & collection
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred while deelting documents: {e}")
            return 0 
            
            
    #example usage:    
    #crud = CRUD()
    #data.to.insert={"name":"Max","breed" : "Labrador", "age" : 3}
    #crud.create(data_to_insert)
    #results = crud.read(read_query)
    #print(results)