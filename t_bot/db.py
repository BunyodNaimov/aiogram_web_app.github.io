import sqlite3

db_connection = sqlite3.connect('../database.db')
db_cursor = db_connection.cursor()


def db_create_table_product():
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, title TEXT, description TEXT, price REAL)
    """)


def db_get_all_products():
    products = db_cursor.execute("""
    SELECT * FROM products""").fetchall()
    print(products)
    return products