import sys
import pymysql

sys.path.append("../..")
from db_connection.mariaDB_connection import Connection

class AwakeningRepo:
    def __init__(self):
        self.connection = Connection('awakening_data')

        self.awakening_count = self.get_row_count("awakening_information")

    def get_row_count(self, table_name):
        conn, cur = self.connection.get_connection()
        query = f"SELECT COUNT(*) FROM {table_name}"
        cur.execute(query)
        return cur.fetchone()['COUNT(*)']

    def add_awakening(self, rotation, name, aka, description, image, effective_to):
        conn, cur = self.connection.get_connection()
        query = "INSERT INTO awakening_information VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (self.awakening_count+1, rotation, name, aka, description, image, effective_to))
        conn.commit()
        self.awakening_count += 1

        # return awakening_id
        return self.awakening_count

    def update_awakening(self, awakening_id, rotation, name, aka, description, image, effective_to):
        conn, cur = self.connection.get_connection()
        query = "UPDATE awakening_information SET rotation=%s, name=%s, aka=%s, description=%s, image=%s, effective_to=%s WHERE id=%s"
        cur.execute(query, (rotation, name, aka, description, image, effective_to, awakening_id))
        conn.commit()

    def get_awakening(self, awakening_id):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM awakening_information WHERE id = %s"
        cur.execute(query, awakening_id)
        return cur.fetchone()

    def get_awakening_by_name(self, name):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM awakening_information WHERE REPLACE(name, ' ', '') = %s"
        cur.execute(query, name.replace(" ", ""))
        return cur.fetchone()

    def get_awakening_by_aka(self, aka):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM awakening_information WHERE aka = %s"
        cur.execute(query, aka)
        return cur.fetchone()

    def get_all_awakenings(self):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM awakening_information"
        cur.execute(query)
        return cur.fetchall()

    def delete_awakening(self, awakening_id):
        conn, cur = self.connection.get_connection()
        query = "DELETE FROM awakening_information WHERE id = %s"
        cur.execute(query, awakening_id)
        conn.commit()
        self.awakening_count -= 1

    def clear_repository(self):
        conn, cur = self.connection.get_connection()
        query = "TRUNCATE TABLE awakening_information"
        cur.execute(query)
        conn.commit()
        self.awakening_count = 0


if __name__ == "__main__":
    repo = AwakeningRepo()

    print(repo.get_awakening_by_name("강한 충돌"))
    print(repo.get_awakening_by_aka("강충"))

    # repo.clear_repository()
