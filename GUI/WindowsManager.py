from GUI.dialogs.start import create_start_window
from GUI.dialogs.restore_password import restore_password_window
from GUI.dialogs.registration import registration_window
from GUI.dialogs.add_meter import add_meter_window
from GUI.dialogs.show_receipt import show_receipt_photo_window
from GUI.dialogs.add_receipt import add_receipt_window
from GUI.show_meters import show_meters_window
from GUI.personal import personal_window
from GUI.receipts import receipts_window

class WinManager():

	#Объявление данных для работы с БД
	def __init__(self,cursor,connection,repository):
		self.cursor = cursor #Обозначение БД
		self.connection = connection #Подключение к БД
		self.repository = repository #Запросы к БД

	#При переходе назад
	def On_Back(self,now_panel,want_panel):
		if now_panel == '1':
			print(1)

	#При переходе вперёд
	def On_Next(self,now_panel,want_panel,data):
		if now_panel == 'create_start_window' and want_panel == 'show_meters_window':
			show_meters_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'create_start_window' and want_panel == 'restore_password_window':
			restore_password_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'create_start_window' and want_panel == 'registration_window':
			registration_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_meters_window' and want_panel == 'add_meter_window':
			add_meter_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_meters_window' and want_panel == 'show_personal_window':
			personal_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_meters_window' and want_panel == 'show_receipts_window':
			receipts_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_personal_window' and want_panel == 'show_meters_window':
			show_meters_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_personal_window' and want_panel == 'show_receipts_window':
			receipts_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_receipts_window' and want_panel == 'show_meters_window':
			show_meters_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_receipts_window' and want_panel == 'show_personal_window':
			personal_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_receipts_window' and want_panel == 'show_receipt_photo_window':
			show_receipt_photo_window(self.cursor, self.connection, self.repository, WinManager, data)
		elif now_panel == 'show_receipts_window' and want_panel == 'add_receipt_window':
			add_receipt_window(self.cursor, self.connection, self.repository, WinManager, data)
	#При создании окна
	def On_Create(self):
		create_start_window(self.cursor, self.connection, self.repository, WinManager)