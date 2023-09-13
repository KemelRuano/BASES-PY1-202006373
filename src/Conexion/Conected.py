import mysql.connector

db = {
    'host': "localhost",
    'user': 'root',
    'password': 'mysql',
    'port': '3306'
}

def query(query):
    try:
            connection = mysql.connector.connect(**db)
            cursor = connection.cursor()
            cursor.execute(query)
             
            cursor.close()
            connection.close()
            
    except mysql.connector.Error as err:
        return False
 

