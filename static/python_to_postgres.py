import psycopg2

hostname = 'localhost'
database = 'dcc'
username = 'postgres'
pwd = 'aarti'
port_id = 5432

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    print("Connection successful")
    conn.close()
except Exception as error:
    print("Connection failed:", error)