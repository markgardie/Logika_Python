import sqlite3
import datetime

def create_connection(db_file):
    """Створення підключення до бази даних"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_query(conn, query, params=None):
    """Виконання SQL запиту"""
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor
    except sqlite3.Error as e:
        print(f"Помилка при виконанні запиту: {e}")
        return None

def create_tables(conn):

    orders_table = ''' 
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL,

    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    FOREIGN KEY(product_id) REFERENCES products(product_id)
    '''

    execute_query(conn, orders_table)

def total_sales(conn):
    query = ''' 
    SELECT SUM(orders.quantity * products.price)
    FROM orders
    JOIN products ON products.product_id = orders.product_id;

    '''

    cursor = execute_query(conn, query)
    if cursor:
        result = cursor.fetchone()
        print("Загальний обсяг продажів:", result)
        return result
    return None

def average_order_value(conn):
    query = ''' 
    SELECT AVG(total)
    FROM (
            SELECT orders.order_id, SUM(products.price * orders.quantity) as total
            FROM orders
            JOIN products ON products.product_id = orders.product_id
            GROUP BY orders.order_id
        )

    '''

    cursor = execute_query(conn, query)
    if cursor:
        result = cursor.fetchone()
        print("Середній чек:", result)
        return result
    return None

