import scrapy
from pathlib import Path
import csv


class StockSpider(scrapy.Spider):
    name = 'stock_spider'
    allowed_domains = ["https://www.tradingview.com"]
    start_urls = ['https://www.tradingview.com/markets/world-stocks/worlds-largest-companies/']

    def start_requests(self):
        urls = [
            # "https://www.tradingview.com/markets/world-stocks/worlds-largest-companies/",
            "https://www.tradingview.com/symbols/NSE-CNX500/components/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        a = response.xpath('//tr/td')
        stock_name = a.xpath('span/sup/text()').extract()
        stock_code = a.xpath('span/a/text()').extract()
        stock_svg = a.xpath('span/img/@src').extract()
        #  stock_price_all = a.xpath('text()').extract() to extract the data of price, volume, market cap, circle supply, rank of the stock 

        # Replace occurrences of "tradingview" with "barterview" in SVG URLs
        stock_svg = [svg.replace("tradingview", "barterview") for svg in stock_svg]

        # Writing data to CSV file
        csv_file_path = 'test.csv'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['stock name', 'stock code', 'svg'])
            for name, code, svg in zip(stock_name, stock_code, stock_svg):
                writer.writerow([name, code, svg])
        
        self.log(f'Saved data to {csv_file_path}')
    


        #  stock_price = stock_price_all[2:]

        #  print('Stock Name:', stock_name)
        #  print('Stock Code:', stock_code)
        #  print('Stock SVG:', stock_svg)
        #  print('Stock Price:', stock_price)
        #  stock_rank = a.xpath('text()').extract()[:0]
        #  stock_price = a.xpath('text()').extract()[:1]
        #  stock_market_cap = a.xpath('text()').extract()[:2]
        #  stock_volume = a.xpath('text()').extract()[:3]
        #  stock_circle_supply = a.xpath('text()').extract()[:4]


        
        #  print(stock_code,stock_name,stock_svg,stock_volume,stock_rank,stock_price,stock_market_cap,stock_volume,stock_circle_supply)
         

        #  stock_price = stock_price_all[:6]
        #  print ("stock_name :", stock_name)
        #  print ("stock_code: ",stock_code)
        #  print ("stock_svg:",stock_svg)
        #  print ("stock_rank:",stock_rank)
        #  print ("stock_price:",stock_price)
        #  print ("stock_market_cap:",stock_market_cap)
        #  print ("stock_volume:",stock_volume)
        #  print ("stock_circle_supply:",stock_circle_supply)


        #  b = response.xpath('//tr')
        #  for i in b:
        #     stock_price = i.xpath('td/text').extract()
        #     print(stock_price)

        
        



    # def parse_stock(self, response):
    #     # Extracting data from individual stock pages
    #     stock_name = response.css('.apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat::text').get()
    #     stock_symbol = response.css('.tv-circle-logo-PsAlMQQF tv-circle-logo--xsmall-PsAlMQQF tickerLogo-GrtoTeat::text').get()
    #     stock_price = response.css('.cell-RLhfr_y4 right-RLhfr_y4::text').get()
    #     stock_high = response.css('.js-high::text').get()
    #     stock_volume = response.css('.cell-RLhfr_y4 right-RLhfr_y4::text').get()

    #     # Printing the extracted data
    #     print('Stock Name:', stock_name)
    #     print('Stock Symbol:', stock_symbol)
    #     print('Stock Price:', stock_price)
    #     print('Stock High:', stock_high)
    #     print('Stock Volume:', stock_volume)

    #     # Yielding the extracted data
    #     yield {
    #         'Stock Name': stock_name,
    #         'Stock Symbol': stock_symbol,
    #         'Stock Price': stock_price,
    #         'Stock High': stock_high,
    #         'Stock Volume': stock_volume,
    #     }
