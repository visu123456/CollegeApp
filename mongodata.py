import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")


myclient = pymongo.MongoClient("mongodb+srv://hdon:hdon123@mycluster.r0zu9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["material"]
mycol = mydb["materials"]
def give_mongo_data():
    



    print(list(mycol.find()))

    return list(mycol.find())

    
if __name__ == "__main__":
    give_mongo_data()