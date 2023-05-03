import psycopg2

def get_records(pattern):
    conn = psycopg2.connect(host="localhost", dbname = "PhoneBook", user = "postgres",
                        password = "21614519Er", port = 5432)
    cur = conn.cursor()

    query = "SELECT * FROM phonebook WHERE name LIKE %s OR surname LIKE %s OR phone LIKE %s"
    cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results