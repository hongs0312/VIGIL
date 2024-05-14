from db_connection.mariaDB_connection import Connection


class GearRepo:
    def __init__(self):
        self.connection = Connection('gear_data')

        self.forward_count = self.get_row_count("forward_information")
        self.goalie_count = self.get_row_count("goalie_information")

    def get_row_count(self, table_name):
        conn, cur = self.connection.get_connection()
        query = f"SELECT COUNT(*) FROM {table_name}"
        cur.execute(query)
        return cur.fetchone()['COUNT(*)']

    def add_forward_gear(self, name, image, description):
        conn, cur = self.connection.get_connection()
        query = "INSERT INTO forward_information VALUES(%s, %s, %s, %s)"
        cur.execute(query, (self.forward_count+1, name, image, description))
        conn.commit()
        self.forward_count += 1

        return self.forward_count

    def update_forward_gear(self, forward_id, name, image, description):
        conn, cur = self.connection.get_connection()
        query = "UPDATE forward_information SET name=%s, image=%s, description=%s WHERE id=%s"
        cur.execute(query, (name, image, description, forward_id))
        conn.commit()

    def get_forward_gear(self, forward_id):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM forward_information WHERE id = %s"
        cur.execute(query, forward_id)
        return cur.fetchone()

    def get_forward_gear_by_name(self, name):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM forward_information WHERE REPLACE(name, ' ', '') = %s"
        cur.execute(query, name.replace(" ", ""))
        return cur.fetchone()

    def get_all_forward_gear(self):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM forward_information"
        cur.execute(query)
        return cur.fetchall()

    def add_goalie_gear(self, name, image, description):
        conn, cur = self.connection.get_connection()
        query = "INSERT INTO goalie_information VALUES(%s, %s, %s, %s)"
        cur.execute(query, (self.goalie_count+1, name, image, description))
        conn.commit()
        self.goalie_count += 1

        return self.goalie_count

    def update_goalie_gear(self, goalie_id, name, image, description):
        conn, cur = self.connection.get_connection()
        query = "UPDATE goalie_information SET name=%s, image=%s, description=%s WHERE id=%s"
        cur.execute(query, (name, image, description, goalie_id))
        conn.commit()

    def get_goalie_gear(self, goalie_id):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM goalie_information WHERE id = %s"
        cur.execute(query, goalie_id)
        return cur.fetchone()

    def get_goalie_gear_by_name(self, name):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM goalie_information WHERE REPLACE(name, ' ', '') = %s"
        cur.execute(query, name.replace(" ", ""))
        return cur.fetchone()

    def get_all_goalie_gear(self):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM goalie_information"
        cur.execute(query)
        return cur.fetchall()

    def get_gear_by_name(self, gear_type, gear_name):
        conn, cur = self.connection.get_connection()
        query = f"SELECT * FROM {gear_type}_information WHERE REPLACE(name, ' ', '') = %s"
        cur.execute(query, gear_name.replace(" ", ""))
        return cur.fetchone()

    def clear_all_tables(self):
        conn, cur = self.connection.get_connection()

        query = "TRUNCATE TABLE forward_information"
        cur.execute(query)
        query = "TRUNCATE TABLE goalie_information"
        cur.execute(query)

        conn.commit()


if __name__ == "__main__":
    repo = GearRepo()

    repo.clear_all_tables()
