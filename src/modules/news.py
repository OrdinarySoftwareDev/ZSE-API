from modules.pot import *

def run():
    url = "https://zse.bydgoszcz.pl"

    data = {
        "headline" : [],
        "description" : [],
        "date" : [],
        "url" : []
    }

    soup = pot(url=url)
    
    card_headers = soup.find_all("h5",class_="card-header")

    wazne = None

    for header in card_headers:
        if header.text == "Ważne":
            wazne = header.find_parent("div")
            break

    if wazne == None:
        print("Important news segment wasn't found.")
    else:
        smalls = wazne.find_all("small")

        for i,s in enumerate(smalls):
            a = wazne.find_all("a")[i]
            data["date"].append(s.text.replace("Publikacja: ","").split(",")[0])
            data["description"] += ""
            data["headline"].append(a.text.strip())
            data["url"].append(f"{url}/{a.get('href')}")

    news_container = soup.find("div",class_=["col-lg-9","col-xl-8"])

    for h3 in news_container.find_all("h3"):
        data["headline"].append(h3.text)
        data["date"] += ""
    for p in news_container.find_all("p"):
        data["description"].append(p.text.strip())

    for a in news_container.find_all("a",class_=["btn","bnt_primary"]):
        data["url"].append(f"{url}/{a.get('href')}")

    return data