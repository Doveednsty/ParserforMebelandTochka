import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def extract_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получаем заголовок
    title = soup.find('h1', class_='product_title entry-title').text.strip()

    # Ищем все элементы с изображениями внутри карусели
    img_elements = soup.find_all('div', class_='woocommerce-product-gallery__image')

    # Создаем список для хранения данных о продукте
    product_data = []

    for i, img_element in enumerate(img_elements):
        # Находим тег <a> с изображением
        a_tag = img_element.find('a')

        if a_tag:
            # Получаем ссылку на изображение из атрибута href
            img_url = urljoin(url, a_tag['href'])

            # Добавляем данные о продукте в список
            product_data.append({
                'SKU': title,
                'Category': '',  # Добавьте категорию, если она доступна на странице
                'Title': title,
                'Description': '',  # Добавьте описание, если оно доступно на странице
                'Text': '',  # Добавьте текст, если он доступен на странице
                'Photo': img_url,
                'Price': '',  # Добавьте цену, если она доступна на странице
                'Quantity': '',  # Добавьте количество, если оно доступно на странице
                'Price Old': '',  # Добавьте старую цену, если она доступна на странице
                'Editions': '',  # Добавьте редакции, если они доступны на странице
                'Modifications': '',  # Добавьте модификации, если они доступны на странице
                'External ID': '',  # Добавьте внешний идентификатор, если он доступен на странице
                'Parent UID': ''  # Добавьте родительский UID, если он доступен на странице
            })

    return product_data

if __name__ == "__main__":
    # Создаем CSV файл
    csv_file_path = "products_data.csv"
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['SKU', 'Category', 'Title', 'Description', 'Text', 'Photo', 'Price', 'Quantity', 'Price Old', 'Editions', 'Modifications', 'External ID', 'Parent UID']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Замените URL на конкретный подкаталог, например, https://dsv-mebel.ru/mebel/category1
        with open("links.txt", "r") as file:
            for line in file:
                product_data = extract_product_data(line)

                # Записываем данные в CSV файл
                csv_writer.writerows(product_data)

    print(f'Данные сохранены в CSV файл: {csv_file_path}')
