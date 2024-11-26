from modules.pot import *

def parse_lesson_data(unit,info_obj):
    lesson_name = unit.text

    check = lambda x: x.text if x else None

    if info_obj:
        teacher = info_obj.find("a", class_="n")
        teacher = check(teacher)

        room = info_obj.find("a", class_="s")
        room = check(room)

        sid = info_obj.find("a", class_="o")
        sid = check(sid)

    return {"name": lesson_name, "teacher": teacher, "room": room, "sid": sid}

def run(url):
    soup = pot(url=url)

    data = [[] for _ in range(5)]

    seeds = soup.find_all("td",class_="nr")

    for seed in seeds:
        tr = seed.find_parent("tr")
        cells = tr.find_all("td") # to wygląda mniej więcej jak: nr lekcji, czas startu-czas końcowy, lekcje o tej godzinie

        for c in range(2,len(cells)):
            cell = cells[c]
            spans = cell.find_all("span",class_="p")
            
            hour_data = []

            if spans:
                for span in spans:
                    hour_data.append(parse_lesson_data(span, cell))
            else:
                if cell.text.strip() != "":
                    hour_data.append(parse_lesson_data(cell, cell))
                else:
                    hour_data.append({})
                
            data[c-2].append(hour_data)
            
            


    return data
