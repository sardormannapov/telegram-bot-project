import psycopg2


class Postgres:

    def __init__(self):
        self.data_base = psycopg2.connect(
                        host='localhost',
                        user='postgres',
                        database='online_store',
                        password='123456'
                        )
        self.cursor = self.data_base.cursor()

    def create_table(self):
        """Create table"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS computer_mice (
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(255),
                product_image VARCHAR(255),
                product_price VARCHAR(255),
                product_url VARCHAR(255)
            )
        """)

    def insert_into(self, *args):
        self.create_table()
        self.cursor.execute(f"""
            INSERT INTO computer_mice (product_name, product_image, product_price, product_url) 
            VALUES 
            (%s, %s, %s, %s)
        """, args)
        return self.data_base.commit()

    def select_data(self):
        """select data"""
        self.cursor.execute("""
            SELECT product_name, product_image,product_price,product_url
            FROM computer_mice
        """)
        return self.cursor.fetchall()

Postgres().select_data()