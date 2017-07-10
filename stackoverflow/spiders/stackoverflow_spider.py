import scrapy
from stackoverflow.items import StackoverflowItem


class StackoverflowSpider(scrapy.Spider):

    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]

    def start_requests(self):

        urls = ['https://stackoverflow.com/questions/tagged/android?page={page}&sort=votes&pagesize=50'.format(page=page)
                for page in range(1, 10000)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

            # add code extraction
            #0th-order link list on search page
   
        link_base = 'https://stackoverflow.com'
        link_addon_list = response.xpath('//a[@class="question-hyperlink"]/@href').extract()

        items = [] # used to save all info collected


        for link_addon in link_addon_list:
            item = StackoverflowItem()
            #the link to open the project page
            link_level0 = (link_base + link_addon).encode('utf-8')
            request = scrapy.Request(link_level0, callback=self.parse_nextlevel)
            request.meta['items'] = items
            yield request

    #1st-order link list on project
    def parse_nextlevel(self, response):
        items = response.meta['items']
        item = StackoverflowItem()
        #item['code'] = response.body
        item['code_accepted'] = response.xpath('//div[@class="answer accepted-answer"]/*//code/text()').extract()
        print item['code_accepted']
        print '########################################'
        yield item #sending array 'items' into the pipeline


"""
        for index in range(1, 50):
            sel = response.xpath('//*[@id="questions"]/div[{index}]'.format(index=index))
            item = StackoverflowItem()
            item['votes'] = sel.xpath('div[1]/div[2]/div[1]/div[1]/span/strong/text()').extract()
            item['answers'] = sel.xpath('div[1]/div[2]/div[2]/strong/text()').extract()
            item['views'] = "".join(sel.xpath('div[1]/div[3]/@title').extract()).split()[0].replace(",", "")
            item['questions'] = sel.xpath('div[2]/h3/a/text()').extract()
            item['links'] = "".join(sel.xpath('div[2]/h3/a/@href').extract()).split("/")[2]
            item['tags'] = sel.xpath('div[2]/div[2]/a/text()').extract()

"""

"""    #fetch the code, create new item and append the new item to items
    def parse_fetchcode(self, response):
        items = response.meta['items']
        linkstr = response.meta['linkstr']
        item = GithubspiderItem()
        if (len(items)==0):
            item['idd'] = "1"
        else:
            item['idd'] = str(int(items[-1]['idd']) + 1)
        item['link'] = linkstr
        item['code'] = response.body
        #yield item
        items.append(item)
"""
           
