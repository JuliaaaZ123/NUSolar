# starter.py

import requests
import random

def get_random_joke():
    """Fetch a random joke from an online API."""
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} ... {joke['punchline']}"
    else:
        return "Failed to fetch a joke."


def get_random_name():
    """Fetch a random name from list."""
    names=[
        "shirley",
        "Willie wildcat",
        "Schill",
        "Hummel"
    ]
    return random.choice(names)
if __name__ == "__main__":
    print("Fetching a random name for you...")
    print(get_random_name())