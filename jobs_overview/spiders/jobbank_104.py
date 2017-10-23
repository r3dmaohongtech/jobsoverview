import scrapy
#from bs4 import BeautifulSoup
import json
import requests
from scrapy.spider import BaseSpider
from jobs_overview.items import JobsOverviewItem

class Spider104(BaseSpider):
    name = 'jobbank_104'
    
    #url_part1 = 'https://www.104.com.tw/jobs/search/list?ro=0&keyword=%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B7%A5%E7%A8%8B%E5%B8%AB&area=6001001000%2C6001002000&order=1&asc=0&excludeJobKeyword=%E7%B3%BB%E7%B5%B1%E5%88%86%E6%9E%90%E5%B8%AB&kwop=7&page='
    page_range = range(1,6)
    #url_part2 = '&mode=s&jobsource=n104bank1'
    start_urls = ['https://www.104.com.tw/jobs/search/list?ro=0&keyword=%E6%95%B8%E6%93%9A%E5%88%86%E6%9E%90%E5%B7%A5%E7%A8%8B%E5%B8%AB&area=6001001000%2C6001002000&order=1&asc=0&excludeJobKeyword=%E7%B3%BB%E7%B5%B1%E5%88%86%E6%9E%90%E5%B8%AB&kwop=7&page='+str(i)+'&mode=s&jobsource=n104bank1' for i in page_range]
    
    def parse(self, response):
        res = json.loads(response.body_as_unicode())
        jobItems = []#JobsOverviewItem()
        #[items['custName'] for items in res['data']['list']]
        
        for items in res['data']['list']:
        	jobItem = JobsOverviewItem()
        	jobItem['title'] = items['jobName']
        	jobItem['address'] = items['jobAddress']
        	jobItem['description'] = items['description']
        	jobItem['education'] = items['optionEdu']
        	jobItem['required_year'] = items['periodDesc']
        	jobItem['apply_count'] = items['applyCnt']
        	jobItem['comp_name'] = items['custName']
        	jobItem['industry'] = items['coIndustryDesc']
        	jobItem['salary'] = items['salaryDesc']
        	jobItem['appearDate'] = items['appearDate']
        	jobItem['link'] = items['link']['job']
        	jobItems.append(jobItem)
        return jobItems