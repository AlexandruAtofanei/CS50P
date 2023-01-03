import re
import sys
import csv
from datetime import datetime, timedelta


def main():

    while True:
        menu()
        option = input("What do you wanna do next? ").strip()
        match option:
            case "0":
                sys.exit("\nThank you for using this program. Goodbye!")
            case "1":
                while True:
                    try:
                        username = input(
                            "Please enter your username: ").strip()
                        password = input(
                            "Please enter your password: ").strip()
                        print(gate(authenticate(username, password)))
                        break
                    except ValueError:
                        print("\nInvalid username or paswword. Try again!\n")
            case "2":
                register()
            case "3":
                user = input("Please provide your username: ").strip()
                plate = input(
                    "Please provide your license plate number: ").strip().lower()
                print(recover(user, plate))
            case _:
                print(f"\n{option} is not a valid menu option, try again! \n")


def menu():
    """
    Returns a menu.

    :return: A string containing a menu
    :rtype: str
    """
    print(
        "[1] Authenticate",
        "[2] Register a new account",
        "[3] Recover password",
        "[0] Exit the program",
        sep="\n")


def authenticate(username, password):
    """
    Check username and password in csv and authenticate user.

    :return: Users username after succesful authentication
    :rtype: str
    """
    usernames = []
    passwords = []
    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            usernames.append(row["username"])
            passwords.append(row["password"])
    if username in usernames and password in passwords:
        return username
    else:
        raise ValueError


def gate(user):
    """
    Check in database if a gate is free and asign a user to it.

    :param user: Validated username from users input
    :type user: str
    :return: A string with the available free gate
    :rtype: str
    """
    now = datetime.now().isoformat(" ", timespec="seconds")
    now = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    time_stamps = []
    gates = []
    usernames = []
    truck_unload_time = 4
    with open("gates.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            time_stamps.append(datetime.strptime(
                (row["timestamp"]), "%Y-%m-%d %H:%M:%S"))
            gates.append(row["gate"])
            usernames.append(row["username"])
        index = time_stamps.index(min(time_stamps))
        if now < min(time_stamps):
            delta = min(time_stamps) - now
            minutes_remaining = delta.seconds / 60
            return (f"\nIn {round(minutes_remaining)} minutes, gate {gates[index]} will be free for you.\n")
        else:
            time_stamps[index] = now + timedelta(hours=truck_unload_time)
            usernames[index] = user
            with open("gates2.csv", "w") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=[
                                        "gate", "username", "timestamp"])
                writer.writeheader()
                n = 0
                while n < 3:
                    x = gates[n]
                    y = usernames[n]
                    z = time_stamps[n]
                    writer.writerow({"gate": x, "username": y, "timestamp": z})
                    n += 1
                output_file.close()
                with open("gates2.csv",) as input_file:
                    data = input_file.readlines()
                with open("gates.csv", "w") as output_file:
                    output_file.writelines(data)
                return (f"\nPlease proceed to gate {gates[index]}.\n")


def register_user(username):
    """
    Check if username is already in database and it respects the minimum conditions

    :param username: users username input
    :type username: str
    :raise Value error: When the username doesn`t respect the minimum conditions
    :return: True if conditions are met
    :rtype: boolean
    """
    usernames = []
    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            usernames.append(row["username"])
    if re.search(r"^[\w!@_#%&.]{6,12}$", username):
        if username in usernames:
            return False
        else:
            return True
    else:
        raise ValueError


def register_plate(plate):
    """
    Check if license plate number is already in database or it respects minimum conditions

    :param plate: users plate input
    :type plate: str
    :raise Value error: When the plate doesn`t respect the minimum conditions
    :return: True if conditions are met
    :rtype: boolean
    """
    plates = []
    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            plates.append(row["license plate"])
    if re.search(
            r"^(AB|AG|AR|B|BC|BH|BN|BR|BT|BV|BZ|CJ|CL|CS|CT|CV|DB|DJ|GJ|GL|GR|HD|HR|IF|IL|IS|MH|MM|MS|NT|OT|PH|SB|SJ|SM|SV|TL|TM|TR|VL|VN|VS)\d\d[A-Z]{3}$", plate, re.IGNORECASE):
        if plate in plates:
            return False
        else:
            return True
    else:
        raise ValueError


def register_passw(passw):
    """
    Check if password respects minimum conditions

    :param passw: users password input
    :type passw: str
    :raise Value error: When passw doesn`t respect the minimum conditions
    :return: True if conditions are met
    :rtype: boolean
    """
    if re.search(r"^[\w!@_#%&.-]{4,8}$", passw):
        return True
    else:
        raise ValueError


def register():
    """
    Register a new user appending to database.csv the username, license plate number and password.
    Check the three inputs for conditions.

    :raise Value error: When inputs don\`t respect minimum conditions
    :return: A string informing user that the register was succesful
    :rtype: str
    """
    while True:
        try:
            print(
                "Username must be at least 6, no more then 12, character(s) long",
                "Username must contain letters or numbers",
                "Username can contain special characters: '!@_#%&.-'",
                sep="\n")
            user = input("Please provide an new username: \n").strip()
            if register_user(user):
                break
            else:
                print("\nThere is already an account with that username. Try again: \n")
        except ValueError:
            print("\nUsername does not respect the minimum conditions. Try again: \n")

    while True:
        try:
            plate = input(
                "Please provide your vehicles license plate number: \n").strip().lower()
            if register_plate(plate):
                break
            else:
                print(
                    "\nThere is already an account for that plate number. Try again: \n")
        except ValueError:
            print("\nLicense plate does not respect Romanian standard! Try again: \n")

    while True:
        try:
            print("Password must be at least 4, no more then 8, character(s) long",
                  "Password must contain letters or numbers",
                  "Password can contain special characters: !@_#%&.-",
                  sep="\n")
            passw = input("Please provide an new password: \n").strip()
            if register_passw(passw):
                break
        except ValueError:
            print("\nPassword does not respect the minimum conditions. Try again: \n")
    with open("database.csv", "a", newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=["username", "license plate", "password"])
        writer.writerow(
            {"username": user, "license plate": plate, "password": passw})
        print("\nUser created succesfully! You can continue with authentication.\n")


def recover(username, plate):
    """
    User will recover his password after inputing username and license plate number.

    :param username: users username input
    :type passw: str
    :param plate: users license plate number input
    :type passw: str
    :return: Users password
    :rtype: str
    """
    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if username == row["username"] and plate == row["license plate"]:
                return (f"\nUser found, your password is: {row['password']}\n")
        return (f"\nUsername or license plate number are not correct.\n")


if __name__ == "__main__":
    main()
