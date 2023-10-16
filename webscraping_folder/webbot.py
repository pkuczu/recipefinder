from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('recipes.sql')

# request = requests.get("https://www.allrecipes.com/search?q=chicken") # Example with chicken
# if request.status_code != 200:
#     print("Error in retrieving the webpage.")
#     exit()
# page_html = BeautifulSoup(request.content, 'html5lib')

# links = page_html.find_all("a") # Find all elements with the tag <a>

# f = open("test.txt", "a")
# for link in links:
#     if (link.get("href").find("https://www.allrecipes.com/recipe") != -1 and link.get("href").find("https://www.allrecipes.com/recipe/201") == -1 and link.get("href").find("chicken") != -1):
#         f.write(link.get("href"))
#         f.write('\n')
# f.close()

def getRecipeAllRecipes(ingredient):
    url = "https://www.allrecipes.com/search?q=" + ingredient
    request = requests.get(url)
    if request.status_code != 200:
        print("Error in retrieving the webpage.")
        exit()
    page_html = BeautifulSoup(request.content, 'html5lib')

    links = page_html.find_all("a") # Find all elements with the tag <a>

    f = open("test.txt", "a")
    for link in links:
        if (link.get("href").find("https://www.allrecipes.com/recipe") != -1 and link.get("href").find("https://www.allrecipes.com/recipe/201") == -1 and link.get("href").find(ingredient) != -1):
            f.write(link.get("href"))
            f.write('\n')
    f.close()

getRecipeAllRecipes('chicken')
getRecipeAllRecipes('turkey')