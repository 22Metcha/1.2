#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()
choice = "y"
while choice.lower() == "y":
    print()
    miles_driven = float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))
    print()
    mpg = round(miles_driven / gallons_used, 2)
    tpc = round(cost_per_gallon * gallons_used, 2)
    cpm = round(tpc / miles_driven, 1)
    print("miles per Gallon:\t\t" + str(mpg))
    print("Total Gas Cost:\t\t\t" + str(tpc))
    print("cost per mile:\t\t\t" + str(cpm))
    print()
    choice = input("Get entries for another trip? (y/n): ")

print()
print("Bye")



