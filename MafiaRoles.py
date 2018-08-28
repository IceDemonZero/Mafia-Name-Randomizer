"""
This project is made to randomly assign roles for mafia games.
"""
import random as ran
import sys as s

__author__ = 'Jay Edwards'


class Mafia:
    def __init__(self):
        self.fullPlayers = False  # Checks if the numbers of players is full
        self.fullRoles = False   # Checks if the numbers of roles is full
        self.playersList = []  # The list that holds player names
        self.rolesList = []  # The list that holds role names
        self.finalPairs = []  # The list that will hold the assigned names and roles

    def players(self):
        max_players = int(input("How many players will there be?: "))  # maximum amount of players allowed
        number_of_players = 0  # numberOfPlayers will be the number of players entered so far
        while number_of_players <= max_players:  # Loops around until condition is met
            list_of_players = input("Give me a player name please: ")  # Takes in names as input
            self.playersList.append(list_of_players)  # Adds the name to a list
            number_of_players = number_of_players + 1  # Increases the number of players entered
            if number_of_players == max_players:  # checks if all players have been entered
                print("All player names have been entered.")
                self.fullPlayers = True  # The list is now full so we have all the players required
                self.roles()  # Tells the next function to start

    def roles(self):
        max_roles = int(input("How many roles will there be?: "))  # maxRoles is the maximum amount of roles allowed
        number_of_roles = 0  # numberOfRoles will be the number of roles entered so far
        while number_of_roles <= max_roles:  # Does the same things as the loop in players() except its for roles
            list_of_roles = input("Give me a role please: ")
            self.rolesList.append(list_of_roles)  # Adds a role to the list
            number_of_roles = number_of_roles + 1
            if number_of_roles == max_roles:  # checks if all roles have been entered
                print("All roles have been entered.")
                self.fullRoles = True
                self.randomize_roles()  # Tells the final function to start

    def randomize_roles(self):
        check_players = len(self.playersList)  # an integer which calculates the number of players
        check_roles = len(self.rolesList)  # same as above but for roles

        if self.fullPlayers and self.fullRoles:  # Checks if lists are full
            if check_players < check_roles:
                answer = input("Do you want to proceed with less players then there are roles? (Answer yes or no): ")
                if answer == "Yes" or "yes" or "Y" or "y":
                    ran.shuffle(self.rolesList)
                    ran.shuffle(self.playersList)

                    for player, role in zip(self.playersList, self.rolesList):
                        self.finalPairs.append(player + ": " + role)
                    print(self.finalPairs)
                    s.exit()
                elif answer == "No" or "no" or "N" or "n":
                    s.exit()
            elif check_players > check_roles:
                answer = input("Are you sure you want to proceed? Not everyone will get a role? (Answer yes or no): ")
                if answer == "Yes" or "yes" or "Y" or "y":
                    ran.shuffle(self.rolesList)
                    ran.shuffle(self.playersList)

                    for player, role in zip(self.playersList, self.rolesList):
                        self.finalPairs.append(player + ": " + role)
                    print(self.finalPairs)
                    s.exit()
                elif answer == "No" or "no" or "N" or "n":
                    s.exit()
            else:
                ran.shuffle(self.rolesList)
                ran.shuffle(self.playersList)

                for player, role in zip(self.playersList, self.rolesList):
                    self.finalPairs.append(player + ": " + role)
                print(self.finalPairs)
                s.exit()


mafia = Mafia()  # Creating a class instance
mafia.players()
