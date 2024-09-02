import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        if connection.is_connected():
            return connection
        else:
            print(f"Failed to connect to the database: {db_name}")
            return None
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def signup(username, email, password, host, port, database, mysql_user, mysql_password):
    connection = create_connection(host, mysql_user, mysql_password, database)
    if connection is None:
        print("Failed to create a database connection.")
        return False
    
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        connection.commit()
        return True
    except Error as e:
        print(f"The error '{e}' occurred")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def login(email, password, host, port, database, mysql_user, mysql_password):
    connection = create_connection(host, mysql_user, mysql_password, database)
    if connection is None:
        print("Failed to create a database connection.")
        return False
    
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cursor.fetchone()
        if user:
            return True
        return False
    except Error as e:
        print(f"The error '{e}' occurred")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def get_user_id(email, host, port, database, mysql_user, mysql_password):
    connection = create_connection(host, mysql_user, mysql_password, database)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE email=%s",
        (email,)
    )
    user_id = cursor.fetchone()
    return user_id[0] if user_id else None

def store_mcq_result(user_id, language, correct_count, total_questions, host, port, database, mysql_user, mysql_password):
    connection = create_connection(host, mysql_user, mysql_password, database)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO mcq_results (user_id, language, correct_count, total_questions) VALUES (%s, %s, %s, %s)",
        (user_id, language, correct_count, total_questions)
    )
    connection.commit()

def store_coding_result(user_id, language, problem, solution, score, host, port, database, mysql_user, mysql_password):
    import mysql.connector
    
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=mysql_user,
            password=mysql_password
        )
        
        cursor = connection.cursor()
        query = """
        INSERT INTO coding_results (user_id, language, problem, solution, score)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, language, problem, solution, score))
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_mcq_results(user_id, host, port, database, mysql_user, mysql_password):
    connection = create_connection(host, mysql_user, mysql_password, database)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT language, correct_count, total_questions, created_at FROM mcq_results WHERE user_id=%s",
        (user_id,)
    )
    return cursor.fetchall()

def get_coding_results(user_id, host, port, database, mysql_user, mysql_password):
    connection = create_connection(host, mysql_user, mysql_password, database)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT language, problem, solution, created_at FROM coding_results WHERE user_id=%s",
        (user_id,)
    )
    return cursor.fetchall()
