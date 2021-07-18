from bs4 import BeautifulSoup
import requests

def GetRecipeByUrl(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')

    match = soup.findAll('span', class_="mcui mcui-Crafting_Table pixel-image")

    if match is None:
        match = soup.findAll('div',class_="mcui mcui-Crafting_Table pixel-image")

        if match is None:

            return {"status":"itemdoesntexist","url":url}

    if len(match) == 1:

        fullrecipe = []
        rows = match[0].findAll('tr', class_="mcui-row")
        itemTitle = soup.find('h1',id="firstHeading").text

        for i, row in enumerate(rows):

            items = row.findAll('td')

            for j, item in enumerate(items):
                if item.span.span:
                    title = item.span.span['data-minetip-title']
                    anchors = item.findAll('a')

                    if len(item.span.span) >= 3:
                        amount = item.span.span.findAll('a')

                        fullrecipe.append({"row": i + 1, "column": j + 1, "name": title[title.find("&") + 2:], "amount": int(amount[1].span.text)})



                    else:

                        fullrecipe.append({"row": i + 1, "column": j + 1, "name": title[title.find("&") + 2:],"amount": 1})
                else:
                    fullrecipe.append(({"row":i + 1,"column": j + 1,"name":"none","amount":0}))

                        # item.span.span['a'][1]


        return {"status": "success", "item": itemTitle.rstrip().lstrip(), "recipe": fullrecipe,'set':False}

    elif len(match) > 1:
        allRecipes = []
        for i, recipes in enumerate(match):


            fullTitle = recipes.find('span',class_="mcui-output").span.span['data-minetip-title']
            fullrecipe = []
            rows = recipes.findAll('tr',class_="mcui-row")
            for j, row in enumerate(rows):

                items = row.findAll('td')

                for k, item in enumerate(items):
                    if item.span.span:
                        title = item.span.span['data-minetip-title']
                        anchors = item.findAll('a')

                        if len(item.span.span) >= 3:
                            amount = item.span.span.findAll('a')
                            fullrecipe.append({"row": j + 1, "column": k + 1, "name": title[title.find("&") + 2:],"amount": int(amount[1].span.text)})
                        else:
                            fullrecipe.append(
                                {"row": j + 1, "column": k + 1, "name": title[title.find("&") + 2:], "amount": 1})
                    else:
                        fullrecipe.append(({"row": j + 1, "column": k + 1, "name": "none", "amount": 0}))
            allRecipes.append({"item":fullTitle[fullTitle.find("&") + 2:],"recipe":fullrecipe})

        return {'status':'success','set':True,"recipes":allRecipes,}
    else:
        return {"status":"itemdoesntexist","url":url}

def GetRecipeByName(name):
    req = requests.get("https://hypixel-skyblock.fandom.com/"+name)