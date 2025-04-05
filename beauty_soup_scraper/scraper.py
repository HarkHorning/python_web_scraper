import asyncio
from bs4 import BeautifulSoup
import requests

cookbook = [ # Add your link(s) here
    'https://www.scrapethissite.com/pages/forms/',
    'https://www.scrapethissite.com/pages/simple/'
]

order = 'h1' # Put what are you looking for here

async def fetch(recipe):
    ingredients = requests.get(recipe)
    soup = BeautifulSoup(ingredients.text, 'html.parser')
    your_serving = soup.find(order)
    # return your_serving
    print(your_serving)

for recipe in cookbook:
    asyncio.run(fetch(recipe))
