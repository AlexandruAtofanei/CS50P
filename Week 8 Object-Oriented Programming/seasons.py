from datetime import date, datetime
import sys
import inflect


class Birthdate:
    def __init__(self, birthdate=0):
        self.birthdate = self.get(birthdate)
        self._today = self.today()
        self.td = self.time_delta()

    # Define a method that gets the users input
    def get(self, user_input):
        if user_input == 0 :
            user_input = input("What`s your birthdate? ")
        # Define exceptions
        try:
            # Check if input is of format YYYY-MM-DD
            if user_input := datetime.strptime(user_input, "%Y-%m-%d"):
                # Return a new input with time set at midnight
                user_input = datetime.combine(user_input, datetime.min.time())
                return user_input
        except ValueError:
            sys.exit("Time should be of format year-month-day! ")

    # Define a method that returns todays date with time set at midnight
    def today(self):
        return datetime.combine(date.today(), datetime.min.time())

    # Define a method that returns the delta in minutes
    def time_delta(self):
        # Check if birthdate is not in the future
        if self.birthdate < self._today:
            delta = self._today - self.birthdate
            td = delta.days * (24 * 60)
            return td
        else:
            sys.exit("You can`t be borne in the future! ")

    # Method that returns the time delta as a str
    def __str__(self):
       return f"{self.td}"


def main():
    # Print the minutes passed since birth till today in words.
    print (number_to_words(Birthdate()))

# Define function that uses inflect to transform minutes in to words.
def number_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(str(minutes), andword='')
    return f"{words} minutes".capitalize()


if __name__ == "__main__":
    main()
