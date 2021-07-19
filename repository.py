#Запросы к БД со значениями
from common.sql import requests

class repository():
	#Поиск пользователя по ID
	def search_user(cursor,connection,data):
		search_user = requests['search_user'] #SQL запрос
		cursor.execute(search_user,data) #Запрос к БД
		return cursor.fetchone() #Возврат полученных данных (fetchone - для одного, fetchall - для 2-ух и более)

	#Добавление пользователя
	def insert_user(cursor,connection,data):
		insert_user = requests['insert_user'] #SQL запрос
		cursor.execute(insert_user,data) #Запрос к БД
		connection.commit() #Сохранение в БД

	#Удаление пользователя
	def delete_user(cursor,connection,data):
		delete_user = requests['delete_user'] #SQL запрос
		cursor.execute(delete_user,data) #Запрос к БД
		connection.commit() #Сохранение в БД

	#Поиск пользователя по логину
	def search_user_by_login(cursor,connection,data):
		search_user_by_login = requests['search_user_by_login'] #SQL запрос
		cursor.execute(search_user_by_login,data) #Запрос к БД
		user = cursor.fetchone()
		return user #Возврат полученных данных

	#Поиск пользователя по логину и паролю
	def search_user_by_login_password(cursor,connection,data):
		search_user_by_login_password = requests['search_user_by_login_password'] #SQL запрос
		cursor.execute(search_user_by_login_password,data) #Запрос к БД
		new_user = cursor.fetchone()
		return new_user #Возврат полученных данных

	#Поиск секретного вопроса с ответом пользователя по логину
	def search_question_answer_by_login(cursor,connection,data):
		search_question_answer_by_login = requests['search_question_answer_by_login'] #SQL запрос
		cursor.execute(search_question_answer_by_login,data) #Запрос к БД
		question_and_answer = cursor.fetchone()
		return question_and_answer #Возврат полученных данных

	#Обновление пароля пользователя
	def update_password_by_login(cursor,connection,data):
		update_password_by_login = requests['update_password_by_login'] #SQL запрос
		cursor.execute(update_password_by_login,data) #Запрос к БД
		connection.commit() #Сохранение в БД

	#Добавление пользователя
	def add_user(cursor,connection,data):
		add_user = requests['add_user']
		cursor.execute(add_user,data)
		connection.commit()

	def update_user_question(cursor,connection,data):
		update_user_question = requests['update_user_question']
		cursor.execute(update_user_question,data)
		connection.commit()

	def update_user_answer(cursor,connection,data):
		update_user_answer = requests['update_user_answer']
		cursor.execute(update_user_answer,data)
		connection.commit()

	def update_user_surname(cursor,connection,data):
		update_user_surname = requests['update_user_surname']
		cursor.execute(update_user_surname,data)
		connection.commit()

	def update_user_name(cursor,connection,data):
		update_user_name = requests['update_user_name']
		cursor.execute(update_user_name,data)
		connection.commit()

	def update_user_patronymic(cursor,connection,data):
		update_user_patronymic = requests['update_user_patronymic']
		cursor.execute(update_user_patronymic,data)
		connection.commit()

	def update_user_address(cursor,connection,data):
		update_user_address = requests['update_user_address']
		cursor.execute(update_user_address,data)
		connection.commit()

	#Поиск ID пользователя по логину
	def search_user_id_by_login(cursor,connection,data):
		search_user_id_by_login = requests['search_user_id_by_login']
		cursor.execute(search_user_id_by_login,data)
		user_id = cursor.fetchone()
		return user_id

	#Установка состояния снятия для счётчиков при добавлении нового
	def delete_meter(cursor,connection,data):
		search_meter_id_by_user_id_type = requests['search_meter_id_by_user_id_type']
		cursor.execute(search_meter_id_by_user_id_type,data)
		meter_id = cursor.fetchone()
		delete_receipts = requests['delete_receipts']
		data_to_delete = (meter_id[0],)
		cursor.execute(delete_receipts,data_to_delete)
		delete_meter = requests['delete_meter']
		cursor.execute(delete_meter,data)
		connection.commit()

	#Добавление счётчика
	def add_meter(cursor,connection,data):
		add_meter = requests['add_meter']
		cursor.execute(add_meter,data)
		connection.commit()

	def update_saving_login(cursor,connection,data):
		update_saving_login = requests['update_saving_login']
		cursor.execute(update_saving_login,data)
		connection.commit()

	def update_saving_password(cursor,connection,data):
		update_saving_password = requests['update_saving_password']
		cursor.execute(update_saving_password,data)
		connection.commit()

	def update_saving_folder(cursor,connection,data):
		update_saving_folder = requests['update_saving_folder']
		cursor.execute(update_saving_folder,data)
		connection.commit()

	def select_save_login_password(cursor,connection):
		select_save_login_password = requests['select_save_login_password']
		cursor.execute(select_save_login_password)
		login_password = cursor.fetchone()
		return login_password

	def select_save_folder(cursor,connection):
		select_save_folder = requests['select_save_folder']
		cursor.execute(select_save_folder)
		folder = cursor.fetchone()
		return folder

	def show_personal(cursor,connection,data):
		show_personal = requests['show_personal']
		cursor.execute(show_personal,data)
		personal = cursor.fetchone()
		return personal

	def show_meters_by_user_id(cursor,connection,data):
		show_meters_by_user_id = requests['show_meters_by_user_id']
		cursor.execute(show_meters_by_user_id,data)
		meters = cursor.fetchall()
		return meters

	def delete_meters(cursor,connection,data):
		delete_meters = requests['delete_meters']
		cursor.execute(delete_meters,data)
		connection.commit()

	def delete_receipts(cursor,connection,data):
		delete_receipts = requests['delete_receipts']
		cursor.execute(delete_receipts,data)
		connection.commit()

	def delete_settings(cursor,connection):
		delete_settings_user = requests['delete_settings_user']
		cursor.execute(delete_settings_user)
		delete_settings_password = requests['delete_settings_password']
		cursor.execute(delete_settings_password)
		delete_settings_folder = requests['delete_settings_folder']
		cursor.execute(delete_settings_folder)

	def show_hot_water_meter_by_user_id(cursor,connection,data):
		show_hot_water_meter_by_user_id = requests['show_hot_water_meter_by_user_id']
		cursor.execute(show_hot_water_meter_by_user_id,data)
		hot_meter = cursor.fetchone()
		return hot_meter

	def show_cold_water_meter_by_user_id(cursor,connection,data):
		show_cold_water_meter_by_user_id = requests['show_cold_water_meter_by_user_id']
		cursor.execute(show_cold_water_meter_by_user_id,data)
		cold_meter = cursor.fetchone()
		return cold_meter

	def search_meter_id_by_user_id_type(cursor,connection,data):
		search_meter_id_by_user_id_type = requests['search_meter_id_by_user_id_type']
		cursor.execute(search_meter_id_by_user_id_type,data)
		meter_id = cursor.fetchone()
		return meter_id

	def add_receipt(cursor,connection,data):
		add_receipt = requests['add_receipt']
		cursor.execute(add_receipt,data)
		connection.commit()

	def show_id_receipts_by_meter(cursor,connection,data):
		show_id_receipts_by_meter = requests['show_id_receipts_by_meter']
		cursor.execute(show_id_receipts_by_meter,data)
		receipts_id = cursor.fetchall()
		return receipts_id

	def show_id_receipts(cursor,connection):
		show_id_receipts = requests['show_id_receipts']
		cursor.execute(show_id_receipts)
		receipts_id = cursor.fetchall()
		return receipts_id

	def update_reading(cursor,connection,data):
		update_reading = requests['update_reading']
		cursor.execute(update_reading,data)

	def update_date(cursor,connection,data):
		update_date = requests['update_date']
		cursor.execute(update_date,data)
		connection.commit()

	def update_receipt(cursor,connection,data):
		update_receipt = requests['update_receipt']
		cursor.execute(update_receipt,data)
		connection.commit()

	def show_hot_water_meter_id_by_user_id(cursor,connection,data):
		show_hot_water_meter_id_by_user_id = requests['show_hot_water_meter_id_by_user_id']
		cursor.execute(show_hot_water_meter_id_by_user_id,data)
		meter_id = cursor.fetchone()
		return meter_id

	def show_cold_water_meter_id_by_user_id(cursor,connection,data):
		show_cold_water_meter_id_by_user_id = requests['show_cold_water_meter_id_by_user_id']
		cursor.execute(show_cold_water_meter_id_by_user_id,data)
		meter_id = cursor.fetchone()
		return meter_id

	def show_receipts_by_meter_id(cursor,connection,data):
		show_receipts_by_meter_id = requests['show_receipts_by_meter_id']
		cursor.execute(show_receipts_by_meter_id,data)
		receipt_ids = cursor.fetchall()
		return receipt_ids

	def update_meter(cursor,connection,data):
		update_meter = requests['update_meter']
		cursor.execute(update_meter,data)
		connection.commit()

	def show_receipts_to_delete_by_meter_id(cursor,connection,data):
		show_receipts_to_delete_by_meter_id = requests['show_receipts_to_delete_by_meter_id']
		cursor.execute(show_receipts_to_delete_by_meter_id,data)
		receipt_ids = cursor.fetchone()
		return receipt_ids