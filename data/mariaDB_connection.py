import pymysql


class Connection:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'discord'
        self.password = 'discord'
        self.db = 'character_data'
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        print("[알림][DB에 성공적으로 연결되었습니다]")

    def __del__(self):
        self.conn.close()
        print("[알림][DB 연결을 끊었습니다]")

    def get_connection(self):
        self.conn.ping()
        return self.conn, self.cur