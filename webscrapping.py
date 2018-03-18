__author__ = 'Joaquín Jiménez García'

from bs4 import BeautifulSoup
import requests

URL_BASE = "http://jarroba.com/"
MAX_PAGES = 20
counter = 0

for i in range(1, MAX_PAGES):
    if i > 1:
        url = "%spage/%d/" % (URL_BASE, i)
    else:
        url = URL_BASE

    req = requests.get(url)
    statusCode = req.status_code
    
    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

        for entrada in entradas:
            counter += 1
            titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
            autor = entrada.find('span', {'class': 'autor'}).getText()
            fecha = entrada.find('span', {'class': 'fecha'}).getText()

            print ("%d - %s  |  %s  |  %s" % (counter, titulo, autor, fecha))

    else:
        break