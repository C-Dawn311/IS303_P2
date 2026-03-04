# Authors: Courtney Bingham, Anna, Braden Adams, Ethan Lawson

lstTeams = ["Real Salt Lake", "BYU", "UVU", "USU", "U of U", "SUU", "Utah Tech", "Weber State", "Sao Paulo", "Madrid"]

# lets the user choose their team name (and removes said name from the list) or opposing team name
# determined by what they selected from the menu function (selection) default value of 1
# should fulfill the function talked about on third requirement
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
    

# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome 
# message. Return the name to the main program and store it in variable so it can be used throughout the program.

# function to welcome user and explains rules and asks for their name and returns that to the function
# needs rules inputted
# should fulfill first requirement
def welcome():
    print("Welcome to the game!")
    print("Explain rules here")
    sName = input("Please enter your name here: ")
    return sName


# Display of menu and return choice. Store in variable and use this value to determine which function to call next.


# Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the 
# user choose the opponent but do not display the team they chose previously. Remove that team from the list. 
# Allow the user to select an opponent, and return team name. This function should receive a parameter but give 
# it a default value if none is passed. You can use this function for both choosing the home team and the opponent team.


# Play the game receiving both team names. Generate random scores without ties. Return W or L.
import random
def game_result(sHome, sAway):
    iHome = random.randrange(0,4)
    iAway = random.randrange(0,4)
    while iHomeTeam == iAwayTeam:
        iHomeTeam = random.randrange(0, 4)
        iAwayTeam = random.randrange(0, 4)
    if iHomeTeam > iAwayTeam:
        print("W")
    else:
        print("L")


# Display the final record for a team. Receive the home team data and display information.

