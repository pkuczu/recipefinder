# current branch name: finalizing_database

from bs4 import BeautifulSoup
import requests
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('recipes.sql')

def getRecipeAllRecipes(ingredient):
    # Get first page 
    url = "https://www.allrecipes.com/search?q=" + ingredient
    request = requests.get(url)
    if request.status_code != 200:
        print("Error in retrieving the webpage.")
        exit()
    page_html = BeautifulSoup(request.content, 'html5lib')

    num_repeat = len(page_html.find_all("a", class_="button--outlined-little-round type--rabbit-bold")) + 1

    for i in range(num_repeat):
        x = i * 24
        url = "https://www.allrecipes.com/search?" + ingredient + "=" + ingredient + "&" + "offset=" + str(x) + "&q=" + ingredient
        request = requests.get(url)
        if request.status_code != 200:
            print("Error in retrieving the webpage.")
            exit()
        page_html = BeautifulSoup(request.content, 'html5lib')

        links = page_html.find_all("a") # Find all elements with the tag <a>

        for link in links:
            if (link.get("href").find("https://www.allrecipes.com/recipe") != -1 and link.get("href").find("https://www.allrecipes.com/recipes/201") == -1 and link.get("href").find(ingredient) != -1):
                # f.write(link.get("href"))
                # f.write('\n')
                # getIngredientsAllRecipes(link.get("href"))
                actual_link = link.get("href")
                ingredient_list = getIngredientsAllRecipes(link.get("href"))
                ingredient_str = ''
                for i in ingredient_list:
                    ingredient_str = ingredient_str + i[1:len(i)-1] + ', '
                cursor.execute('''INSERT INTO test VALUES (?, ?)''', (actual_link, ingredient_str))

def getIngredientsAllRecipes(url):
    request = requests.get(url)
    if request.status_code != 200:
        print("Error in retrieving the webpage.")
        exit()
    page_html = BeautifulSoup(request.content, 'html5lib')

    ingredients = page_html.find_all(class_="mntl-structured-ingredients__list-item")
    ingredient_list = []
    for i in ingredients:
        ingredient_list.append(i.getText())
    return ingredient_list

conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS test")

cursor.execute(""" CREATE TABLE IF NOT EXISTS test (link TEXT, ingredients TEXT); """)
conn.commit()

# getRecipeAllRecipes('squid')

# List of things to input into the database
meat_list = ['chicken', 'beef', 'steak', 'turkey', 'lamb', 'veal', 'pork', 'sausage', 'duck', 'goose', 'octopus', 'fish', 'salmon', 'tilapia', 'crab', 'lobsters', 'mussels', 'shrimp', 'prawns', 'oysters', 'scallops', 'clams']
vegetable_list = ['broccoli', 'carrots', 'asparagus', 'green beans', 'tomatoes', 'bok choy', 'broccolini', 'celery', 'corn', 'snap peas', 'peas', 'peppers', 'squash', 'brussel sprouts', 'cabbage', 'beet', 'cauliflower', 'chicory', 'cucumbers', 'zucchini', 'radish', 'lettuce', 'spinach', 'mushrooms', 'tomatillo']
fruit_list = ['mango', 'apple', 'orange', 'banana', 'grape', 'kiwi', 'cherry', 'avocado', 'grapefruit', 'pineapple', 'cranberry', 'berries', 'blueberries', 'strawberries', 'blackberries', 'apricot', 'peach', 'lemon', 'lime', 'pear', 'guava', 'plum', 'raspberry', 'pomegranate', 'watermelon']
spices_list = ['cinnamon', 'oregano', 'italian seasoning', 'basil', 'herbes de provence', 'chives', 'cilantro', 'dill', 'lemongrass', 'marjoram', 'green onion', 'parsley', 'garlic', 'onions', 'rosemary', 'sage', 'tarragon', 'thyme', 'mint', 'pepper', 'salt', 'clove', 'fenugreek', 'cardamom', 'allspice', 'paprika', 'mustard', 'caraway', 'star anise', 'fennel', 'ancho', 'red pepper flakes', 'coriander', 'mace', 'sumac', 'cumin', 'chili powder', 'tumeric', 'garam masala', 'nutmeg', 'cayenne', 'zest', 'chocolate']
types_of_cooking_styles_list = ['spatchcock', 'braising', 'stewing', 'pot roasting', 'barbecuing', 'smoking', 'pan sear', 'grilling', 'broiling', 'oven roast', 'stir frying', 'deep frying', 'shallow fry', 'fry', 'roast', 'bake']

for food in meat_list:
    getRecipeAllRecipes(food)

# for food in vegetable_list:
#     getRecipeAllRecipes(food)

# for food in fruit_list:
#     getRecipeAllRecipes(food)

# for food in spices_list:
#     getRecipeAllRecipes(food)

# for food in types_of_cooking_styles_list:
#     getRecipeAllRecipes(food)

cursor.execute('''INSERT INTO test VALUES (?, ?)''', ('actual_link', 'ingredient_str'))

cursor.execute('''SELECT * FROM test''')
results = cursor.fetchall()
print(results)

conn.close()