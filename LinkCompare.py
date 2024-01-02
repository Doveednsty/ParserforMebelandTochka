from bs4 import BeautifulSoup
import requests

url = "https://dsv-mebel.ru/mebel/modulnaya-sistema-mori/"
i = 1
# Отправка запроса на сервер
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Получение HTML-кода страницы
    html = response.text

    # Инициализация BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, "html.parser")

    # Находим все элементы с классом "product"
    product_elements = soup.find_all("li", class_="product")

    # Извлекаем ссылки на товары
    product_links = [element.find("a")["href"] for element in product_elements]

    # Выводим найденные ссылки
    for link in product_links:
        print(link)
        i+=1
else:
    print("Ошибка при запросе:", response.status_code)
