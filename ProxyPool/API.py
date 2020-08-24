from ProxyPool.MysqlControl import MysqlClient
from flask import Flask, g

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Welcome to the Proxy Pool System</h2>'


@app.route('/random')
def random():
    conn = mysql_conn()
    return conn.random()


@app.route('/count')
def count():
    conn = mysql_conn()
    return str(conn.count())


def mysql_conn():
    if not hasattr(g, 'mysql'):
        g.conn = MysqlClient()
    return g.conn
