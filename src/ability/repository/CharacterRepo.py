from db_connection.mariaDB_connection import Connection
from ability.repository.sql import character_information_create, skill_information_create


class CharacterRepo:
    def __init__(self):
        # character_data DB 연결 객체
        self.connection = Connection('character_data')

        self.character_count = self.get_row_count("character_information")
        self.skill_count = self.get_row_count("skill_information")

    def get_row_count(self, table_name):
        conn, cur = self.connection.get_connection()
        query = f"SELECT COUNT(*) FROM {table_name}"
        cur.execute(query)
        return cur.fetchone()['COUNT(*)']

    def add_character(self, name):
        conn, cur = self.connection.get_connection()
        query = "INSERT INTO character_information VALUES(%s, %s, 0, 0, 0, 0, 0)"
        cur.execute(query, (self.character_count+1, name))
        conn.commit()
        self.character_count += 1

        # return character_id
        return self.character_count

    def get_character(self, name):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM character_information WHERE name = %s"
        cur.execute(query, name.lower())
        return cur.fetchone()

    def get_all_characters(self):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM character_information"
        cur.execute(query)
        return cur.fetchall()

    def get_all_character_names(self):
        conn, cur = self.connection.get_connection()
        query = "SELECT name FROM character_information"
        cur.execute(query)
        return cur.fetchall()

    def add_skill(self, name, cooldown, damage, description, features, image):
        conn, cur = self.connection.get_connection()
        query = "INSERT INTO skill_information VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (self.skill_count+1, name, cooldown, damage, description, image, features))
        conn.commit()
        self.skill_count += 1

        # return skill_id
        return self.skill_count

    def update_skill(self, skill_id, name, cooldown, damage, description, image, features):
        conn, cur = self.connection.get_connection()
        query = "UPDATE skill_information SET name=%s, cooldown=%s, damage=%s, description=%s, image=%s, feature=%s WHERE id=%s"
        cur.execute(query, (name, cooldown, damage, description, image, features, skill_id))
        conn.commit()

    def get_skill(self, skill_id):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM skill_information WHERE id = %s"
        cur.execute(query, skill_id)
        return cur.fetchone()

    def get_skill_by_name(self, name):
        conn, cur = self.connection.get_connection()
        query = "SELECT * FROM skill_information WHERE name = %s"
        cur.execute(query, name)
        return cur.fetchone()

    def link_character_and_skill(self, character_id, skill_type, skill_id):
        conn, cur = self.connection.get_connection()
        query = f"UPDATE character_information SET `{skill_type.lower()}`=%s WHERE `id`=%s"
        cur.execute(query, (skill_id, character_id))
        conn.commit()

    def clear_repository(self):
        conn, cur = self.connection.get_connection()
        query = "TRUNCATE character_information"
        cur.execute(query)
        query = "TRUNCATE skill_information"
        cur.execute(query)
        conn.commit()

    def make_table(self):
        conn, cur = self.connection.get_connection()
        cur.execute(character_information_create)
        cur.execute(skill_information_create)
        conn.commit()

    def drop_table(self):
        conn, cur = self.connection.get_connection()
        query = "DROP TABLE character_information"
        cur.execute(query)
        query = "DROP TABLE skill_information"
        cur.execute(query)
        conn.commit()


if __name__ == "__main__":
    repo = CharacterRepository()

    repo.clear_repository()