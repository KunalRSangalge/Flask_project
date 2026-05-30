import time
import pymysql

while True:
    try:
        connection = pymysql.connect(
            host="db",
            user="root",
            password="password",
            database="market"
        )

        print("MySQL is ready!")
        connection.close()
        break

    except Exception:
        print("Waiting for MySQL...")
        time.sleep(2)