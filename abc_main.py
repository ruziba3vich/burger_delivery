import mysql.connector
from PyQt5.QtWidgets import QApplication

temporary_connection = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Dost0n1k'
)
original_database_name = "online_burgers_delivery_database"
# delete_query = f"DROP DATABASE {original_database_name};"
cursor = temporary_connection.cursor()
query = f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{original_database_name}';"
# cursor.execute(delete_query)
cursor.execute(query)
result = cursor.fetchone()
if not result:
    create_database = f"CREATE DATABASE {original_database_name};"
    tables = ["products", "User", "Cart"]
    cursor.execute(create_database)
    
    
    products_table = f"""
                        CREATE TABLE {tables[0]}
                        (
                            id INTEGER auto_increment,
                            product_name VARCHAR(30),
                            product_price INTEGER,
                            product_category VARCHAR(30),
                            PRIMARY KEY (id)
                        )"""
    cart_table = f"""
                    CREATE TABLE {tables[2]}
                    (
                        id INTEGER,
                    )
            """
    users_table = f"""
                    CREATE TABLE {tables[1]}
                    (
                        id INTEGER auto_increment,
                        username VARCHAR (30),
                        cart_number INTEGER,
                        in_use TINYINT(1),
                        PRIMARY KEY (id)
                    )
                """
    tables = []
    use_query = f"USE {original_database_name};"
    cursor.execute(use_query)
    for table in tables:
        cursor.execute(table)

cursor.close()
temporary_connection.close()

app = QApplication([])

app.exec()
