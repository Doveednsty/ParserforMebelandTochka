import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получаем заголовок
    title = soup.find('h1', class_='product_title entry-title').text.strip()

    # Создаем директорию для сохранения изображений
    directory = title.replace(' ', '_')
    os.makedirs(directory, exist_ok=True)

    # Ищем все элементы с изображениями внутри карусели
    img_elements = soup.find_all('div', class_='woocommerce-product-gallery__image')

    for i, img_element in enumerate(img_elements):
        # Находим тег <a> с изображением
        a_tag = img_element.find('a')

        if a_tag:
            # Получаем ссылку на изображение из атрибута href
            img_url = urljoin(url, a_tag['href'])

            # Сохраняем изображение с именем "заголовок_номер"
            img_name = f'{title}_{i+1}.jpg'
            img_path = os.path.join(directory, img_name)

            # Скачиваем и сохраняем изображение
            img_data = requests.get(img_url).content
            with open(img_path, 'wb') as img_file:
                img_file.write(img_data)

            print(f'Сохранено изображение: {img_path}')
        else:
            print(f'Изображение не найдено в элементе {i+1}')

if __name__ == "__main__":
    # Замените URL на конкретный подкаталог, например, https://dsv-mebel.ru/mebel/category1
    with open("links.txt", "r") as file:
        for line in file:
            #url = "https://dsv-mebel.ru/mebel/category1"
            download_images(line)
