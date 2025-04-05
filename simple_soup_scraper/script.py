from bs4 import BeautifulSoup
import requests

target = 'https://www.scrapethissite.com/pages/simple/' # Add your link here

try:
    ingredients = requests.get(target)
except Exception as err:
    print(f"Your error, sir: {err}")

mark_up = 'lxml'

le_soupe = BeautifulSoup(ingredients.text, mark_up)

print(
    le_soupe.find(
        'h1'
    ) # .text.strip()
)
