from .base_model import BaseModel


class Payments(BaseModel):
    table_name = 'payments'

    def create(self, data: dict):
        query = f"""INSERT INTO {self.table_name} 
        (installment_id, amount, payment_date, payment_method, 
        reference_number, description)
        VALUES 
        (%s, %s, %s, %s, %s, %s)"""

        params = (
            data['installment_id'], data['amount'],
            data['payment_date'], data['payment_method'],
            data['reference_number'], data['description']
        )

        self.db_manager.execute_query(query, params=params)

    def update(self, id: int):
        query = f"""UPDATE TABLE {self.table_name}
        SET description = %s WHERE id = %s"""
        params = (id,)

        self.db_manager.execute_query(query, params=params)

    def search(self, keyword: str):
        query = f"""SELECT * FROM {self.table_name} 
        WHERE installment_id LIKE %s OR payment_date LIKE %s OR
        payment_method LIKE %s"""
        search_term = (keyword,)

        return self.db_manager.execute_query(query, (search_term,) * 3)
