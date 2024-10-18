# Detective Noir: The Case of the Missing Heirloom

## Game Description
**Detective Noir** is an AI-powered text adventure game that combines classic interactive fiction with modern AI technology. You play as a detective tasked with solving the case of a missing heirloom. Navigate through different locations, gather clues, and interrogate suspects to piece together the mystery. Your choices determine the outcome, leading to multiple endings!

## Table of Contents
- [Installation Instructions]
- [Gameplay Guide]
- [Commands]
- [Game Structure]
- [Requirements]
- [License]

## Installation Instructions
To set up the game on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/detective-noir.git
   cd detective-noir
   ```

2. **Install Required Packages**
   Use the following command to install all the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key** (Optional)
   If you wish to use NLP features, ensure you have an OpenAI API key. Replace `'YOUR_OPENAI_API_KEY'` in `interactions.py` with your actual API key.

## Gameplay Guide
1. **Starting the Game**
   Run the main game script:
   ```bash
   python main.py
   ```

2. **Navigating Locations**
   You will be prompted with descriptions of locations and clues. Choose your next location based on the options provided.

3. **Finding Clues**
   As you navigate, you can find clues that help you solve the case. Collect enough clues to progress.

4. **Interacting with Suspects**
   You can talk to suspects to gather more information. Use the `talk to [suspect name]` command to initiate conversations.

5. **Ending the Game**
   The game will end once you have gathered enough clues or have made enough interactions to solve the case.

## Commands
- **Navigate**: Simply choose from the available locations when prompted.
- **Find Clue**: You will automatically find clues when navigating.
- **Interact with Suspects**: Use the command:
  ```
  talk to [suspect name]
  ```
  Replace `[suspect name]` with the name of the suspect you want to interact with.

### Example Commands
- `talk to Mr. Smith`
- `talk to Ms. Johnson`

## Game Structure
Here's an overview of the project's structure:

```
detective-noir/
│
├── README.md                # Game description, installation instructions, and play guide
├── requirements.txt         # List of required Python packages
├── main.py                  # Main game logic and execution
│
├── assets/                  # Directory for ASCII art and other assets
│   ├── ascii_art.py         # Script to define ASCII art (e.g., titles, rooms)
│   └── graphics/            # Subdirectory for any additional ASCII art files
│       ├── detective_title.txt   # ASCII art for the game title
│       └── suspect_art.txt      # ASCII art for suspect representations
│
├── data/                    # Directory for game data files
│   ├── story.json           # JSON file containing story structure (locations, suspects, clues)
│   └── characters.json      # JSON file for character attributes and dialogues
│
├── game/                    # Main game logic
│   ├── __init__.py          # Init file for the game package
│   ├── game.py              # Core game logic (state management, main loop)
│   ├── nlp.py               # NLP integration (spaCy or OpenAI API logic)
│   └── interactions.py       # Handling player interactions, commands, and responses
│
└── .gitignore               # Files and directories to ignore in version control
```

## Requirements
Make sure you have the following installed:
- Python 3.7 or later
- Required Python packages listed in `requirements.txt`

### Example `requirements.txt`
```plaintext
openai
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the content as needed. Enjoy playing Detective Noir!
