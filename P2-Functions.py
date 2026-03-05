# Authors: Courtney Bingham, Anna Pettit, Braden Adams, Ethan Lawson


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

# Display of menu and return choice. Store in variable and use this value to determine which function to call next.


#  Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the 
# user choose the opponent but do not display the team they chose previously. Remove that team from the list. 
# Allow the user to select an opponent, and return team name. This function should receive a parameter but give 
# it a default value if none is passed. You can use this function for both choosing the home team and the opponent team.


# Play the game receiving both team names. Generate random scores without ties. Return W or L.


# Display the final record for a team. Receive the home team data and display information.

