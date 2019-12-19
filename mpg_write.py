#!/user/bin/env python3

# imports csv
import csv
     
# checks miles driven for the valid number
def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :      "))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. please try again.\n")
            continue

def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:   "))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue


def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # rounds mpg
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles per gallon:\t" + str(mpg))
        print()

        # list for
        data_list = [["Distance", "Gallons", "mpg"],
                    [miles_driven, gallons_used, mpg]]
        
        # gets the data from the csv file
        with open("trips.csv", newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                data_list.append(line)
        
        more = input("more entries? (y or n): ")

    print("Bye")

if __name__ == "__main__":
    main()
        

