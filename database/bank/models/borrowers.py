from .base_model import BaseModel


class Borrowers(BaseModel):
    table_name = "borrowers"

    def create(self, data: dict):
        query = f"""INSERT INTO {self.table_name} (national_code, first_name, last_name, 
        father_name, birth_date, phone, mobile, address, postal_code) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"""
        params = (
            data['national_code'], data['first_name'],
            data['last_name'], data['father_name'],
            data['birth_date'], data['phone'],
            data['mobile'], data['address'], 
            data['postal_code']
        )

        return self.db_manager.execute_query(query, params)

    def update(self, id: str, data: dict):
        query = f"""UPDATE {self.table_name} SET national_code = %s, first_name = %s, 
        last_name = %s, father_name = %s, birth_date = %s, phone = %s, mobile = %s, 
        address = %s, postal_code = %s WHERE id = %s"""
        params = (
            data['national_code'], data['first_name'],
            data['last_name'], data['father_name'],
            data['birth_date'], data['phone'],
            data['mobile'], data['postal_code'], id
        )

        return self.db_manager.execute_query(query, params)

    def search(self, keyword: str):
        query = f"""SELECT * FROM {self.table_name} WHERE national_code LIKE %s
        OR first_name LIKE %s OR last_name LIKE %s OR father_name LIKE %s
        OR birth_date LIKE %s OR phone LIKE %s OR mobile LIKE %s OR postal_code LIKE %s"""
        search_term = f"%{keyword}%"

        return self.db_manager.execute_query(query, (search_term,) * 8)
