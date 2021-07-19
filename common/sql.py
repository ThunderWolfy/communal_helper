#Запросы к БД в SQL виде
requests = {
#Поиск пользователя по ID
'search_user' : """SELECT login, password FROM users WHERE id = %s""",
#Добавление пользователя
'insert_user' : """INSERT INTO users (login, password) VALUES (%s, %s)""",
#Удаление пользователя
'delete_user' : """DELETE FROM users WHERE id = %s""",
#Поиск пользователя по логину
'search_user_by_login' : """SELECT login, password FROM users WHERE login = %s""",
#Поиск пользователя по логину и паролю
'search_user_by_login_password' : """SELECT login, password FROM users WHERE login = %s AND password = %s""",
#Поиск секретного вопроса с ответом пользователя по логину
'search_question_answer_by_login' : """SELECT question, answer FROM users WHERE login = %s""",
#Обновление пароля пользователя
'update_password_by_login' : """UPDATE users SET password = %s WHERE login = %s""",
#Добавление пользователя в БД
'add_user' : """INSERT INTO users (login,password,question,answer,surname,name,patronymic,registration_date, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
#Установка состояния снятия для счётчиков при добавлении нового
'delete_meter' : """DELETE FROM meters WHERE user_id = %s AND type_meter = %s""",
#Добавление счётчика
'add_meter' : """INSERT INTO meters (user_id,serial_number,type_meter,document_number,place_date,tariff, reading) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
#Поиск ID пользователя по логину
'search_user_id_by_login' : """SELECT id FROM users WHERE login = %s""",
'update_saving_password' : """UPDATE settings SET user_password = %s""",
'update_saving_login' : """UPDATE settings SET user_login = %s""",
'update_saving_folder' : """UPDATE settings SET folder = %s""",
'select_save_login_password' : """SELECT user_login, user_password FROM settings""",
'select_save_folder' : """SELECT folder FROM settings""",
'show_personal' : """SELECT login, password, question, answer, surname, name, patronymic, registration_date, address FROM users WHERE id = %s""",
'update_user_question' : """UPDATE users SET question = %s WHERE id = %s""",
'update_user_answer' : """UPDATE users SET answer = %s WHERE id = %s""",
'update_user_surname' : """UPDATE users SET surname = %s WHERE id = %s""",
'update_user_name' : """UPDATE users SET name = %s WHERE id = %s""",
'update_user_patronymic' : """UPDATE users SET patronymic = %s WHERE id = %s""",
'update_user_address' : """UPDATE users SET address = %s WHERE id = %s""",
'show_meters_by_user_id' : """SELECT id FROM meters WHERE user_id = %s""",
'delete_meters' : """DELETE FROM meters WHERE user_id = %s""",
'delete_receipts' : """DELETE FROM receipts WHERE meter = %s""",
'delete_settings_user' : """UPDATE settings SET user_login = ''""",
'delete_settings_password' : """UPDATE settings SET user_password = ''""",
'delete_settings_folder' : """UPDATE settings SET folder = ''""",
'show_hot_water_meter_by_user_id' : """SELECT serial_number, document_number, place_date, tariff, reading FROM meters WHERE user_id = %s AND type_meter = 'ГВС'""",
'show_cold_water_meter_by_user_id' : """SELECT serial_number, document_number, place_date, tariff, reading FROM meters WHERE user_id = %s AND type_meter = 'ХВС'""",
'search_meter_id_by_user_id_type' : """SELECT id FROM meters WHERE user_id = %s AND type_meter = %s""",
'add_receipt' : """INSERT INTO receipts (meter, start_reading) VALUES (%s, %s)""",
'show_id_receipts' : """SELECT id FROM receipts""",
'show_id_receipts_by_meter' : """SELECT id FROM receipts WHERE meter = %s""",
'update_reading' : """UPDATE receipts SET end_reading = %s WHERE meter = %s AND id = %s""",
'update_date' : """UPDATE receipts SET receipt_date = %s WHERE meter = %s AND id = %s""",
'update_receipt' : """UPDATE receipts SET receipt_photo = %s WHERE meter = %s AND id = %s""",
'show_hot_water_meter_id_by_user_id' : """SELECT id FROM meters WHERE user_id = %s AND type_meter = 'ГВС'""",
'show_cold_water_meter_id_by_user_id' : """SELECT id FROM meters WHERE user_id = %s AND type_meter = 'ХВС'""",
'show_receipts_by_meter_id' : """SELECT meter, start_reading, end_reading, receipt_date, receipt_photo FROM receipts WHERE meter = %s OR meter = %s""",
'show_receipts_to_delete_by_meter_id' : """SELECT receipt_photo FROM receipts WHERE meter = %s""",
'update_meter' : """UPDATE meters SET reading = %s WHERE user_id = %s AND type_meter = %s"""
}