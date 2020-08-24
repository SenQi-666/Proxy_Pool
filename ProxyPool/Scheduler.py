from multiprocessing import Process
from ProxyPool.Crawler import *
from ProxyPool.Tester import *
from ProxyPool.API import app
from conf.Settings import *


class Dispatch:
    @staticmethod
    def crawler():
        print('开始爬虫，获取IP，请稍后......')
        for website, cls in CRAWLER_MAP.items():
            print('正在抓取 %s 站点的IP......' % website)
            getattr(eval(cls + '()'), 'start_crawler')(CRAWLER_URL[website])
            print('%s 站点的IP全部生成并保存完成' % website)

    @staticmethod
    def tester():
        print('开始检测IP有效性，请稍后......')
        start_test(BATCH_TEST_SIZE)

    @staticmethod
    def api():
        print('API接口开始运行......')
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        print('代理池开始运行......')

        if CRAWLER_ENABLED:
            crawler = Process(target=self.crawler)
            crawler.start()

        if API_ENABLED:
            api = Process(target=self.api)
            api.start()

        if TESTER_ENABLED:
            self.tester()
