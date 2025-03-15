from connection import make_connection, end_connection

def test_db_connection():
    conn, cursor = make_connection()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Tables in mydatabase:", tables)
    end_connection(conn, cursor)

if __name__ == "__main__":
    test_db_connection()
