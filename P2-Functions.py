# Authors: Courtney Bingham, Anna Pettit, Braden Adams, Ethan Lawson
# Section 004
# 3/9/2026

# Program that allows a user to simulate a soccer season by choosing options from a menu. 
# User will be able to select a home team, opponent teams, and the program assigns random scores
# and displays the results. 

#------------------  DEFINE VARIABLES/LISTS/IMPORT LIBRARIES ---------------------------------
import random
dctGameLog = {}
lstWins = []
lstLosses = []
iWins = 0
iLosses = 0
lstTeams = ["RSL", "BYU", "UVU", "USU", "SUU", "MIT", "NYU", "USC", "ASU", "TCU", "FSU", "UT", "UGA", "CSU"]
sOpp = lstTeams[0]

#--------------------------------- CUSTOM FUNCTIONS --------------------------------------------
# Function 1 - Display menu and return choice
def menu() :
    #display menu options
    print("\n-- Menu --")
    print("1. Choose opposing team")
    print("2. Play game")
    print("3. Display final record")
    print("4. Exit")

    iChoice = 0
    #prompt user for menu choice and assign value
    while iChoice not in range(1,5) :
        repeat = True
        #verify that user enters a valid input (number between 1 and 4)
        while repeat:
            try : 
                choice = int(input("\nPlease select your choice (1-4): "))
                repeat = False
            except :
                print("Please enter a valid integer. ")
        if choice in range(1,5):
            return choice
        else:
            print("Please enter a number between 1 and 4.")
            

#Function (#2/3) that allows user to select home and opponent teams
def team_name(selection = 1):
    global lstTeams

    #home team option
    if selection == 1:
        
        #display teams list
        print("\nPlease enter one of the following teams: ")
        print(", ".join(lstTeams))
        
        #prompt user for home team
        sTeamName = input("Enter your team name: ").upper()

        #verify that team exists in the list
        while sTeamName not in lstTeams:
            print("Please enter a valid team.")
            print(", ".join(lstTeams))
            sTeamName = input("Enter your team name: ").upper()
        
        #remove home team from list once selected
        lstTeams.remove(sTeamName) 

        return sTeamName
    
    #away team option
    elif selection == 2:

        #display teams list
        print("Please enter one of the following teams.")
        print(", ".join(lstTeams))

        #prompt user for opponent team
        sOppTeam = input("Enter the opposing team: ").upper()

        #verify that team exists in the list
        while sOppTeam not in lstTeams:
            print("Please enter a valid team.")
            print(", ".join(lstTeams))
            sOppTeam = input("Enter the opposing team: ").upper()

        return sOppTeam

#Function (#4) that randomly generates scores for home and opponent teams
def game_result(sAway = lstTeams[0]):
    global lstWins
    global lstLosses
    global iWins
    global iLosses

    #generate random scores for games, without ties
    iHomeTeam = random.randrange(0,4)
    iAwayTeam = random.randrange(0,4)
    while iHomeTeam == iAwayTeam:
        iHomeTeam = random.randrange(0, 4)
        iAwayTeam = random.randrange(0, 4)
    
    #calculate win or loss, and add to wins and losses lists/running counter
    if iHomeTeam > iAwayTeam:
        print(f"Win against {sAway}! Score: {iHomeTeam} - {iAwayTeam}")
        lstWins.append(sAway)
        iWins += 1
    else:
        print(f"Loss against {sAway}! Score: {iHomeTeam} - {iAwayTeam}")
        lstLosses.append(sAway)
        iLosses += 1

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

#FUNCTION to display a welcome message
def welcomemessage():
    #entrance text
    print("\n--- Official Soccer League ---")

    bContinue = True

    #prompt for user name
    while bContinue == True :
        try : 
            sUserName = input("\nWe're glad you're here! Please enter your name: ").title()
            bContinue = False
        except: 
            print("That is an invalid entry. Please enter your name.")
    
    return sUserName


#----------------------MAIN PROGRAM-----------------------------
# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. 
sUserName = welcomemessage()
print(f"\nWelcome to the premier soccer league simulation, {sUserName}! ")

#Display league rules
print("\n--- League Rules ---")
print("This game will simulate a soccer league by allowing you, the user, to choose the name of your home team from a list. " \
"Then, simulate a season by choosing an opposing team with the option 1. Upon clicking option 2, " \
"you will be able to play said team as many times as you wish! Each win and loss will be recorded. " \
"When you are ready for the season to be over, select option 3 to display the final record. " \
"However beware that once selected, your season will end. If at any time you wish to exit early, select option 4. "
"(Our feelings won't be hurt.) Have fun! ")

#lets user choose their home team, and displays choice
sHome = team_name(1)
print(f"Congratulations! You are now team {sHome}. ")

#display program menu and return choice while the choice is 1 and 2, with options 3 and 4 terminating the program after
#the displayed actions
bContinue = True
while bContinue == True :

    #display program menu
    iChoice = menu()

    # choose opposing team
    if iChoice == 1:
        sOpp = team_name(2)

    # play game
    elif iChoice == 2:
        game_result(sOpp)

    #display final record
    elif iChoice == 3:
        display_record(iWins,iLosses)
        bContinue = False
    
    #option 4; terminates program
    else:
        bContinue = False

print("\nThank you for playing. Have a nice day! ")

#thank you so much! :)