# branch name: sql_python

import sqlite3
from sqlite3 import Error
 
conn = sqlite3.connect('recipes_test.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS test")

#Creating table as per requirement
# sql = """ CREATE TABLE IF NOT EXISTS test (
#                                     name TEXT,
#                                     link TEXT,
#                                     ingredients TEXT,
#                                 ); """
cursor.execute(""" CREATE TABLE IF NOT EXISTS test (link TEXT, ingredients TEXT); """)
conn.commit()


ingredients = ['2 tablespoons peanut oil, divided', '1  shallot, finely chopped', '¼  white onion, chopped', '2 tablespoons butter', '1 tablespoon ginger garlic paste', '2 teaspoons lemon juice', '2 teaspoons garam masala, divided', '1 teaspoon chili powder', '1 teaspoon ground cumin']
ingredient_str = ''
for x in ingredients:
    ingredient_str += ". " + x

cursor.execute('''INSERT INTO test VALUES (?, ?)''', ("https://www.allrecipes.com/recipe/45957/chicken-makhani-indian-butter-chicken/", ingredient_str))

cursor.execute('''SELECT * FROM test''')
results = cursor.fetchall()
print(results)

conn.close()