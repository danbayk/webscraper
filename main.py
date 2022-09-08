from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

DC = ["worcester.html", "berkshire.html", "franklin.html", "hampshire.html"]
urls = ["https://umassdining.com/locations-menus/worcester/menu",
        "https://umassdining.com/locations-menus/berkshire/menu",
        "https://umassdining.com/locations-menus/franklin/menu",
        "https://umassdining.com/locations-menus/hampshire/menu"]

worcesterMenu = ["worcesterbreakfast.txt",
                 "worcesterlunch.txt",
                 "worcesterdinner.txt"]

berkshireMenu = ["berkshirebreakfast.txt",
                 "berkshirelunch.txt",
                 "berkshiredinner.txt"]

franklinMenu = ["franklinbreakfast.txt", "franklinlunch.txt", "franklindinner.txt"]

hampshireMenu = ["hampshirebreakfast.txt", "hampshirelunch.txt", "hampshiredinner.txt"]

menuType = ["breakfast_menu", "lunch_menu", "dinner_menu"]

currMenu = []
url = "https://umassdining.com/locations-menus/worcester/menu"

path = "C:\Program Files (x86)\chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service=s)
# driver.get(url)

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
itemCount = 0
worcesterBreakfast = []
worcesterLunch = []
worcesterDinner = []
berkshireBreakfast = []
berkshireLunch = []
berkshireDinner = []
franklinBreakfast = []
franklinLunch = []
franklinDinner = []
hampshireBreakfast = []
hampshireLunch = []
hampshireDinner = []
finalFoodItems = [worcesterBreakfast, worcesterLunch, worcesterDinner, berkshireBreakfast, berkshireLunch,
                  berkshireDinner, franklinBreakfast, franklinLunch, franklinDinner, hampshireBreakfast, hampshireLunch,
                  hampshireDinner]
page_sources = []
for x in urls:
    driver.get(x)
    html = driver.page_source
    page_sources.append(html)

cc = 0
for x in page_sources:
    #with open(x) as temphtml:
    soup = BeautifulSoup(x, "html.parser")
    if cc == 0:
        currMenu = worcesterMenu
    elif cc == 1:
        currMenu = berkshireMenu
    elif cc == 2:
        currMenu = franklinMenu
    elif cc == 3:
        currMenu = hampshireMenu
    cc += 1

    countType = 0
    for hall in currMenu:
        elements = soup.find_all(id=menuType[countType])

        with open("%s" % hall, "w") as outfile:
            for item in elements:
                outfile.write("%s\n" % item)

        outfile.close()

        countType += 1

        itemTag = "data-dish-name="
        titleTag = "menu_category_name\">"
        currentStr = ""
        currentFoodStr = ""
        currentTitleStr = ""
        currentTitle = ""
        currCategory = ""
        currFood = ""
        quoteCount = 0
        x = 0
        y = 0

        with open("%s" % hall, "r") as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                # Search for titleTag ---> >= 20
                if y < 20:
                    currentTitleStr = currentTitleStr + c
                    if currentTitleStr[y] == titleTag[y]:
                        y += 1
                    else:
                        currentTitleStr = ""
                        y = 0
                # Search for itemTag ---> >= 15
                if x < 15:
                    currentStr = currentStr + c
                    if currentStr[x] == itemTag[x]:
                        x += 1
                    else:
                        currentStr = ""
                        x = 0
                # Get text after titleTag
                if y >= 20:
                    if c != "<":
                        currentTitle = currentTitle + c
                    else:
                        currCategory = currentTitle.replace(">", "")
                        # Everytime a title is found, new list is created within finalFoodItems
                        finalFoodItems[itemCount].append([currCategory])
                        currentTitleStr = ""
                        currentTitle = ""
                        y = 0
                # Get text after itemTag
                if x >= 15:
                    if (c == "\""):
                        quoteCount += 1
                    if quoteCount < 2:
                        currentFoodStr = currentFoodStr + c
                    else:
                        finalFoodItems[itemCount][finalFoodItems[itemCount].__len__() - 1].append(
                            currentFoodStr.replace("=\"", ""))
                        currentFoodStr = ""
                        quoteCount = 0
                        currentStr = ""
                        x = 0
            itemCount += 1
            f.close()

for x in finalFoodItems:
    print(x)
