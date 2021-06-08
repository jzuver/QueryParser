
from parserFunctions import *
import data
import os.path as path

def main():
    print("enter: help \n or load data and begin query")

    keepRunning  = True

    # loop to allow for as many queries as desired, will run until user types quit
    while keepRunning:

        # get user input
        userInput = input(">")

        # check if user wants to quit, print help, or create/overwrite the database
        if userInput.lower() == "quit":
            keepRunning = False

        elif userInput.lower() == "help":
            printHelp()

        elif userInput.lower() == "load data":
            data.initDb()
            print("Database created (or overwritten).")

        # split user input string into individual components
        userInputList = inputToList(userInput)

        # if the query is valid, and the database exists, establish connection, do query, and print query results
        if validateInput(userInputList) and path.exists("data.db"):

            cur = data.sqliteConnect()

            if len(userInputList) == 4:
                # case for join statement, allows for the user to type in the join statement as outlined for
                # our query language
                if userInputList[0].lower() == "tweet" and userInputList[1].lower() == "insults" and userInputList[2].lower() == "losers":
                    print(data.fetch(cur, userInputList[3]))

                # case for non-join statement queries
                else:
                    print(data.fetch(cur, userInputList[3], userInputList[1], userInputList[0], userInputList[2]))

        # if database hasn't been created, display error message to user
        elif not path.exists("data.db"):
            print("The database has not been created yet. Please use the load data command to create the database.")

        # case for if database exists, but user entered an invalid query
        elif userInput.lower() != "help" and userInput.lower() != "quit":
            print("Invalid query, type help for list of commands.")

main()
