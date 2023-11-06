import sqlite3
from sqlite3 import Error

def search_ingredient(ingredient):
    conn = sqlite3.connect('recipes_test.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT ingredients FROM test''')
    ingredients = cursor.fetchall()      # a string of all the ingredients together
    print(ingredient)

    conn.close()

conn = sqlite3.connect('recipes_test.db')
cursor = conn.cursor()
table_name = 'test'

cursor.execute(f"PRAGMA table_info({table_name})")

# Fetch and print the column names
column_names = [row[1] for row in cursor.fetchall()]
print("Column names:")
for name in column_names:
    print(name)


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

search_ingredient("hello")
    