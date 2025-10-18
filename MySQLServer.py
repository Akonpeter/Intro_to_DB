import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Prizylink330@",  # <-- replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database (won’t fail if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL or creating database: {err}")

    finally:
        # Close cursor and connection safely
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()
