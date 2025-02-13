def main():
    print('''   Welcome to Treasure Island.
    Your mission is to find the treasure.''')
    ans1 = input("You are at a crossroads do you go left or right?: ").upper()
    if ans1 == 'RIGHT':
        print("You fall into a hole. Game Over.")
        agian = input('would you like to try again? (y/n): ').upper()
        if agian == ("Y" or "YES"):
            main()
        else:
            quit()
    elif ans1 == 'LEFT':
        ans2 = input('You\'ve cometo a lake. There is an island in the middle of the lake do you "wait" for a boat or do you "swim" to the island?: ').upper()
        if ans2 == "SWIM":
            print('''You get Attacked by trout.
                Game Over''')
            again = input('would you like to try again? (y/n): ').upper()
            if agian == ("Y" or "YES"):
                main()
            else:
                quit()
        elif ans2 == "WAIT":

