#Импорт библиотек и модулей
import wx #Интерфейс
from common.db import create_connection #Подключение к БД
from GUI.WindowsManager import WinManager #Менеджер окон
from repository import repository #Запросы к БД
cursor, connection = create_connection() #Подключение к БД

#При запуске программы
if __name__ == '__main__':
	app = wx.App() #Создание приложения
	WindowsManager = WinManager(cursor,connection,repository) #Класс менеджера окон
	WindowsManager.On_Create() #Создание окна
	app.MainLoop() #Запуск приложения

#Закрытие подключения
cursor.close()
connection.close()
print('Соединение закрыто')
print('Конец работы')