import requests
from bs4 import BeautifulSoup


class WebScrappingHelper:
    @staticmethod
    def get_name_and_prices(keyword):
        url = f'https://listado.mercadolibre.com.ve/{keyword}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items_unclean = soup.find_all('li', class_="ui-search-layout__item")
        result = []

        for item in items_unclean:
            price = item.find('span', class_="andes-money-amount__fraction")
            name = item.find('h2', class_="ui-search-item__title")
            result.append({'name': name.text, 'price': price.text})

        return result
