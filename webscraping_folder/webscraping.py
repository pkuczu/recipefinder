# Web scraping
import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('recipes.sql')
request = requests.get("https://www.allrecipes.com/")
if request.status_code != 200:
    print("Error in retrieving the webpage.")
    exit()
bs = BeautifulSoup(request.content, 'html5lib')
#print(bs.prettify())

# def extract_recipe_info(soup):
#     recipes = []
#     # Find all elements that contain recipe information
#     recipe_elements = soup.find_all(class_='card__detailsContainer')

#     for element in recipe_elements:
#         recipe_info = {}

#         # Extract recipe title
#         title_element = element.find('span', class_='card__title')
#         if title_element:
#             recipe_info['name'] = title_element.text.strip()

#         # Extract ingredients
#         ingredients_list = element.find_all('span', class_='ingredients-item-name')
#         if ingredients_list:
#             recipe_info['ingredients'] = ', '.join(ingredient.text.strip() for ingredient in ingredients_list)

#         # Extract instructions
#         instructions_element = element.find('div', class_='card__directions')
#         if instructions_element:
#             instructions_list = instructions_element.find_all('li', class_='subcontainer')
#             if instructions_list:
#                 recipe_info['instructions'] = '\n'.join(instruction.text.strip() for instruction in instructions_list)

#         recipes.append(recipe_info)

#     return recipes

# recipes = extract_recipe_info(bs)
# for recipe in recipes:
#     cursor.execute('''
#         INSERT INTO recipes (title, ingredients, instructions)
#             VALUES (?, ?, ?)
#         ''', (recipe['title'], recipe['ingredients'], recipe['instructions']))
#     conn.commit()
# conn.close()
