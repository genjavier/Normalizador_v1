import pymysql



def getConnection():
    connection = pymysql.connect("localhost", "root", "", "AI_bd")
    return connection


def select_region(sql):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor
    finally:
        connection.close()

def select(sql):
    connection = getConnection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor
    finally:
        connection.close()

