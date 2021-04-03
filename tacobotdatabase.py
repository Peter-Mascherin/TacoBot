import pymongo

class TacoBotDb:

    databaseclient = pymongo.MongoClient("mongodb+srv://PeterMascherin:tacobot@tacobotcluster.mowbd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = databaseclient.get_database('tacobotdatabase')
    records = db.tacobot_test
    

    def getDocuments(self):
        return self.records.count_documents({})
    
    def addDiscordIdTest(self,discord_id,discord_user):
        result = self.records.insert_one({"discord_id":str(discord_id),"discord_user":str(discord_user)})
        return result
    

