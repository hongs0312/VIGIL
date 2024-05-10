import pymysql


class Connection:
    def __init__(self, db):
        self.host = '127.0.0.1'
        self.user = 'discord'
        self.password = 'discord'
        self.db = db
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print(f"[알림][{self.db}에 성공적으로 연결되었습니다]")

    def __del__(self):
        self.conn.close()
        print(f"[알림][{self.db}와 연결을 끊었습니다]")

    def get_connection(self):
        self.conn.ping()
        return self.conn, self.cur
