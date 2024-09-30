# starter.py

import requests

def get_random_joke():
    """Fetch a random joke from an online API."""
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} ... {joke['punchline']}"
    else:
        return "Failed to fetch a joke."

if __name__ == "__main__":
    print("Fetching a random joke for you...")
    print(get_random_joke())