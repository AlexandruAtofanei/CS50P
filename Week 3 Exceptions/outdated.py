def main():

    # Define provided list of months
    list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    # Loop to promp the user for the correct input
    while True:
        try:
            date = input("Give me the date in mounth, day, year order! ")
            # Check the format of the input, remove spaces and separate month, day, year through 3 variables
            if "/" in date:
                month, day, year = date.strip().split("/")
                # Check if input respects month and day limits
                if int(month) <= 12 and int(day) <= 31:
                    return print(year, month.zfill(2), day.zfill(2), sep=("-"))
            # For the second format, split first by space the month from year and day and then split the day and year by ',' removing spaces if any
            else:
                month2, dy = date.split(" ", maxsplit=1)
                day2, year2 = dy.split(",")
                month2 = month2.strip()
                day2 = day2.strip()
                year2 = year2.strip()
                # Check if input respects month and day limits
                if int(day2) <= 31 and month2 in list:
                    month2 = str((list.index(month2) + 1))
                    return print(year2, month2.zfill(2), day2.zfill(2), sep=("-"))
        # Repromp user if any of the above conditions are not met
        except ValueError:
            pass

main()
