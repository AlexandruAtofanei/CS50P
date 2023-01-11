# Academic Honesty
https://cs50.harvard.edu/python/2022/honesty/#policy
## Aby to the Academic Honesty Policy and do not copy the solutions.

# Warehouse Manaement
#### Video Demo:  <https://youtu.be/RZJjEl4LdiM>
#### Description:
The program was design to help whith a wherehouse gate unloading management, removing the need of a warehouse gate dispatcher. The program should be used by truck drivers so they can be automatically assigned to a free unloading gate, or be informed, if all gates are ocupied, which one and in how many minutes will free first.
At initializng the program the user is prompted with a menu that has 4 options: "Authenticate", "Register a new account", "Recover Password" and "Exit the Program".
A new user will have first to register an account providing his username, license plate number and password. Username and Password have to met some lenght and character conditions, user is informed of them. License plate number will be checked to met the Romania standard for license plates.
User is informed for any of the three inputs if the conditions are not met and reprompted for a new input. Also, the program checks in the file "database.csv" if there is already an account with the same username or license plate number.
If all conditions are met, they will be stored in a file "database.csv" and with a message the user is informed that the registration of the new account was succesful.
After registration, the user will authenicate with his user name and password, the inputs will be matched in the file "database.csv" to assess if they exist, user will be informed if the username and password are wrong.
With a succesfull authentication, the program will next check for any available free gate in the file "gates.csv". "gates.csv" is structured with an header containing three elements "gate"(the gate number), "username" and "timestamp"(time format datetime.datetime).The program will iterate through all the gates getting the one with the lowest value of the timestamp. If that timestamp is lower then current time, the username will be directed to that gate for unloading. But if all timestamp values are greater then the current time, meaning all gates are ocupied, the user will be informed which gate finishes is freed first and in how many minutes.
The time for a truck unloading was set through a parameter "h" to 4 hours.
Because I couldn`t fiind in the python oficial documentation how to replace the value in a row in a .csv file, the solution I proposed was to iterate through all the rows of the file "gates.csv", write them to a new file "gates2.csv" replacing the old timestamp with the new one (curent timetamp + 4 hours), also appending the username to that line and at the end from "gates2.csv" transfering all data to "gate.csv"
The user also has the posibility in the case of losing his password to recover it. From the menu, the "Recover password" option will prompt the user for his username and license plate number, outputing his password.
And of course, last option, "Exit the program", will exit the program.
