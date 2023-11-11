import mysql.connector
from PyQt5.QtWidgets import QApplication
from abc_b_first_window import FirstWindow

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
    tables = ["Products", "Cart", "purchase_history", "User", "Products_for_cart"]
    cursor.execute(create_database)
    
    products_table = f"""
                        CREATE TABLE {tables[0]}
                        (
                            id INTEGER auto_increment,
                            product_name VARCHAR(30),
                            product_price INTEGER,
                            product_category VARCHAR(30),
                            PRIMARY KEY (id)
                        );"""
    
    cart_table = f"""
                    CREATE TABLE {tables[1]}
                    (
                        id INTEGER,
                        PRIMARY KEY (id),
                    );
            """
    
    purchase_history_table = f"""
                                CREATE TABLE {tables[2]}
                                (
                                    id INTEGER,
                                    cart_id INTEGER,
                                    status INTEGER(1),
                                    PRIMARY KEY (id),
                                    FOREIGN KEY (cart_id) REFERENCES Cart(id)
                                );
                            """
    
    users_table = f"""
                    CREATE TABLE {tables[3]}
                    (
                        id INTEGER auto_increment,
                        username VARCHAR (30),
                        cart_id INTEGER,
                        purchase_history_table_id INTEGER,
                        PRIMARY KEY (id),
                        FOREIGN KEY (purchase_history_table_id) REFERENCES purchase_history(id),
                        FOREIGN KEY (cart_id) REFERENCES Cart(id)
                    );
                """
    
    products_for_cart = f"""
                            CREATE TABLE {tables[4]}
                            (
                                cart_id INTEGER,
                                product_id INTEGER,
                                FOREIGN KEY (cart_id) REFERENCES Cart(id) ON DELETE CASCADE,
                                FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
                            );
                        """
    
    tables = [products_table, cart_table, purchase_history_table, users_table, products_for_cart]
    use_query = f"USE {original_database_name};"
    cursor.execute(use_query)
    for table in tables:
        cursor.execute(table)

cursor.close()
temporary_connection.close()

app = QApplication([])

__welcoming_window = FirstWindow()
__welcoming_window.resize(1200, 600)
__welcoming_window.show()

app.exec()
