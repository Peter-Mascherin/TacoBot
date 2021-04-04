import pymongo
import os

class TacoBotEconomy:

    databaseclient = pymongo.MongoClient("mongodb+srv://PeterMascherin:{0}@tacobotcluster.mowbd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(os.getenv('MONGOPASS')))
    db = databaseclient.get_database('tacobotdatabase')
    economyrecords = db.tacobot_economy

    def createAccount(self,discord_id,discord_name):
        self.economyrecords.insert_one({"discord_id":str(discord_id),"discord_name":str(discord_name),"total_money":1000})
    
    def addAmount(self,discord_id,discord_name,amount):
        print("start fresh today")
        #need to find a way to check if the records were found , and update records (both didnt work wonder why)
    def removeAmount(self):
        print("yo")
    
    def getDocuments(self):
        return self.economyrecords.count_documents({})


    
    
    


        

    

