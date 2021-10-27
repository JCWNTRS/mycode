#!/usr/bin/env python3
print("Welcome to the retro computer guessing game!!")
comp_years = {"85-93":"ST","79-84":"800XL","81-94":"BBC B", "82-84":"Oric","77-93":"Apple II","82-94":"CBM64"}
print("The Timeframes are as follows")
for key in comp_years.keys():
  print(key)
round = 0
machine = " "

while round < 5 and machine not in comp_years:
    round += 1
    years = (input("Pick a timeframe from the list to guess the computer: "))
    if years == "85-93":
        print(f"OK, {years} it is then :)")
        machine = (comp_years.get('85-93'))
        print (machine)
        print ("This is a machine with only 2 letters in its name, made by Atari over the years 85-93")
        #guess = (input("What is your guess? ")
