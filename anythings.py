import sqlite3
def add_seller(conn, username, name,  password):
   c = conn.cursor()
   c.execute('''INSERT INTO workers (username, name, pass)
               VALUES (?, ?, ?)''', (username, name, password))
def clear_table(database_path, table_name):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    try:
        # Use DELETE to remove all rows from the table
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        print(f"All rows from {table_name} cleared.")
    except sqlite3.Error as e:
        print(f"Error clearing table {table_name}: {e}")
    finally:
        conn.close()

# Example usage
database_path = "daily_counter.db"
table_name = "workers"
clear_table(database_path, table_name)
# conn = sqlite3.connect(database_path)
# add_seller(conn, 'majd','مجد أبو النور', '4242')