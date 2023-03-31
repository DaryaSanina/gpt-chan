import openai
from dotenv import load_dotenv
import os

# Get the OpenAI API key
path = os.path.join(os.path.dirname(__file__), '.env')  # Path to .env file (in the same directory as this code)
if os.path.exists(path):  # If the .env file exists
    load_dotenv(path)
    openai.api_key = os.environ.get('OPENAI_API_KEY')  # Load the key
else:
    print("No .env file")

while True:
    # Get the user input
    query = input()

    # Generate the response
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": query}
      ]
    )

    # Display the response
    print(response.choices[0].message.content)
