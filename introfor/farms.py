#!/usr/bin/python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
def farmnames():
    for farm in farms:
         print(farm.get("name"))
#Enumerate farmnames using farmnames function
farmnames()
farmname = input("Pick a Farm: ")
if farmname == "NE Farm".lower:
    print(farmname)
   # print(farmname)
   # else:
   # print("Not a farm")
