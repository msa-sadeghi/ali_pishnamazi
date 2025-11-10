from .base_model import BaseModel
class Borrower(BaseModel):
    table_name = "borrowers"
    def create(self, data):
        query = """INSERT INTO borrowers (national_code, first_name, last_name, father_name, birth_date,
        phone, mobile, address, postal_code) VALUES (%s, %s, %s , %s, %s , %s , %s,%s, %s)
        RETURNING id"""
        params = (
            data['national_code'], data['first_name'],
            data['last_name'], data['father_name'],
            data['birth_date'], data['phone'],
            data['mobile'], data['address'],
            data['postal_code']
        )
        return self.db.execute_query(query, params)
    
    def update(self, id, data):
        pass
    def search(self, keyword):
        pass
