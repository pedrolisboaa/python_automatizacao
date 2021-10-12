import requests
from bs4 import BeautifulSoup


def pegar_todos_valores_da_pagina(site):
    response = requests.get(site)
    html = BeautifulSoup(response.text, 'html.parser')

    for anuncio in html.select(".ui-search-result__content"):
        titulo = anuncio.select_one('h2')
        preco = anuncio.select_one('.price-tag-fraction')

        with open('preco_produto.txt', 'a+') as file:
            file.write(f'{preco.text} - {titulo.text}\n')

