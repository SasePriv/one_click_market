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
        total = 0
        max_price = float('-inf')
        min_price = float('inf')

        for item in items_unclean:
            price_element = item.find('span', class_="andes-money-amount__fraction")
            price = float(price_element.text) if price_element else 0.0
            name = item.find('h2', class_="ui-search-item__title").text
            image = item.find('img', class_="ui-search-result-image__element")['data-src']

            total += price

            max_price = max(max_price, price)
            min_price = min(min_price, price)

            result.append({"price": price, "name": name, "image": image})

        average_price = total / len(items_unclean) if len(items_unclean) > 0 else 0.0

        return {
            'list_items': result,
            'max_price': max_price,
            'min_price': min_price,
            'average_price': average_price
        }
