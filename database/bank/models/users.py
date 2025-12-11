from .base_model import BaseModel


class Users(BaseModel):
    table_name = "users"

    def create(self, data: dict):
        query = f"""INSERT INTO {self.table_name} (username, password_hash, 
        full_name, role, is_active)
        VALUES
        (%s, %s, %s, %s, %s)"""
        params = (
            data['username'], data['password_hash'],
            data['full_name'], data['role'],
            data['is_active']
        )

        self.db_manager.execute_query(query, params=params)

    def update(self, id: str, data: dict):
        query = f"""UPDATE TABLE {self.table_name}
        SET username = %s password_hash = %s
        full_name = %s role = %s is_active = %s
        WHERE id = %s"""

        params = (
            data['username'], data['password_hash'],
            data['full_name'], data['role'],
            data['is_active'], id
        )

        self.db_manager.execute_query(query, params=params)

    def search(self, keyword: str):
        query = f"""SELECT * FROM {self.table_name}
        WHERE username LIKE %s OR full_name LIKE %s
        OR role LIKE %s OR is_active LIKE %s"""

        search_term = (keyword,)
        self.db_manager.execute_query(query, (search_term,) * 4)
