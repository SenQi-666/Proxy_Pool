from ProxyPool.MysqlControl import MysqlClient
from ProxyPool.Header import UAPool
from conf.Settings import *
from queue import Queue
import threading
import requests
import time


class Produce(threading.Thread):
    def __init__(self, queue):
        super(Produce, self).__init__()
        self.q = queue
        self.mysql = MysqlClient()

    def run(self):
        self.mysql.count()
        result = self.mysql.cursor.fetchall()
        for detail in result:
            self.q.put(detail[1])


class Tester(threading.Thread):
    def __init__(self, queue):
        super(Tester, self).__init__()
        self.q = queue

    def run(self):
        while True:
            if self.q.empty():
                break
            else:
                ip = self.q.get()
                headers = {'User-Agent': UAPool().get_header()}
                proxy = {ip.split('://')[0]: ip.split('://')[1]}
                try:
                    response = requests.get(TEST_URL, headers=headers, proxies=proxy, timeout=TEST_TIMEOUT)
                    if response.status_code in TEST_STATUS_CODES:
                        print('当前代理IP：%s 可用' % ip)
                        MysqlClient().increase(ip)
                    elif response.status_code == 404:
                        print('检测站点：%s 已失效，请更换其他站点' % TEST_URL)
                    else:
                        print('访问出现问题')
                except Exception as e:
                    MysqlClient().decrease(ip)
                    print('代理IP：%s 请求失败，异常：%s' % (ip, e.args[0]))
                time.sleep(TESTER_DELAY)


def start_test(batch_size):
    q = Queue()
    p = Produce(q)
    p.start()

    for _ in range(batch_size):
        t = Tester(q)
        t.start()
