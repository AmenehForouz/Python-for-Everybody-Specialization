# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly
# using try except

hrs = input("Enter Hours:")
rph = input('Enter rate per hour: ')
try:
    h = float(hrs)
    r = float(rph)
    if h <= 40:
        print(h * r)
    else:
        print((40 * r) + ((h-40)*1.5*r))
except:
    print('either hours or rate per hour is not number, enter again')