import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from pytaxonomies import Entry, Predicate, Taxonomy

CONTENT_URL = 'https://www.wada-ama.org/en/prohibited-list'

TAXONOMY_DESCRIPTION = 'This taxonomy aims to list doping substances'
TAXONOMY_EXPANDED = 'Doping substances'
TAXONOMY_NAME = 'doping-substances'

ignore = ('NON-APPROVED SUBSTANCES', )


def list_predicates(articles):
    predicates = {}
    for article in articles:
        title = article.find('p', attrs={'class': 'h3 panel-title'}).text
        if title in ignore:
            continue
        predicate = Predicate()
        predicate.predicate = title
        div = article.find('div', attrs={'class': 'layout-wysiwyg'})
        description = div.find('p')
        predicate.description = description.find_next_sibling().text
        predicates[title] = predicate
    return predicates


def generate_taxonomy():
    new_taxonomy = Taxonomy()

    new_taxonomy.name = TAXONOMY_NAME
    new_taxonomy.expanded = TAXONOMY_EXPANDED
    new_taxonomy.description = TAXONOMY_DESCRIPTION
    
    response = requests.get(CONTENT_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.findAll('article', attrs={'class': 'panel hide-reader'})
    
    new_taxonomy.predicates = list_predicates(articles)

    for article in articles:
        title = article.find('p', attrs={'class': 'h3 panel-title'}).text
        if title in ignore:
            continue
        products = article.findAll('li')
        products_list = {}
        for product in products:
            entry = Entry()
            entry.value = product.text
            products_list[entry.value] = entry
        new_taxonomy.predicates[title].entries = products_list

    return new_taxonomy


if __name__ == '__main__':
    taxonomy = generate_taxonomy()
    taxonomy.version = 2
    with open(Path(__file__).resolve().parent / 'machinetag.json', 'wt', encoding='utf-8') as f:
        json.dump(taxonomy.to_dict(), f, indent=2, ensure_ascii=False)
