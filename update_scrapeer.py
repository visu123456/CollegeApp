from turtle import up
import requests

from bs4 import BeautifulSoup




def give_data():
    updates_str = ""
    u = "https://www.gtu.ac.in/Circular.aspx"

    r = requests.get(u)
    pg_soup = BeautifulSoup(r.content,"html.parser")

    all_updates = pg_soup.find_all('ul',class_="timeline")

    for tb in all_updates:
        for updt in tb.find_all('div',class_="rows")[:5]:
            updates_str += str(updt)
    

    fl = open("Templates/gtu_data.html","w",encoding='utf-8')
    fl.write('<html>')
    fl.write(updates_str)
    fl.write("\n")
    fl.write('</html>')

    return updates_str



if __name__ == "__main__":
    give_data()