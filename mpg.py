#!/usr/bin/env python3

# imports csv
import csv

# checks miles driven for the valid number
def write_trips():
    while True:
        write_trips = float(input("Enter miles driven :     "))                    
        if write_trips > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def write_trips():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def write_trips():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
     print()                           
    mpg = round((miles_driven / gallons_used), 2)
    print("Miles Per Gallon:\t" + str(mpg))
    print()
    write_trips()
    more = input("More entries? (y or n): ")
       
    print("Bye")

if __name__ == "__main__":
   main()

