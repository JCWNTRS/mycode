#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginall = 0
logingood = 0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        loginall += 1
        #print(loginall)
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1

logingood == loginall -- loginfail
print("The total number of login attempts is", loginall)
print("The number of failed log in attempts is", loginfail)
print("The number of good login attempts is", logingood)
