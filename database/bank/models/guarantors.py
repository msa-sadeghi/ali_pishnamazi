from .base_model import BaseModel


class Guarantors(BaseModel):
    def create(self, data: dict):
        query = """INSERT INTO {self.table_name} (loan_id,
        national_code, first_name, last_name, phone, 
        address, relationship)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s)"""

        params = (
            data['loan_id'], data['national_code'],
            data['first_name'], data['last_name'],
            data['phone'], data['address'],
            data['relationship']
        )

        self.db_manager.execute_query(query, params=params)

    def update(self, id: str, data: dict):
        # I'm not sure that what could we update here in this table
        pass

    def search(self, keyword: str):
        query = f"""SELECT * FROM {self.table_name}
        WHERE loan_id LIKE %s OR first_name LIKE %s OR
        last_name LIKE %s OR relationship LIKE %s"""
        params = (keyword,)

        self.db_manager.execute_query(query, params=params)
