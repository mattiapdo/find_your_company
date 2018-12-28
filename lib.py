from bs4 import BeautifulSoup
import requests


def parse_page(url):
    new_companies = list()
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    for card in soup.find_all('div', attrs= {"class":'card'}):
        info = {}
        if (card.get_text() != ""):
            try:
                info["Name"] = card.find_all('a')[0].get_text()
                info["Website"] = card.find_all('a')[1].get_text()
                info["Description"] = card.find_all('p', attrs = {"class": "text-left card_description"})[0].get_text()
                info["Location"] = card.find_all('p')[2].get_text()
                new_companies.append(info)
            except:
                print("\tCannot store info regarding", info["Name"])
                
    return(new_companies)