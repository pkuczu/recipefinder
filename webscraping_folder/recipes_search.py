import sqlite3
from sqlite3 import Error

def search_ingredient(ingredient):      # returns a list of the recipes that have the ingredient
    conn = sqlite3.connect('recipes_test.db')
    cursor = conn.cursor()

    recipes_containing_ingredient = []

    cursor.execute('''SELECT name FROM test''')
    all_names = cursor.fetchall()
    # print(all_names)

    cursor.execute('''SELECT ingredients FROM test''')
    all_ingredients = cursor.fetchall()      # a string of all the ingredients together, comma separated
    # print(all_ingredients)

    ingredient = ingredient.lower()

    for i in range(len(all_names)):
        recipe_name = all_names[i]
        recipe_name = recipe_name[0]
        # recipe_name = recipe_name.replace('{', '').replace('}', '')

        ingredients_list = all_ingredients[i]

        ingredients_list = ingredients_list[0]
        # ingredients_list = ingredients_list.replace('{', '').replace('}', '')
        ingredients_list = ingredients_list.split(". ")

        for item in ingredients_list:
            # print(item)
            item_keywords = item.split()

            for keyword in item_keywords:
                keyword = keyword.replace(',', '')
                if keyword == ingredient:
                    recipes_containing_ingredient.append(recipe_name)
    
    # for ingredients_list in all_ingredients:
        # print(ingredients_list)
        # ingredients_listed = ingredients_list[0]
        # ingredients_listed = ingredients_listed.split(", ")
        
        # for item in ingredients_listed:
            # if (item == ingredient):
                # print(f"The ingredient {ingredient} was found in the recipe ")

    # print(ingredients)

    conn.close()

    return recipes_containing_ingredient

print(search_ingredient("butter"))

# conn = sqlite3.connect('recipes_test.db')
# cursor = conn.cursor()
# table_name = 'test'

# cursor.execute(f"PRAGMA table_info({table_name})")

# Fetch and print the column names
# column_names = [row[1] for row in cursor.fetchall()]
# print("Column names:")
# for name in column_names:
    # print(name)


# cursor.execute("SELECT link, ingredient FROM test")
# row_count = cursor.fetchone()[0]
# rows = cursor.fetchall()
# print(rows)
# print(f"Number of records: {row_count}")

# cursor.execute('''SELECT * from test''')

# results = cursor.fetchall()

# print(results)

# for result in results:
    # print(result)

print(search_ingredient("spinach"))
    