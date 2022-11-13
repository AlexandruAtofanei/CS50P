import re
import sys


def main():
    # Print converted input
    print(convert(input("Hours: ")))

def convert(s):
    # Define a dictionary with time conversion
    conversion_table = {
        "12:00 AM" : "00:00", "1:00 AM" : "01:00", "2:00 AM" : "02:00", "3:00 AM" : "03:00",
        "4:00 AM" : "04:00", "5:00 AM" : "05:00", "6:00 AM" : "06:00", "7:00 AM" : "07:00",
        "8:00 AM" : "08:00", "9:00 AM" : "09:00", "10:00 AM" : "10:00", "11:00 AM" : "11:00",
        "12:00 PM" : "12:00", "1:00 PM" : "13:00", "2:00 PM" : "14:00", "3:00 PM" : "15:00",
        "4:00 PM" : "16:00", "5:00 PM" : "17:00", "6:00 PM" : "18:00", "7:00 PM" : "19:00",
        "8:00 PM" : "20:00", "9:00 PM" : "21:00", "10:00 PM" : "22:00", "11:00 PM" : "23:00",
         "12:00 AM" : "00:00" }
    # Serach the input for the provided time format
    if matches := re.search(r"^(1?[0-9])(\:?[0-5]?[0-9]?)( AM| PM)( to )(1?[0-9])(\:?[0-5]?[0-9]?)( AM| PM)", s):
        # Define a list where to store all elements from .groups()
        time = []
        # Loop through the groups and store elements in list
        for t in matches.groups():
            # Condition: depending on the format add ':00' if not imputed
            if t == "":
                time.append(":00")
            else:
                time.append(t)
        # Define variables x, y to use in conversion_table
        x = (time[0] + ":00" + time[2])
        y = (time[4] + ":00" + time[6])
        t = (conversion_table[x]).split(":")
        u = (conversion_table[y]).split(":")
        # Return the conversed value
        return (t[0]+ time[1] + time[3] + u[0] + time[5])
    else:
        sys.exit(ValueError)


if __name__ == "__main__":
    main()
