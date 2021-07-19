import wx
import os
def create_start_window(cursor, connection, repository, WinManager):
	#Класс диалогового окна
	class Frame(wx.Dialog):
		#Функция при создании диалогого окна
		def __init__(self,*args,**kv):
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.VERTICAL) #Контейнер со всеми виджетами на панели
			self.flexgridsizer = wx.FlexGridSizer(3,2,10,10) #Контейнер для логина и пароля
			self.login_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Логин') #Текст "Логин"
			self.login_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(200,21)) #Поле для ввода логина
			self.password_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Пароль') #Текст "Пароль"
			self.password_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(200,21)) #Поле для ввода пароля
			self.save_data_checkbox = wx.CheckBox(self.panel,wx.ID_ANY,'Запомнить мой пароль',wx.DefaultPosition)
			self.flexgridsizer.Add(self.login_statictext) #Добавление в контейнер для логина и пароля текста "Логин"
			self.flexgridsizer.Add(self.login_textctrl) #Добавление в контейнер для логина и пароля поле для ввода логина
			self.flexgridsizer.Add(self.password_statictext) #Добавление в контейнер для логина и пароля текста "Пароль"
			self.flexgridsizer.Add(self.password_textctrl) #Добавление в контейнер для логина и пароля поле для ввода пароля
			self.flexgridsizer.AddSpacer(0)
			self.flexgridsizer.Add(self.save_data_checkbox)
			login_password = repository.select_save_login_password(cursor,connection)
			if login_password != None:
				self.login_textctrl.SetValue(login_password[0])
				self.password_textctrl.SetValue(login_password[1])
				self.save_data_checkbox.SetValue(True)
			self.buttons_boxsizer = wx.BoxSizer(wx.HORIZONTAL)
			self.enter_button = wx.Button(self.panel,wx.ID_ANY,'Войти',wx.DefaultPosition,wx.Size(50,21)) #Кнопка "Войти"
			self.cancel_button = wx.Button(self.panel,wx.ID_ANY,'Отмена',wx.DefaultPosition,wx.Size(50,21)) #Кнопка "Отмена"
			self.buttons_boxsizer.Add(self.enter_button)
			self.buttons_boxsizer.AddSpacer(10)
			self.buttons_boxsizer.Add(self.cancel_button)
			self.staticline = wx.StaticLine(self.panel,wx.ID_ANY,wx.DefaultPosition,wx.Size(350,1))
			self.help_flexgridsizer = wx.FlexGridSizer(2,2,10,10)
			self.forget_password_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Забыли пароль?')
			self.forget_password_button = wx.Button(self.panel,wx.ID_ANY,'Восстановить пароль',wx.DefaultPosition,wx.Size(200,21))
			self.create_account_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Нет аккаунта?')
			self.create_account_button = wx.Button(self.panel,wx.ID_ANY,'Создать новый аккаунт',wx.DefaultPosition,wx.Size(200,21))
			self.help_flexgridsizer.Add(self.forget_password_statictext)
			self.help_flexgridsizer.Add(self.forget_password_button)
			self.help_flexgridsizer.Add(self.create_account_statictext)
			self.help_flexgridsizer.Add(self.create_account_button)
			self.boxsizer.AddStretchSpacer(1) #Установка пробела между вверхом окна и контейнером со всеми виджетами на панели
			self.boxsizer.Add(self.flexgridsizer,0,wx.ALIGN_RIGHT+wx.ALL,20) #Установка контейнера для логина и пароля по середине
			self.boxsizer.Add(self.buttons_boxsizer,0,wx.ALIGN_RIGHT+wx.RIGHT,20) #Установка кнопки в правом нижнем углу с отступом 10 со всех сторон
			self.boxsizer.Add(self.staticline,0,wx.ALIGN_CENTER+wx.ALL,20)
			self.boxsizer.Add(self.help_flexgridsizer,0,wx.ALIGN_RIGHT+wx.RIGHT,20)
			self.boxsizer.AddStretchSpacer(1) #Установка пробела между низом окна и контейнером со всеми виджетами на панели
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.Center()
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.enter_button.Bind(wx.EVT_BUTTON, self.EnterInTheSystem, id = wx.ID_ANY) #Установка действия при нажатии на кнопку "Войти"
			self.cancel_button.Bind(wx.EVT_BUTTON, self.OnClose, id = wx.ID_ANY) #Установка действия при нажатии на кнопку "Отмена"
			self.forget_password_button.Bind(wx.EVT_BUTTON, self.RestorePassword, id = wx.ID_ANY)
			self.create_account_button.Bind(wx.EVT_BUTTON, self.CreateAccount, id = wx.ID_ANY)

		#Функция при закрытии окна
		def OnClose(self,event):
			self.Destroy() #Разрушение экрана

		#Функция при нажатии на кнопку "Войти в систему"
		def EnterInTheSystem(self,event):
			login = self.login_textctrl.GetValue() #Данные из поля для ввода логина
			password = self.password_textctrl.GetValue() #Данные из поля для ввода пароля
			login_for_save = login
			password_for_save = password
			if login != '' and password != '':
				data = (login,) #Данные для запроса в БД
				user = repository.search_user_by_login(cursor,connection,data) #Запрос в БД с поиском пользователя по логину
				#Если найден пользователь
				if user != None:
					new_data = (login,password)
					user_with_password = repository.search_user_by_login_password(cursor,connection,new_data) #Запрос в БД с поиском по логину и паролю
					if self.save_data_checkbox.IsChecked:
						data = (password,)
						repository.update_saving_password(cursor,connection,data)
						data = (login,)
						repository.update_saving_login(cursor,connection,data)
						data = (os.getcwd(),)
						repository.update_saving_folder(cursor,connection,data)
					if user_with_password != None:
						self.Destroy()
						WindowsManager = WinManager(cursor,connection,repository)
						class data:
							def __init__(self,login):
								self.login = login
						need_data = data(login)
						WindowsManager.On_Next('create_start_window','show_meters_window',need_data)
					else:
						replace = wx.MessageBox('Указан не правильный пароль.\nВосстановить пароль?',' ',wx.YES_NO+wx.ICON_INFORMATION) #Сообщение с предложением восстановить пароль
						#Если нажали да
						if replace == wx.YES:
							WindowsManager = WinManager(cursor,connection,repository)
							class data:
								def __init__(self,login):
									self.login = login
							need_data = data(login)
							self.login_textctrl.SetValue('')
							self.password_textctrl.SetValue('')
							WindowsManager.On_Next('create_start_window','restore_password_window',need_data)
				#Иначе
				else:
					yesno = wx.MessageBox('Данного пользователя нет в БД.\nЖелаете зарегистрироваться?','Новый пользователь',wx.YES_NO+wx.ICON_INFORMATION) #Сообщение с предложением зарегистрировать нового пользователя
					#Если нажали да
					if yesno == wx.YES:
						WindowsManager = WinManager(cursor,connection,repository)
						need_data = ''
						self.login_textctrl.SetValue('')
						self.password_textctrl.SetValue('')
						WindowsManager.On_Next('create_start_window','registration_window',need_data)
			else:
				wx.MessageBox('Не заполнено одно из полей','Ошибка',wx.OK+wx.ICON_ERROR)

		def RestorePassword(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class data:
				def __init__(self,login):
					self.login = login
			data_for_db = (self.login_textctrl.GetValue(),)
			self.question_and_answer = repository.search_question_answer_by_login(cursor, connection, data_for_db)
			if self.question_and_answer != None:
				need_data = data(self.login_textctrl.GetValue())
				self.login_textctrl.SetValue('')
				self.password_textctrl.SetValue('')
				WindowsManager.On_Next('create_start_window','restore_password_window',need_data)
			else:
				wx.MessageBox('Данного пользователя нет в БД','Ошибка',wx.OK+wx.ICON_ERROR)

		def CreateAccount(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			need_data = ''
			self.login_textctrl.SetValue('')
			self.password_textctrl.SetValue('')
			WindowsManager.On_Next('create_start_window','registration_window',need_data)


	frm = Frame(None, title="Вход в систему") #Создание элемента класса без предшествующих окон и с названием "Вход в систему"
	frm.SetSize(375,325)
	frm.ShowModal() #Окно становится модальным