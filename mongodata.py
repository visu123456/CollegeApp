from turtle import pen
import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")


myclient = pymongo.MongoClient("mongodb+srv://hdon:hdon123@mycluster.r0zu9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["material"]
mycol = mydb["materials"]


def take_data_from_db():
    # print(list(mycol.myrow.find()))
    return list(mycol.myrow.find())


def give_mongo_data():
    # print(list(mycol.find()))
    return list(mycol.find())

def get_time_table_data():
    tt_db = myclient["timetable"]
    tt_col  = tt_db["timetables"]
    data_ = list(tt_col.find())[0]


    lecture_data = {
        "1":[],
        "2":[],
        "3":[],
        "4":[],
        "5":[],
        "6":[]
    }

    for day_ in ['"monday"','"tuesday"','"wednesday"','"thursday"','"friday"']:
        lecture_data["1"].append(data_[day_][0])
        lecture_data["2"].append(data_[day_][1])
        lecture_data["3"].append(data_[day_][2])
        lecture_data["4"].append(data_[day_][3])
        lecture_data["5"].append(data_[day_][4])
        lecture_data["6"].append(data_[day_][5])
        lecture_data["5"].append(data_[day_][6])
        lecture_data["6"].append(data_[day_][7])

    print(lecture_data)
    return lecture_data

    # return list(tt_col.find())[0]





    
if __name__ == "__main__":
    # give_mongo_data()
    # get_time_table_data()
    pass
