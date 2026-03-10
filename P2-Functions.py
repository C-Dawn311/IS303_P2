# Authors: Courtney Bingham, Anna Pettit, Braden Adams, Ethan Lawson

# Program that allows a user to simulate a soccer season by choosing options from a menu. 
# User will be able to select a home team, opponent teams, and the program assigns random scores
# and displays the results. 

import random

# Function 1 - Display menu and return choice
def menu() :
    print("--Menu--")
    print("1. Choose opposing team")
    print("2. Play game")
    print("3. Display final record")
    print("4. Exit")

    choice = 0
    #prompt user for menu choice and assign value
    while choice not in range(1,5) :
        try :
            choice = int(input("Please select your choice (1-4): "))
        except :
            print("Please enter a number between 1 and 4. ")
    return choice

#Function (#2/3) that allows user to select home and opponent teams
def teamname(selection = 1):
    if selection == 1:
        print(lstTeams)
        sTeamName = input("Enter your team name: ")
        lstTeams.pop(sTeamName) 
        return sTeamName
    elif selection == 2:
        print(lstTeams)
        sOppTeam = input("Enter the opposing team: ")
        # I don't know whether we need to get rid of the opposing team or not
        return sOppTeam

#Function (#4) that randomly generates scores for home and opponent teams
def game_result(sHome, sAway):
    global lstWins
    global lstLosses

    #generate random scores for games, without ties
    iHomeTeam = random.randrange(0,4)
    iAwayTeam = random.randrange(0,4)
    while iHomeTeam == iAwayTeam:
        iHomeTeam = random.randrange(0, 4)
        iAwayTeam = random.randrange(0, 4)
    
    #calculate win or loss, and add to wins and losses lists
    if iHomeTeam > iAwayTeam:
        print("W")
        lstWins.append(sAway)
    else:
        print("L")
        lstLosses.append(sAway)

# FUNCTION 5 - Calculates and displays final record
def display_record(iWins,iLosses) : 
    global dctGameLog
    global lstWins
    global lstLosses
    
    #final calculations and display
    iPercentageWon = iWins / (iWins + iLosses)
    dctGameLog.update({
        "Won Against" : lstWins,
        "Lost Against" : lstLosses
        })

    #Print out: Teams won against:
    print ("\n---Teams won against---")
    for wins in dctGameLog['Won Against'] :
        print(f'- {wins}')

    #Print out: Teams lost against
    print("\n---Teams lost against---")
    for losses in dctGameLog['Lost Against'] :
        print(f'- {losses}')

    #Print out Final season record 
    print( f"\nFinal season record: {iWins} - {iLosses}")

    #After all of this, print out a final message based on the record of the home team.
    if iPercentageWon >= 0.75 :
        print( "Qualified for the NCAA Soccer Tournament! Congrats!")
    elif iPercentageWon >= 0.5 :
        print( "You had a good season. We're excited to see you next year!")
    else :
        print( "Your team needs to practice! You got it next year.")


#--------MAIN PROGRAM--------

#DEFINE FUNCTIONS
dctGameLog = {}
lstWins = []
lstLosses = []


lstTeams = ["Real Salt Lake", "BYU", "UVU", "USU", "U of U", "SUU", "Utah Tech", "Weber State", "Sao Paulo", "Madrid"]

# lets the user choose their team name (and removes said name from the list) or opposing team name
# determined by what they selected from the menu function (selection) default value of 1
# should fulfill the function talked about on third requirement
    

# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome 
# message. Return the name to the main program and store it in variable so it can be used throughout the program.
print("--- Official Soccer League ---")
bContinue = True

while bContinue == True :
    try : 
        sUserName = str(input("Please enter your name: "))
        bContinue = False
    except: 
        print("That is an invalid entry. Please enter your name.")

#Display welcome message
# function to welcome user and explains rules and asks for their name and returns that to the function
# needs rules inputted
# should fulfill first requirement

# Display of menu and return choice. Store in variable and use this value to determine which function to call next.


# Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the 

# user choose the opponent but do not display the team they chose previously. Remove that team from the list. 
# Allow the user to select an opponent, and return team name. This function should receive a parameter but give 
# it a default value if none is passed. You can use this function for both choosing the home team and the opponent team.


# Play the game receiving both team names. Generate random scores without ties. Return W or L.


# Display the final record for a team. Receive the home team data and display information.


