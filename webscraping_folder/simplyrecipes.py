from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('recipes.sql')

# current branch name: simplyRecipes

def getRecipeSimplyRecipes(ingredient):
    # Get first page 
    url = "https://www.simplyrecipes.com/search?q=" + ingredient
    request = requests.get(url)
    if request.status_code != 200:
        print("Error in retrieving the webpage.")
        exit()
    page_html = BeautifulSoup(request.content, 'html5lib')

    num_repeat = len(page_html.find_all("a", class_="pagination__item")) + 1

    for i in range(num_repeat):
        x = i * 24
        url = "https://www.simplyrecipes.com/search?q=" + ingredient + "&offset=" + str(x)
        if request.status_code != 200:
            print("Error in retrieving the webpage.")
            exit()
        page_html = BeautifulSoup(request.content, 'html5lib')

        links = page_html.find_all(class_="comp card") # Find all elements with the tag <a>

        f = open("test3.txt", "a")
        for link in links:
            if (link.get("href").find("https://www.simplyrecipes.com/") != -1 and link.get("href").find(ingredient) != -1):
                f.write(str(link.get("href")))
                f.write('\n')
            #getIngredientsAllRecipes(link.get("href"))
        f.close()

# def getIngredientsSimplyRecipes(url):
#     request = requests.get(url)
#     if request.status_code != 200:
#         print("Error in retrieving the webpage.")
#         exit()
#     page_html = BeautifulSoup(request.content, 'html5lib')

#     ingredients = page_html.find_all(class_="mntl-structured-ingredients__list-item")
#     f2 = open("test2.txt", "a")
#     for i in ingredients:
#         ingredient = str(i.getText())
#         f2.write(ingredient)
#     f2.write('\n')
#     f2.close

getRecipeSimplyRecipes('asian')