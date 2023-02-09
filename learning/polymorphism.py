#
# Python:   3.10.7
#
# Author:   Bryan
#
# Purpose:  The Tech Academy - Python Course, Creating a sql database using Python.


# Parent class
class Player:
    name = "Jon"
    email = "jon@gmail.com"
    password = "125five"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your Password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("You have returned again, {}!.".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child class
class Game(Player):
    game_tokens = 555
    game_completed = "55%"

# Child class 2
class Apex(Player):
    apex_rank = "Gold"
    apex_kd = "1.5"
    apex_pin = "2355"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_name == self.email and entry_pin == self.pin_number):
            print("Welcome, {}!".format(entry_name))
        else:
            print("The pin you or email you used is wrong.")

    

customer = Player()
customer.getLoginInfo()

apex = Game()
apex.getLoginInfo()
