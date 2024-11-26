from modules.pot import *

def run():
    soup = pot(url="https://zastepstwa.zse.bydgoszcz.pl", encoding_a="iso-8859-2")

    zastepstwa = soup.find_all("td")
    kl_2i = {
        "id" : [],
        "info" : [],
        "teacher" : [],
        "substitute" : [],
        "comment" : []
    }

    for td in zastepstwa:
        if td.text.strip().find("2 I")>=0:
            tr = td.find_parent("tr")
            tds = tr.find_all("td")
            
            og_nauczyciel = td

            while og_nauczyciel:
                og_nauczyciel = og_nauczyciel.find_previous('td')
                if og_nauczyciel and 'st1' in og_nauczyciel.get('class', []):
                    break

            values = [
                tds[0].text,
                tds[1].text,
                og_nauczyciel.text,
                tds[2].text,
                tds[3].text
            ]

            for i,key in enumerate(kl_2i):
                kl_2i[key].append(values[i].strip())

    return kl_2i