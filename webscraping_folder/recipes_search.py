import sqlite3
from sqlite3 import Error

def removeCharacters(my_string):        # want to remove ()
    to_return = ""

    for char in my_string:
        # if char == "'":
            # continue
        if char == "(":
            continue
        if char == ")":
            continue

        to_return += char

    return to_return

def search_ingredient(ingredient):      # returns a list of the recipes that have the ingredient
    conn = sqlite3.connect('recipes_test.db')
    cursor = conn.cursor()

    recipes_containing_ingredient = []

    # cursor.execute('''SELECT * FROM test''')
    # results = cursor.fetchall()
    # print(f"Results: {results}")

    # cursor.execute('''SELECT name FROM test''')
    # all_names = cursor.fetchall()

    cursor.execute('''SELECT ingredients FROM test''')
    all_ingredients = cursor.fetchall()      # a string of all the ingredients together, comma separated

    cursor.execute('''SELECT link FROM test''')
    all_links = cursor.fetchall()

    # ingredient = ingredient.lower()

    for i in range(len(all_links)):
        # recipe_name = all_names[i]
        # recipe_name = recipe_name[0]

        link = removeCharacters(all_links[i])
        # print(f"Link: {link}")

        ingredients_list = removeCharacters(all_ingredients[i])

        # print(f"Ingredients list: {ingredients_list}")

        # ingredients_list = ingredients_list[0]
        ingredients_list = ingredients_list.split(". ")

        for item in ingredients_list:
            item_keywords = item.split()

            for keyword in item_keywords:
                keyword = keyword.replace(',', '')
                if keyword == ingredient:
                    # recipes_containing_ingredient.append(f"{recipe_name}: {link}")
                    # recipes_containing_ingredient.append(recipe_name)
                    recipes_containing_ingredient.append(link)

    conn.close()

    return recipes_containing_ingredient

# print(search_ingredient("butter"))
print(search_ingredient("squid"))
print(search_ingredient("paprika"))

# print(search_ingredient("spinach"))