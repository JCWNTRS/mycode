#!/usr/bin/env python3
import requests as rq

URL= "http://www.boredapi.com/api/activity/"

howmany = input("How many activities would you like me to suggest?")

num = int(howmany)


print(f"Getting you {num} random activities")

print(num)
for n in range(1, num + 1):
    activity = rq.get(URL).json()
    print(activity["activity"])
    with open('/home/student/mycode/myapi/activities.txt','a') as file:
        file.write(activity["activity"] + "\n")

print("I've also written them to activities.txt, so you can look at them later")
