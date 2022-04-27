from bs4 import BeautifulSoup
import requests
import re

search_term = input("what graphic card do you want to search for? ")
url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

item_found = {   }

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")


    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))

    for item in items:
        parent = item.parent
        link = None
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_= "item-container")
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            item_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass



sorted_items = sorted(item_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['pride']}")
    print(item[1]['link'])
    print("------------------------------------------------------------")