from db_connection import DatabaseConnection

connection = DatabaseConnection.create()
connection.connect()

other_method_connection = DatabaseConnection.create()

if other_method_connection == connection:
    print("They are the same")
