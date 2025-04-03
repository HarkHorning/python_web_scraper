from bs4 import BeautifulSoup
import requests

target = ''

try:
    ingredients = requests.get(target)
except Exception as err:
    print(f"Your error, sir: {err}")

mark_up = 'lxml' or 'html'

le_soupe = BeautifulSoup(ingredients.text, mark_up)

print(
    le_soupe.find(
        'h1'
    ).text.strip()
)
