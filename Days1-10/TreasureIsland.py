
#This is the main def for the start of the game-------------------------------------------------------------------------- 
def main():
    print('''   Welcome to Treasure Island.
        Your mission is to find the treasure.''')
    q1()
#------------------------------------------------------------------------------------------------------------------------      
#This is question 1 of the game------------------------------------------------------------------------------------------            
def q1():
    ans1 = input("You are at a crossroads do you go left or right?: ").upper()
    if ans1 == 'RIGHT':
        print("You fall into a hole. Game Over.")
        again()
    elif ans1 == 'LEFT':
        q2()
    else:
        print('Please enter either "left" or "right"')
        q1()
#------------------------------------------------------------------------------------------------------------------------

#This is question 2 of the game------------------------------------------------------------------------------------------
def q2():
    ans2 = input('You\'ve come to a lake. There is an island in the middle of the lake do you '
                 '"wait" for a boat or do you "swim" to the island?: ').upper()
    if ans2 == "SWIM":
        print('''You get Attacked by trout.
            Game Over''')
        again()
    elif ans2 == "WAIT":
        q3()
    else:
        print('Plese enter either "swim" or "wait"')
#------------------------------------------------------------------------------------------------------------------------

#This is question 3 of the game -----------------------------------------------------------------------------------------
def q3():
    ans3 = input("The boat came and you arive at the island unharmed."
                 "There is a house with 3 doors, one \x1b[31mred\x1b[0m, one \x1b[93myellow\x1b[0m, and one \x1b[34mblue\x1b[0m. What color do you choose?: ").upper()
    if ans3 == "RED":
        print('You walk in the door and are Burned by fire. Game Over.')
        again()
    elif ans3 == "YELLOW":
        print('''*******************************************************************************
                            |                   |                  |                     |
                    _________|________________.=""_;=.______________|_____________________|_______
                    |                   |  ,-"_,=""     `"=.|                  |
                    |___________________|__"=._o`"-._        `"=.______________|___________________
                            |                `"=._o`"=._      _`"=._                     |
                    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                    /______/______/______/______/______/______/______/______/______/______/[TomekK]
                    *******************************************************************************''')
        print('You walk through the door and find the treasure chest!!! YOU WIN!')
        input("Press enter to quit")
        quit()
    elif ans3 == "BLUE":
        print("You walk throgh the door and get eated by beasts. Game over.")
        again()
    else:
        print('Please Enter either "red", "yellow", or "blue"')
        q3()
#------------------------------------------------------------------------------------------------------------------------

#This is the def to ask if you want to retry----------------------------------------------------------------------------- 
def again():
    again = input('would you like to try again? (y/n): ').upper()
    if again == ("Y" or "YES"):
        main()
    else:
        quit()
#------------------------------------------------------------------------------------------------------------------------

#This starts the game when you run the file------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
#------------------------------------------------------------------------------------------------------------------------
#Finish adding so if you type an ans that is not a option it lets you retype it 