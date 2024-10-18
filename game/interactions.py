from nlp import NLP

class Interactions:
    def __init__(self, characters_data):
        self.characters_data = characters_data
        self.nlp = NLP(api_key='YOUR_OPENAI_API_KEY')  # Replace with your actual API key

    def interact_with_suspect(self, suspect_key):
        """Interact with a suspect and show their dialogue."""
        suspect = self.characters_data['suspects'][suspect_key]
        print(suspect['dialogues']['greeting'])
        user_input = input("What do you want to ask them? ")
        response = self.nlp.get_response(user_input)
        print("Suspect:", response)

    def handle_command(self, command):
        """Process player commands and provide responses."""
        command = command.lower()
        if "talk to" in command:
            suspect_key = command.split("talk to ")[-1].strip()
            self.interact_with_suspect(suspect_key)
        else:
            print("Invalid command. Try 'talk to [suspect name]'.")