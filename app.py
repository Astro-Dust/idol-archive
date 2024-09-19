from urllib.request import urlopen
from fastapi import FastAPI
from bs4 import BeautifulSoup

# WEB SCRAPING

html = urlopen('https://kpopping.com/profiles/the-idols/women')
bs = BeautifulSoup(html, 'html.parser')

names = bs.find_all('div', {'class':'item'})
groups = bs.find_all('div', {'class':'item'})

idols_storage = {}

for name, group in zip(names, groups):
    idol_name = name.find('a')
    idol_group = group.find('span')

    if idol_name and idol_group:
        idols_storage[idol_name.text] = idol_group.text


# CLEANING ANNOYING IDOL GROUP'S PARENTHESIS

def clean_data(idols_storage:dict) -> dict:
    cleaned_storage = {}

    # removing parenthesis and commas
    for key, value in idols_storage.items():
        cleaned_value = value.replace('(', '').replace(')', '').replace(',', '').replace('\n', '').strip()
        cleaned_storage[key] = cleaned_value

    return cleaned_storage


# CREATING AN ENDPOINT

app = FastAPI()

@app.get('/get-idols')
def get_idols():
    return clean_data(idols_storage)
