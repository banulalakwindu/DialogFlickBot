import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ai"
)


def insert_order(item, quantity, type):
    try:
        cursor = cnx.cursor()
        query = "INSERT INTO orders (item_name, quantity, disk_type) VALUES (%s, %s, %s)"
        values = (item, quantity, type)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        print("Order inserted successfully")
        return 1
    except mysql.connector.Error as err:
        print("Error Inserting order item: {}".format(err))
        cnx.rollback()
        return -1
    except Exception as e:
        print("An error Occurred: {}".format(e))
        cnx.rollback()
        return -1
