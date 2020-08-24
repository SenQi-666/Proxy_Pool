## ProxyPool

------

可扩展的代理池，提供接口，目前针对云代理对接 [ip3366.net](ip3366.net)，如扩展其他站点可自行修改



### 目录

------

```
├── ProxyPool
│   ├── API.py
│   ├── Crawler.py
│   ├── Header.py
│   ├── MysqlControl.py
│   ├── Scheduler.py
│   ├── Tester.py
│   └── __init__.py
├── bin
│   ├── __init__.py
│   └── run_project.py
├── conf
│   └── Settings.py
├── libs
│   └── fake_useragent.json
├── README.md
└── requirements.txt
```



### 使用前请安装依赖

```
$ pip3 install -r requirements.txt
```



### 基础配置

------

#### 程序基本配置

在 conf/Settings.py 修改

```python
# 爬虫类，如扩展其他站点可在此配置
CRAWLER_MAP = {
    'yundaili': 'YunDaiLiCrawler',
    # 'kuaidaili': 'KuaiDaiLiCrawler',
}

# 爬虫站点URL规则, 如扩展其他站点可在此配置
CRAWLER_URL = {
    'yundaili': 'http://www.ip3366.net/?&page=%s',
}

# 检测URL
TEST_URL = 'http://www.ip3366.net/'

# 爬虫超时异常
CRAWLER_TIMEOUT = 5

# 检测超时异常
TEST_TIMEOUT = 5

# 检测状态码
TEST_STATUS_CODES = [200, 302]

# 浏览器标识，None为默认从库中随机选择，也可指定
USER_AGENT = None

# 数据库地址
MYSQL_HOST = 'localhost'

# 数据库端口
MYSQL_PORT = 3306

# 数据库用户名
MYSQL_USERNAME = 'root'

# 数据库密码，如无填None
MYSQL_PASSWORD = None

# 数据库名称，自行更改
DB_NAME = 'ProxyPool'

# API接口地址
API_HOST = '0.0.0.0'

# API接口端口
API_PORT = 5001

# 初始代理等级分数
INITIAL_SCORE = 5

# 最大代理等级分数
MAX_SCORE = 10

# 最小代理等级分数
MIN_SCORE = 1

# 爬虫开关
CRAWLER_ENABLED = True

# 检测器开关
TESTER_ENABLED = True

# API接口服务
API_ENABLED = True

# 爬虫延迟
CRAWLER_DELAY = 1

# 检测延迟
TESTER_DELAY = 1

# 最大批检测量
BATCH_TEST_SIZE = 10
```



### 运行

------

```
$ cd bin
$ python3 run_project.py
```



#### 运行效果

```
代理池开始运行......
开始检测IP有效性，请稍后......
开始爬虫，获取IP，请稍后......
正在抓取 yundaili 站点的IP......
API接口开始运行......
 * Serving Flask app "ProxyPool.API" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
代理IP：HTTP://203.218.116.199:8888 已保存
代理IP：HTTPS://27.43.191.43:9999 已保存
代理IP：HTTPS://220.249.149.51:9999 已保存
代理IP：HTTP://27.43.190.54:9999 已保存
代理IP：HTTPS://123.55.98.204:9999 已保存
代理IP：HTTP://58.253.153.161:9999 已保存
当前代理IP：HTTP://203.218.116.199:8888 可用
代理IP：HTTP://203.218.116.199:8888，当前等级分数已+1，现分数为：6
当前代理IP：HTTPS://220.249.149.51:9999 可用
代理IP：HTTPS://220.249.149.51:9999，当前等级分数已+1，现分数为：6
当前代理IP：HTTP://58.253.153.161:9999 可用
当前代理IP：HTTPS://27.43.191.43:9999 可用
代理IP：HTTP://58.253.153.161:9999，当前等级分数已+1，现分数为：6
代理IP：HTTPS://27.43.191.43:9999，当前等级分数已+1，现分数为：6
当前代理IP：HTTP://27.43.190.54:9999 可用
代理IP：HTTP://27.43.190.54:9999，当前等级分数已+1，现分数为：6
当前代理IP：HTTPS://58.253.159.205:9999 可用
代理IP：HTTPS://58.253.159.205:9999，当前等级分数已+1，现分数为：6
......
```

