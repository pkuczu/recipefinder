from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('recipes.sql')

def getRecipeAllRecipes(ingredient):
    # Get first page 
    url = "https://www.allrecipes.com/search?q=" + ingredient
    request = requests.get(url)
    if request.status_code != 200:
        print("Error in retrieving the webpage.")
        exit()
    page_html = BeautifulSoup(request.content, 'html5lib')

    links = page_html.find_all("a") # Find all elements with the tag <a>

    f = open("test.txt", "a")
    for link in links:
        if (link.get("href").find("https://www.allrecipes.com/recipe") != -1 and link.get("href").find("https://www.allrecipes.com/recipes/201") == -1 and link.get("href").find(ingredient) != -1):
            f.write(link.get("href"))
            f.write('\n')
    f.close()


    # Get all the pages after the first 

    num_repeat = len(page_html.find_all("a", class_="button--outlined-little-round type--rabbit-bold")) + 1
    print(num_repeat)

    for i in range(1, num_repeat):
        x = i * 24
        url = "https://www.allrecipes.com/search?" + ingredient + "=" + ingredient + "&" + "offset=" + str(x) + "&q=" + ingredient
        request = requests.get(url)
        if request.status_code != 200:
            print("Error in retrieving the webpage.")
            exit()
        page_html = BeautifulSoup(request.content, 'html5lib')

        links = page_html.find_all("a") # Find all elements with the tag <a>

        f = open("test.txt", "a")
        for link in links:
            if (link.get("href").find("https://www.allrecipes.com/recipe") != -1 and link.get("href").find("https://www.allrecipes.com/recipes/201") == -1 and link.get("href").find(ingredient) != -1):
                f.write(link.get("href"))
                f.write('\n')
        f.close()


getRecipeAllRecipes('chicken')
getRecipeAllRecipes('turkey')