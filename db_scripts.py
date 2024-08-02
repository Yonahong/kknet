import csv
import sqlite3

with open("icecreams.csv", "r", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f.readlines())

    ice_creams = [i for i in dict_reader]

for ice_cream in ice_creams:
    ice_cream["image"] = ice_cream["image"] + ".png"


db = sqlite3.connect("db.sqlite3")

cursor = db.cursor()
for ice_cream in ice_creams:
    cursor.execute("INSERT INTO kknet_icecream(id,name,price,mfr,category,img) VALUES(?,?,?,?,?,?)",
                   (ice_cream["id"], ice_cream["name"], ice_cream["price"], ice_cream["mfr"], ice_cream["category"], ice_cream["image"]))
    
db.commit()