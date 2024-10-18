import json
import random
from ascii_art import ASCIIGraphics
from interactions import Interactions

class Game:
    def __init__(self):
        self.graphics = ASCIIGraphics(graphics_dir='assets/graphics')
        self.story_data, self.characters_data = self.load_data()
        self.current_location = "crime_scene"
        self.clues_found = []
        self.interactions = Interactions(self.characters_data)

    def load_data(self):
        """Load story and character data from JSON files."""
        with open('data/story.json', 'r') as story_file:
            story_data = json.load(story_file)

        with open('data/characters.json', 'r') as characters_file:
            characters_data = json.load(characters_file)

        return story_data, characters_data

    def print_location_description(self):
        """Print the description of the current location."""
        location_details = self.story_data['locations'][self.current_location]
        print(location_details['description'])
        print("Clues available:", ", ".join(location_details['clues']))
        print("You can go to:", ", ".join(location_details['next']))

    def navigate(self):
        """Navigate to different locations."""
        print("Where would you like to go?")
        options = self.story_data['locations'][self.current_location]['next']
        for i, option in enumerate(options, 1):
            print(f"{i}. {option.replace('_', ' ').title()}")
        
        choice = int(input("Choose a location (1/2): ")) - 1
        if 0 <= choice < len(options):
            self.current_location = options[choice]
        else:
            print("Invalid choice, please try again.")

    def find_clue(self):
        """Find a clue in the current location."""
        clues = self.story_data['locations'][self.current_location]['clues']
        if clues:
            found_clue = random.choice(clues)
            self.clues_found.append(found_clue)
            print(f"You found a clue: {found_clue}")
            clues.remove(found_clue)  # Remove the found clue

    def play(self):
        """Main game loop."""
        self.graphics.print_ascii_art("title")
        while True:
            self.print_location_description()
            self.find_clue()
            self.navigate()
            if len(self.clues_found) >= 3:  # Example condition to end the game
                print("You have gathered enough clues to solve the case!")
                break

if __name__ == "__main__":
    game = Game()
    game.play()