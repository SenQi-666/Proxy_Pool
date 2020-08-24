from ProxyPool.MysqlControl import MysqlClient
from ProxyPool.Header import UAPool
from conf.Settings import *
from lxml import etree
import aiohttp
import asyncio


class BasicCrawler:
    def __init__(self, timeout, user_agent=None):
        self.timeout = timeout
        self.user_agent = user_agent
        self.mysql = MysqlClient()

    async def source_page(self, url):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(url, headers={'User-Agent': self.user_agent}, timeout=self.timeout) as response:
                page_text = await response.text()
                await asyncio.sleep(CRAWLER_DELAY)
                return page_text


class YunDaiLiCrawler(BasicCrawler):
    def __init__(self):
        timeout = CRAWLER_TIMEOUT
        user_agent = UAPool().get_header()
        super(YunDaiLiCrawler, self).__init__(timeout, user_agent)

    async def get_ip(self, url):
        ip_lst = []
        page_text = await self.source_page(url)
        html = etree.HTML(page_text)
        ips = html.xpath('//*[@id="list"]/table//tr/td[1]/text()')
        ports = html.xpath('//*[@id="list"]/table//tr/td[2]/text()')
        agreements = html.xpath('//*[@id="list"]/table//tr/td[4]/text()')
        for ip, port, agreement in zip(ips, ports, agreements):
            ip_lst.append('%s://%s:%s' % (agreement, ip, port))

        return ip_lst

    @staticmethod
    def generate_urlist(url):
        urls = [url % num for num in range(1, 11)]
        return urls

    def start_crawler(self, url):
        urls = self.generate_urlist(url)
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(self.get_ip(url)) for url in urls]
        [task.add_done_callback(self.save) for task in tasks]
        loop.run_until_complete(asyncio.wait(tasks))

    def save(self, task):
        result = task.result()
        if result:
            for ip in result:
                self.mysql.add(ip)
                print('代理IP：%s 已保存' % ip)
        else:
            return None
