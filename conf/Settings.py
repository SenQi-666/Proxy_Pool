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
