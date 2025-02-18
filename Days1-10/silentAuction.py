from os import system as command
art = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                   jgs/_______________\\
                    '''
class SilentAuction():
    def __init__(self,item,startPrice):
        self.item = item
        self.startPrice = startPrice
        
        self.bidsDict = {}
        self.playing = True
        
    def addBid(self):
        command('cls')
        print(f'This is a silet aution for {self.item}')
        print(f"the starting bid ammmout is ${self.startPrice}")
        name = input("Bidder Name: ")
        ammount = float(input("Bid Ammount: $"))
        if not ammount >= self.startPrice:
            print("Please enter a number equal to or higher then the starting bid ammount")
            self.addBid()
        self.bidsDict[name] = ammount
    def getHighestBidder(self):
        command('cls')
        highestBidder = max(self.bidsDict, key=self.bidsDict.get)
        print(f"The winner is {highestBidder} with the ammount of  ${self.bidsDict[highestBidder]}")
    def start(self):
        self.addBid()
        while self.playing:
            q = input("Add another bidder? (Y/N): ").upper()
            if q == "Y" or q == "YES":
                self.addBid()
            else:
                self.getHighestBidder()
                self.playing = False
                quit()

def main():
    print(art)
    print("Welcome to The silet action")
    bidItem = input("What item is being auctioned off today?: ")
    startPrice = float(input("What is the starting bid ammount: $"))
    aution = SilentAuction(bidItem,startPrice)
    aution.start()

if __name__ == "__main__":
    main()