# Authors: Courtney Bingham, Anna, Braden Adams, Ethan Lawson

# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome 
# message. Return the name to the main program and store it in variable so it can be used throughout the program.


# Display of menu and return choice. Store in variable and use this value to determine which function to call next.


#  Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the 
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


