import re
import scrapy
import douban_movie.items


def parse_by_xpath(response):
    print('xxx', parse_by_xpath)
    for each in response.xpath("//div[@class='item']"):
        item = douban_movie.items.DoubanMovieItem()
        item['name'] = each.xpath("./div[@class='info']/div/a/[span@class='title'/text()]").extract()
        print('xxx', item['name'])
        yield item

def trim_str(value):
	return re.sub(r'\s+', " ", str(value))

def trim_all(item):
    for i in item:
        item[i] = trim_str(item[i])

def trim_arr(arr):
    result = []
    for a in arr:
        a = trim_str(a)
        if len(a) > 0 and a != ' ' and a != ' / ':
            result.append(a)
    return result

def add_value(arr):
    va = ''
    for a in arr:
        val = trim_str(a)
        if val is not None and len(val) != 0:
            va += val
    return va

def get_value(dom, xpath):
    return add_value(dom.xpath(xpath).extract())

def get_arr_value(dom, xpath):
    return trim_arr(dom.xpath(xpath).extract())

class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    url = 'https://movie.douban.com/top250?start='
    offset = 0
    start_urls = [url + str(offset)]
    # start_urls = ['https://movie.douban.com/subject/1292052/']
    start_css = 'ol.grid_view div.item div.info '
    start_xpath = "//div[@id='wrapper']/div[@id='content']"

    def parse_detail(self, response):
        item = douban_movie.items.DoubanMovieItem()
        item['url'] = response.url

        dom = response.xpath(self.start_xpath)
        item['number'] = get_value(dom, "./div[@class='top250']/span[@class='top250-no']/text()")
        item['name'] = get_value(dom, "./h1/span[1]/text()")
        item['time'] = get_value(dom, "./h1/span[2]/text()")

        dom = dom.xpath("./div/div/div/div/div/div")
        item['director'] = get_value(dom, "./span[1]/span[@class='attrs']/a/text()")
        item['scenario'] = get_value(dom, "./span[2]/span[@class='attrs']/a/text()")
        item['starts'] = get_arr_value(dom, "./span[3]/span[2]/a/text()")
        item['type'] = get_arr_value(dom, "./span[@property='v:genre']/text()")
        desc_arr = get_arr_value(dom, './text()')
        item['district'] = desc_arr[0]
        item['language'] = desc_arr[1]
        item['time_desc'] = get_arr_value(dom, "./span[@property='v:initialReleaseDate']/text()")
        return item

    def parse(self, response):
        for each in response.xpath("//div[@class='item']"):
            url = get_value(each, "./div[@class='info']/div[@class='hd']/a/@href")
            yield scrapy.Request(url, callback=self.parse_detail)

        if self.offset < 225:
            self.offset += 25
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
        pass
