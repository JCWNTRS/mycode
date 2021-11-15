#!/usr/bin/env python3

#Import required modules
import requests as rq
#Set variables
URL= "http://www.boredapi.com/api/activity/"
#Get number of required activities from the user
num = int(input("How many activities would you like me to suggest?"))
#Confirm number back to user
print(f"Getting you {num} random activities")
#Run loop and grab 'num' + 1 activities, write to screen and write to file.
for n in range(1, num + 1):
    activity = rq.get(URL).json()
    print(activity["activity"])
    with open('/Users/jonathan/Documents/Dev/Python/mycode/myapi/activities.txt','a') as file:
        file.write(activity["activity"] + "\n")
#Tell user the activities have been written to a file. 
print("I've also written them to activities.txt, so you can look at them later")
