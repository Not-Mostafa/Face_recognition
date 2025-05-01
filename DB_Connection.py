import pyodbc

def connect_to_database(server_name, database_name='master'):
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            f'SERVER={server_name};'
            f'Database={database_name};'
            'Trusted_Connection=True'
        )
        print(f'Successfully connected to database "{database_name}"')
        return connection
    except pyodbc.Error as ex:
        print(f'Failed to connect to database: {ex}')
        return None


def create_database(server_name, database_name):
    try:
        connection = connect_to_database(server_name, 'master')
        if connection is None:
            return False

        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute('CREATE DATABASE ' + database_name)
        print(f'Database "{database_name}" created successfully on server "{server_name}"')
        cursor.close()
        connection.close()
        return True
    except pyodbc.Error as ex:
        print(f'Failed to create database: {ex}')
        return False


def drop_database(server_name, database_name):
    try:
        # Must connect to master database to drop databases
        connection = connect_to_database(server_name, 'master')
        if connection is None:
            return False

        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute('DROP DATABASE ' + database_name)
        print(f'Database "{database_name}" dropped successfully from server "{server_name}"')
        cursor.close()
        connection.close()
        return True
    except pyodbc.Error as ex:
        print(f'Failed to drop database: {ex}')
        return False

if __name__ == "__main__":
    server = "MOSTAFA"
    db_name = "TestLast"
    if drop_database(server, db_name):
        create_database(server, db_name)