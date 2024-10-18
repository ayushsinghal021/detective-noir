import openai

class NLP:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, user_input):
        """Get a response from the OpenAI API based on user input."""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content'].strip()