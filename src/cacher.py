from modules.pot import *

from datetime import datetime, timedelta
import json
import re
import os


# linki do planów dla wszystkich klas, i nauczycieli
# wygląda to mniej więcej tak: "sid" : link
group_hrefs = {} 

# ta funkcja upraszcza pełne nazwy sal, klas i nauczycieli po to, że będzie łatwiej się do nich odnosić w linku
# np. zamiast /plan/1A 1A Ivy wystarczy dać /plan/1A
# albo zamiast /plan/M.Chabowski (Ch) wystarczy /plan/Ch
# ten skrócony identyfikator to 'sid'
def simplify_name(s):
    match = re.search(r'\((.{2})\)', s)
    if match:
        return match.group(1)
    else:
        return s.split()[0]
        

# find_hrefs znajduje sid do każdego linku
def find_hrefs(url):
    soup = pot(url=url)

    a_elements = [li.find("a") for li in soup.find_all("li")]

    for a in a_elements:
        name = a.text
        sid = simplify_name(name)

        href = f"{url.split('/l')[0]}/{a.get('href')}"

        group_hrefs[sid] = href

find_hrefs("https://plan.zse.bydgoszcz.pl/lista.html")

with open("./cache/group_hrefs.json","w+") as f:
    json.dump(group_hrefs,f)
