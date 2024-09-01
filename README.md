# Парсинг мобильных ОС с OZON
**Задача**:
<br>
скрипт для извлечения 100 самых популярных смартфонов на Ozon и составления рейтинга версий мобильных операционных систем.
<br><br>
**Сделано**:
1. Selenium на удалённом вебдрайвере от brightdata.com (Web Scraper API) - для перехода по страницам, прокрутки динамически загружаемого контента и извлечения ссылок на смартфоны.
2. Scrapy - для извлечения информации из страниц со смартфонами.
3. Pandas - для анализа полученных данных.
<br><br>

**Сборка проекта**:
<br><br>
устанавливаем зависимости из  <code>requirements.txt</code><br><br>
brightdata.com - вебдрайвер+прокси для парсинга. Бесплатный лимит ~ 0,5 Gb<br>
Создаём бесплатную учетную запись, в ней Scraping Browser,
в его настройках новую Zone, во вкладке Access parameters копируем username и password.<br><br>
<code>example_dotenv</code> переименовываем в  <code>.env</code> и прописываем username и password туда.<br><br>
<code>scrapy crawl ozon_spider</code> запускает парсинг и сохраняет его сводные результаты в <code>result.txt</code>
