#!/usr/bin/env python3
def main():
    """Ask user for input"""
    uname = input("Please enter your name: ")
    dow = input("Please enter the day of the week: ")
    """Print results"""
    print("Hello, " + uname + "!" + " " + "Happy" + " " + dow + "!")
    print(f"Hello, {uname}! Happy {dow}!")
main()
