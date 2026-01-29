import psycopg2
from psycopg2 import pool
from config import DB_CONFIG
from logging import getLogger, basicConfig, INFO

basicConfig(level=INFO)
sample_logger = getLogger(__name__)


class DatabaseManager:
    _instance = None
    _connection_pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize_pool(self):
        try:
            self._connection_pool = pool.SimpleConnectionPool(
                minconn=1, maxconn=10, **DB_CONFIG
            )
            sample_logger.info("connection pool created successfully")
        except Exception as e:
            sample_logger.error(f"error creating pool {e}")

    def get_connection(self):
        if self._connection_pool is None:
            self.initialize_pool()
        return self._connection_pool.getconn()

    def return_connection(self, connection):
        self._connection_pool.putconn(connection)

    def execute_query(self, query, params=None):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                rows = cursor.fetchall() if cursor.description else None
                return rows
        except Exception as ex:
            print(ex)
            conn.rollback()
        finally:
            self.return_connection(conn)


d = DatabaseManager()
print(d.execute_query("""SELECT * FROM borrowers"""))
