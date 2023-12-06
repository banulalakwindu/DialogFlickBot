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


def get_movie_info(movie):
    try:
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM movie WHERE mov_title = %s"
        values = (movie,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        print("Movie info retrieved successfully")
        return result
    except mysql.connector.Error as err:
        print("Error retrieving movie info: {}".format(err))
        return None
    except Exception as e:
        print("An error Occurred: {}".format(e))
        return None


def insert_movie(movie):
    try:
        cursor = cnx.cursor()
        query = "INSERT INTO request (mov_name) VALUES (%s)"
        values = (movie,)
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
