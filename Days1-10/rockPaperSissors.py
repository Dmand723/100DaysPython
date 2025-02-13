import random as r #This will reassign the class random to the name r 
from os import system as command   
choices = ['Rock','Paper',"Scissors"]
def main():
    command('cls')#used to clear the termial for a cleaner look 
    try:
        userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
    except:
        print('please Enter a number (0, 1, or 2)')
        main()
        return
    computerChoice = r.randint(0,2)
    if userChoice >=3 or userChoice <0:
        print("Invalid choice. You loose!")
        quit()
    print(f'You picked {choices[userChoice]}')
    print(f'The computer choose {choices[computerChoice]}')
    
    if userChoice == 0 and computerChoice == 2:
        print("You win!!")
    elif computerChoice == 0 and userChoice == 2:
        print('You loose!!')
    elif computerChoice < userChoice:
        print("You win!!")
    elif computerChoice > userChoice:
        print('You loose!!')
    elif computerChoice == userChoice:
        print('Its a Draw')

if __name__ == "__main__":
    main()