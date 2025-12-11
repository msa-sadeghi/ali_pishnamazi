from datetime import datetime, timedelta
from .base_model import BaseModel


class Loans(BaseModel):
    table_name = "loans"

    def create(self, data: dict):
        query = f"""INSERT INTO {self.table_name} (borrower_id, loan_amount, 
        installment_count, start_date, end_date, loan_type, status, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"""
        params = (
            data['borrower_id'], data['loan_amount'], data['installment_count'],
            data['start_date'], data['end_date'], data['loan_type'], data['status'],
            data['description']
        )

        res = self.db_manager.execute_query(query, params)
        self.initialize_installment(data, res)

        return res

    def initialize_installment(self, loan_data: dict, id: int):
        for i in range(loan_data['installment_count']):
            query = """INSERT INTO installments (loan_id, installment_number, due_date, amount)
            VALUES (%s, %s, %s)"""
            start_time_date = datetime.strptime(
                loan_data['start_date'], '%Y-%m-%d'
            )
            params = (
                id, i + 1, start_time_date + timedelta(days=30),
                loan_data['loan_amount'] / loan_data['installment_count']
            )

            self.db_manager.execute_query(query, params)

    def update(self, id: str, data: dict):
        query = f"""UPDATE {self.table_name} SET status = %s WHERE id = %s"""

        return self.db_manager.execute_query(query, (data['status'], id))

    def search(self, keyword: str):
        query = f"""SELECT * FROM {self.table_name} WHERE borrower_id LIKE %s OR
        loan_amount LIKE %s OR start_date LIKE %s OR end_date LIKE %s OR
        loan_type LIKE %s"""
        search_term = (keyword,)

        return self.db_manager.execute_query(query, (search_term,) * 5)
