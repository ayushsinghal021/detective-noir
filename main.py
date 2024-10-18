import os
from game import Game

def clear_screen():
    """Clear the console screen for a cleaner interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function to run the Detective Noir game."""
    clear_screen()
    print("Welcome to Detective Noir: The Case of the Missing Heirloom!")
    print("Get ready to solve a thrilling mystery!\n")

    game = Game()
    game.play()

if __name__ == "__main__":
    main()