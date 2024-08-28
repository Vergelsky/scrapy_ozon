import scrapy
import pandas


from ozon_scrapper.services import get_smartphones_urls


class OzonSpider(scrapy.Spider):
    def __init__(self):
        super().__init__()
        self.o_systems = []

    name = "ozon_spider"
    start_urls = get_smartphones_urls(100)

    def parse(self, response):
        os = response.xpath('//dt[span[contains(text(), "Операционная система")]]'
                            '/following-sibling::dd/a/text()').get()
        if os:
            o_system = response.xpath(f'//dt[span[contains(text(), "Версия {os}")]]'
                                        f'/following-sibling::dd/a/text()').get()
            if not o_system:
                o_system = response.xpath(f'//dt[span[contains(text(), "Версия {os}")]]'
                                          f'/following-sibling::dd/text()').get()

            if o_system:
                self.o_systems.append(o_system)
            else:
                self.o_systems.append(os + ' без версии')
        else:
            self.o_systems.append('система не указана')

    def close(self):
        df = pandas.DataFrame(self.o_systems)
        with open('results.txt', 'w', encoding='utf-8') as file:
            file.write(df.value_counts().to_string())
