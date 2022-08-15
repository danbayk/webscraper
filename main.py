from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

DC = ["worcester.html", "berkshire.html", "franklin.html", "hampshire.html"]
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

# path = "C:\Program Files (x86)\chromedriver.exe"
# s = Service(path)
# driver = webdriver.Chrome(service=s)
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
for x in DC:
    # Local version of dining page
    with open(x) as temphtml:
        soup = BeautifulSoup(temphtml, "html.parser")

    if x == "worcester.html":
        currMenu = worcesterMenu
    elif x == "berkshire.html":
        currMenu = berkshireMenu
    elif x == "franklin.html":
        currMenu = franklinMenu
    elif x == "hampshire.html":
        currMenu = hampshireMenu

    countType = 0
    for placeholder in currMenu:
        elements = soup.find_all(id=menuType[countType])

        with open("%s" % placeholder, "w") as outfile:
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
        quoteCount = 0
        x = 0
        y = 0

        currCategory = ""
        currFood = ""

        with open("%s" % placeholder, "r") as f:
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
