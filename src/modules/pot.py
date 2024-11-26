from bs4 import BeautifulSoup
import requests

# ta klasa ma za zadanie skrócenie kodu do pobierania stron

class pot:
    def __new__(cls, url: str, encoding_a: str=None): #
        try:
            print(f"Downloading {url}...")
            response = requests.get(url)
            if encoding_a:
                response.encoding = encoding_a
            else:
                print("Uwaga! Nie podano systemu kodowania. Domyślny: \033[3mutf-8\033[0m.")
                response.encoding = 'utf-8'
            response.raise_for_status()
            print(f"Downloaded {url}!")
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"Error downloading: {e}")
            raise
    
    # + jeszcze jest ta funkcja, chodzi w niej o to że bierze ona dict typu {"klucz": [wartość 1, wartość2]} generowaną przy scrapingu
    # i przekształca go w listę dictów: [{"klucz":wartość 1},{"klucz":wartość 2}]
    # może i dałoby się to ominąć ale jak działa to działa ¯\_(ツ)_/¯
    @staticmethod
    def zipify(d: dict):
        return [dict(zip(d.keys(), values)) for values in zip(*d.values())]
