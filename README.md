# scrapy_ozon
Парсинг списка смартфонов на Ozon и составление из него рейтинга мобильных операционных систем
<br><br>
устанавливаем зависимости из  <code>requirements.txt</code><br><br><br>
brightdata.com - вебдрайвер+прокси для парсинга. Бесплатный лимит ~ 0,5 Gb<br>
Создаём бесплатную учетную запись, в ней Scraping Browser,
в его настройках новую Zone, во вкладке Access parameters копируем username и password.<br>
<code>example_dotenv</code> переименовываем в  <code>.env</code> и прописываем username и password туда.<br><br>
<code>scrapy crawl ozon_spider</code> запускает парсинг и сохраняет его сводные результаты в <code>result.txt</code>
