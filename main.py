# coding: utf-8
import urllib
from bs4 import BeautifulSoup
import urllib.request

if __name__ == '__main__':
    pageDeDepart='https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
    with urllib.request.urlopen(pageDeDepart) as response:
        print(pageDeDepart)
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        pageDeDepart = soup.select("[rel='canonical']")[0]['href']
        for a in soup.select('.mw-parser-output p a'):

            print(a['href'])
