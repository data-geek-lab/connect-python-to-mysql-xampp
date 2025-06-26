

import mysql.connector

print("Script started…")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="",
        database="newdb"
    )

    if conn.is_connected():
        print("✅  Connected to MySQL successfully!")
    else:
        print("❌  Connection object created, but is_connected() returned False.")

except mysql.connector.Error as e:
    print(f"❌  MySQL error: {e}")

except Exception as e:
    print(f"❌  General error: {e}")