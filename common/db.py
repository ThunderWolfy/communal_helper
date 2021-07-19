import psycopg2
from psycopg2 import OperationalError
def create_connection():
    connection = None
    try:
        #Подключение к БД
    	connection = psycopg2.connect(database="practice", user="postgres")
    	cursor = connection.cursor() 
    except OperationalError as e:
        print(f"Ошибка: '{e}'")
    finally:
    	if connection:
    		print('Соединение открыто')
    return cursor,connection