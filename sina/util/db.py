import pymysql
from scrapy.utils.project import get_project_settings


class DBConnection:
    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWORD']
        self.db = self.settings['MYSQL_DB']

    def connection(self):
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            db=self.db
        )
        return conn

    # 执行插入、更新语句
    def execute(self, sql, params):
        conn = self.connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, params)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()
