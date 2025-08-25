import psycopg2
from psycopg2.extras import RealDictCursor
class Database:
    def __init__(self, host='localhost', dbname='SchoolManagement',user='postgres',password = 'root',
                 port=5432
                 ):
        self.con = psycopg2.connect(host=host,database=dbname,user = user,password = password,
            port = port
        )
        self.cursor = self.con.cursor(cursor_factory=RealDictCursor)
    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.con.commit()

    def fetch_one(self, query, params= None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    def fetch_all(self, query, params= None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self):
        self.cursor.close()
        self.con.close()



d = Database()