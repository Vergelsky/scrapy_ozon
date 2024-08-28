import sys
from time import sleep

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv('.env')
AUTH = f'{os.getenv('BRINGDATA_AUTH_LOGIN')}:{os.getenv('BRINGDATA_AUTH_PASSWORD')}'
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'

OZON_URL_START = 'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?page='
OZON_URL_END = '&sorting=rating'

def get_smartphones_urls(qty_smartphones):
    """
    Возвращает список ссылок на смартфоны в порядке убывания рейтинга. Обходит блокировку на странице каталога.
    Используется удалённый webDriver https://brightdata.com/ со встроенным прокси.
    :param qty_smartphones: количество ссылок
    :return:
    """

    page_number = 1
    urls = []
    get_url_succefull = False

    while not get_url_succefull:
        try:
            print('Подключаемся к удалённому браузеру...')
            sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
            with (Remote(sbr_connection, options=ChromeOptions()) as driver):
                print('Подключились! Переходим на страницу...')
                driver.get(OZON_URL_START + str(page_number) + OZON_URL_END)
                print("Страница загружается...")
                sleep(1)
                h1 = driver.find_elements(By.XPATH, "//h1")[0].text
                print("Получили заголовок", h1)
                if h1 == 'Доступ ограничен':
                    raise PermissionError('"Доступ ограничен"\n')
                get_url_succefull = True
                print('Успешно загрузили сайт')
                while True:
                    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
                    sleep(2)
                    elements = driver.find_elements(By.XPATH, "//font[text()='Смартфон']/"
                                                              "parent::span/parent::div/preceding-sibling::a")

                    for element in elements:
                        force_link = '/?oos_search=false'
                        url = element.get_attribute("href")
                        sys.stdout.write(f'\rИзвлекаем очередной url: {url[28:108]}...{url[-10:]}')
                        sys.stdout.flush()
                        url_head = url[:url.rfind('/')]
                        url_final = url_head + force_link
                        urls.append(url_final)
                        if len(urls) >= qty_smartphones:
                            print('\nСписок ссылок сформирован')
                            return urls
                    print('\nПросмотрено страниц: ', page_number)
                    print('Найдено смартфонов на этой странице и всего: ', len(elements), len(urls))
                    page_number += 3
                    driver.get(OZON_URL_START + str(page_number) + OZON_URL_END)
        except Exception as e:
            print("Ошибка: ", e)
            sleep(1)
