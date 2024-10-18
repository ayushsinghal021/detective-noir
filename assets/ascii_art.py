import os

class ASCIIGraphics:
    def __init__(self, graphics_dir):
        self.graphics_dir = graphics_dir
        self.graphics = {
            "title": os.path.join(graphics_dir, "detective_title.txt"),
            "suspect": os.path.join(graphics_dir, "suspect_art.txt"),
            "crime_scene": os.path.join(graphics_dir, "crime_scene_art.txt"),
            "suspect_house": os.path.join(graphics_dir, "suspect_house_art.txt"),
            "alley": os.path.join(graphics_dir, "alley_art.txt")
        }

    def print_ascii_art(self, art_name):
        """Print the specified ASCII art."""
        art_file = self.graphics.get(art_name)
        if art_file and os.path.exists(art_file):
            with open(art_file, 'r') as file:
                print(file.read())
        else:
            print(f"Error: {art_name} art not found.")

# Example usage of ASCIIGraphics
if __name__ == "__main__":
    graphics = ASCIIGraphics(graphics_dir='graphics')
    
    # Print the game title
    graphics.print_ascii_art("title")
    
    # Print art for the crime scene (can be called when the player enters the crime scene)
    graphics.print_ascii_art("crime_scene")
    
    # Print art for suspect house
    graphics.print_ascii_art("suspect_house")
    
    # Print art for alley
    graphics.print_ascii_art("alley")