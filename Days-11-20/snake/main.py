from scripts.settings import *
from scripts.classes.gameClass import Game



def main():
    game = Game()
    game.setup()
    game.mainLoop()

if __name__ == '__main__':
    main()