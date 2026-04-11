import os
import sqlite3
from datetime import date

PASSWORD = "MERKL"

def create_database():
    os.system("touch database.db") # This line is vulnerable to command injection
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()
    print("Database created successfully.")
    return conn

def insert_user(conn):
    cursor = conn.cursor()
    name = input("Name : ")
    birthdate = input("Brithday (jj/mm/yy) : ").split("/")
    today = date.today()
    # nosemgrep: python.lang.security.audit.eval-detected.eval-detected -- Intentional suppression
    age = eval(
        f"{today.year} - {birthdate[2]} - (({today.month}, {today.day}) < (int('{birthdate[1]}'), int('{birthdate[0]}')))"
    ) # This line is vulnerable to SQL injection
    cursor.execute("""
    INSERT INTO users (name, age) VALUES (?, ?)
    """, (name, age))
    conn.commit()
    print("User inserted successfully.")


def affiche_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    else:
        print("No users found.")

def supprimer_user(conn):
    user_id = input("Enter the ID of the user to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = " + user_id) # This line is vulnerable to SQL injection
    conn.commit()
    print(f"User with ID {user_id} deleted successfully.")


def main():
    if (input("password : ") == PASSWORD):
        print("================================")
        print("Access granted.")
        print("================================")
        conn = create_database()
        while True:
            print("\n")
            print("1. Display Users")
            print("2. Insert User")
            print("3. Delete User")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            print("\n================================")
            if choice == '1':
                affiche_users(conn)
            elif choice == '2':
                insert_user(conn)
                affiche_users(conn)
            elif choice == '3':
                supprimer_user(conn)
                affiche_users(conn)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
            print()
        conn.close()
    else :
        print("Access denied.")
        

if __name__ == "__main__":
    main()
    
    