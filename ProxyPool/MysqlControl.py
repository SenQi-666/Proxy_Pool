from conf.Settings import *
import pymysql
import random


class MysqlClient:
    def __init__(self):
        self.conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            db=DB_NAME
        )
        self.cursor = self.conn.cursor()

    def add(self, ip, score=INITIAL_SCORE):
        sql = "INSERT INTO Proxies (IP, SCORE) VALUES (%s, %s)"
        if not self.is_exists(ip):
            self.cursor.execute(sql, (ip, score))
            self.conn.commit()

    def delete(self, ip):
        sql = "DELETE FROM Proxies WHERE IP=%s"
        if self.is_exists(ip):
            self.cursor.execute(sql, ip)
            self.conn.commit()
            return True
        else:
            return False

    def increase(self, ip):
        sql_get = "SELECT * FROM Proxies WHERE IP=%s"
        try:
            if self.cursor.execute(sql_get, ip):
                score = int(self.cursor.fetchone()[2])
                if MIN_SCORE <= score < MAX_SCORE:
                    score += 1
                    sql_increase = "UPDATE Proxies SET SCORE=%s WHERE IP=%s"
                    self.cursor.execute(sql_increase, (score, ip))
                    self.conn.commit()
                    print('代理IP：%s，当前等级分数已+1，现分数为：%s' % (ip, score))
                else:
                    print('代理IP：%s，当前等级分数：%s，请继续使用' % (ip, score))

            else:
                raise ValueError('IP NOT FOUND')
        except Exception as e:
            print(e.args)

    def decrease(self, ip):
        sql_get = "SELECT * FROM Proxies WHERE IP=%s"
        try:
            if self.cursor.execute(sql_get, ip):
                score = int(self.cursor.fetchone()[2])
                if MIN_SCORE < score <= MAX_SCORE:
                    score -= 1
                    sql_decrease = "UPDATE Proxies SET SCORE=%s WHERE IP=%s"
                    self.cursor.execute(sql_decrease, (score, ip))
                    self.conn.commit()
                    print('代理IP：%s，当前等级分数已-1，现分数为：%s' % (ip, score))
                else:
                    sql_del = "DELETE FROM Proxies WHERE IP=%s"
                    self.cursor.execute(sql_del, ip)
                    self.conn.commit()
                    print('当前代理IP：%s，其等级分数已小于最低等级分数：%s，现已移除' % (ip, MIN_SCORE))
            else:
                raise ValueError('IP NOT FOUND')
        except Exception as e:
            print(e.args)

    def random(self):
        sql_max = "SELECT * FROM Proxies WHERE SCORE=%s"
        if self.cursor.execute(sql_max, MAX_SCORE):
            result = self.cursor.fetchall()
            return random.choice(result)[1]
        else:
            sql_else = "SELECT * FROM Proxies WHERE SCORE BETWEEN %s AND %s"
            if self.cursor.execute(sql_else, (MIN_SCORE, MAX_SCORE)):
                result = self.cursor.fetchall()
                return random.choice(result)[1]
            else:
                raise ValueError('ProxyPool is Empty')

    def count(self):
        sql = "SELECT * FROM Proxies"
        return self.cursor.execute(sql)

    def is_exists(self, ip):
        sql = "SELECT * FROM Proxies WHERE IP=%s"
        return self.cursor.execute(sql, ip)
