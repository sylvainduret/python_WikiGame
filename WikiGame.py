# !/usr/bin/env python
# coding: utf-8
import sys
from bs4 import BeautifulSoup
import urllib.request
import os


def Recherche(url):
    Lien_Page = []
    with urllib.request.urlopen(url) as response:
        Page = response.read()  # Crée une chaine de caractère avec tout le code source
        soup = BeautifulSoup(Page, 'html.parser')
        for test in soup.find_all('h1', {"class": "firstHeading"}):  # extraction titre de la page
            titre = str(test.contents[0])
            # S'il y a des exposants
            if 'abbr' in str(test.contents[0]):
                titre = str(test.contents[0].contents[0]) + str(test.contents[0].contents[1].contents[0]) + str(
                    test.contents[1])

            titre = titre.replace("<i>", "").replace("</i>", "").replace("<span>", "").replace("</span>", "")  # TODO gerer le bug du <span>
            Lien_Page.append(titre)

        for anchor in soup.find_all('div', {"class": "mw-parser-output"}):
            for link in anchor.find_all('a'):
                txt = Formatage_Utilisateur(str(link.get('href')))
                if not ('/w/') in txt:
                    if not ('#') in txt:
                        if not ('Fichier:') in txt:
                            if not ('http:') in txt:
                                if not ('https:') in txt:
                                    if not ('Modèle:') in txt:
                                        if not ('/API') in txt:
                                            if not ('Spécial:') in txt:
                                                if not ('Catégorie:') in txt:
                                                    if not ('/wiki/:') in txt:
                                                        if not ('Aide:') in txt:
                                                            if not ('Wikipédia:') in txt:
                                                                if not ('Portail:') in txt:
                                                                    if not ('Projet:') in txt:
                                                                        Lien_Page.append(txt.replace("/wiki/",
                                                                                                     ""))  # on ajoute tout les liens qui sont "propres" et on enleve les "/wiki/" pour clarifier les liens
        return Lien_Page


def Formatage_Utilisateur(txt):
    return txt.replace("%20", " ").replace("%27", "'").replace("%C3%A8", "è").replace("%C3%A9", "é").replace('%C3%AA', 'ê')\
        .replace("%C3%A2", "â").replace("%C5%93", "œ").replace("%C3%B", 'ü').replace("%C3%AC", "ì").replace('%C3%A7', 'ç')\
        .replace('%C3%A0', 'à').replace('%C3%B4', 'ô').replace('%C3%89', 'É').replace("%C3%AF", "ï").replace("%C3%BB", "û")\
        .replace("%C3%AE", "î").replace("%C3%A4", "ä")


def Formatage_Url(txt):
    return txt.replace(" ", "%20").replace("'", "%27").replace("è", "%C3%A8").replace("é", "%C3%A9").replace('ê','%C3%AA')\
        .replace("â", "%C3%A2").replace("œ", "%C5%93").replace('ü', "%C3%B").replace("ì", "%C3%AC").replace('ç','%C3%A7')\
        .replace('à', '%C3%A0').replace('ô', '%C3%B4').replace('É', '%C3%89').replace("ï", "%C3%AF").replace("û","%C3%BB")\
        .replace("î", "%C3%AE").replace("ä", "%C3%A4")


def Affiche_Tableau(tab, debut, fin):
    i = 1
    for indice in range(debut, fin):  # Génère la "liste" grace au tableau
        print('{} - {}'.format(indice, tab[indice]).replace("_", " "))
        i += 1


def Rafraichissement_Ecran():  # clean l'écran en fonction de l'OS
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    victoire = False
    Page_Actuel = Recherche('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
    PageFin = Recherche('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
    origine = Page_Actuel[0]
    Compteur_Tour = 0
    page = 1
    Ancienne_Page = ""
    try:
        while not victoire:
            debut = ((page - 1) * 20) + 1
            fin = debut + 20
            print('Projet Python WIKIGAME! *** tour {}'.format(Compteur_Tour))
            print('Départ :{}'.format(origine).replace("_", " "))
            print('Cible : {}'.format(PageFin[0]).replace("_", " "))
            print('Actuellement : {}'.format(Page_Actuel[0]).replace("_", " "))
            print('0 - Retour /')
            Affiche_Tableau(Page_Actuel, max(1, debut), min(fin, len(Page_Actuel)))
            print('998 - Les liens précédents /')
            print('999 - Voir la suite /')
            nouvelle_Page = int(input('Votre choix : '))
            if nouvelle_Page == 998 or nouvelle_Page == 999 or nouvelle_Page > len(Page_Actuel):
                if nouvelle_Page == 999:
                    if fin < len(Page_Actuel):
                        page += 1
                elif nouvelle_Page == 998:
                    if debut > 1:
                        page -= 1
                else:
                    print('Il n\'y a pas de lien pour ce numéro')
            else:
                if nouvelle_Page == 0:
                    if Compteur_Tour == 0:
                        print("Retour impossible lors du premier tour")
                    else:
                        Page_Actuel = Recherche('https://fr.wikipedia.org/wiki/{}'.format(Ancienne_Page))

                else:
                    # si le choix est de 60 et qu'on ne remet pas page a 1
                    # alors affichage des resultats suivant a partir de 60
                    page = 1
                    # reformatage pour repasser dans l'URL
                    Ancienne_Page = Formatage_Url(Page_Actuel[0])
                    link = 'https://fr.wikipedia.org/wiki/{}'.format(Formatage_Url(Page_Actuel[nouvelle_Page]))
                    Page_Actuel = Recherche(
                        'https://fr.wikipedia.org/wiki/{}'.format(Formatage_Url(Page_Actuel[nouvelle_Page])))
                    Compteur_Tour += 1
                    Rafraichissement_Ecran()

            if Page_Actuel[0] == PageFin[0]:
                victoire = True
                print('Bien joué en seulement {} coups'.format(Compteur_Tour))

    except:
        input('Erreur veuillez relancer le jeu et ne rentrer que des nombres')
        exit(1)
