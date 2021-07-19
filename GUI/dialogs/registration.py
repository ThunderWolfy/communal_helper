import wx
import datetime
def registration_window(cursor, connection, repository, WindowsManager, data):
	#Класс диалогового окна
	class Frame(wx.Dialog):
		#Функция при создании диалогого окна
		def __init__(self,*args,**kv):
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.VERTICAL) #Контейнер со всеми виджетами на панели
			self.flexgridsizer = wx.FlexGridSizer(8,2,10,10) #Контейнер для логина и пароля
			self.login_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Логин(*)') #Текст "Логин"
			self.login_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.password_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Пароль(*)') #Текст "Пароль"
			self.password_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.question_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Секретный вопрос(*)') #Текст "Секретный вопрос"
			self.question_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.answer_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Ответ на вопрос(*)') #Текст "Ответ на вопрос"
			self.answer_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.surname_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Фамилия(*)') #Текст "Фамилия"
			self.surname_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.name_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Имя(*)') #Текст "Имя"
			self.name_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.patronymic_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Отчество (при наличии)') #Текст "Отчество (при наличии)"
			self.patronymic_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.address_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Адрес проживания(*)')
			self.address_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'', wx.DefaultPosition,wx.Size(120,21))
			self.flexgridsizer.Add(self.login_statictext)
			self.flexgridsizer.Add(self.login_textctrl)
			self.flexgridsizer.Add(self.password_statictext)
			self.flexgridsizer.Add(self.password_textctrl)
			self.flexgridsizer.Add(self.question_statictext)
			self.flexgridsizer.Add(self.question_textctrl)
			self.flexgridsizer.Add(self.answer_statictext)
			self.flexgridsizer.Add(self.answer_textctrl)
			self.flexgridsizer.Add(self.surname_statictext)
			self.flexgridsizer.Add(self.surname_textctrl)
			self.flexgridsizer.Add(self.name_statictext)
			self.flexgridsizer.Add(self.name_textctrl)
			self.flexgridsizer.Add(self.patronymic_statictext)
			self.flexgridsizer.Add(self.patronymic_textctrl)
			self.flexgridsizer.Add(self.address_statictext)
			self.flexgridsizer.Add(self.address_textctrl)
			self.note_statictext = wx.StaticText(self.panel,wx.ID_ANY,'* - обязательное поле')
			self.save_button = wx.Button(self.panel,wx.ID_ANY,'Сохранить',wx.DefaultPosition,wx.Size(120,21))
			self.boxsizer.AddStretchSpacer(1) #Установка пробела между вверхом окна и контейнером для логина и пароля
			self.boxsizer.Add(self.flexgridsizer,0,wx.ALIGN_CENTER) #Установка контейнера для логина и пароля по середине
			self.boxsizer.AddStretchSpacer(1) #Установка пробела между низом окна и контейнером для логина и пароля
			self.boxsizer.Add(self.note_statictext,0,wx.ALIGN_CENTER)
			self.boxsizer.Add(self.save_button,0,wx.ALIGN_RIGHT+wx.ALL,10) #Установка кнопки в правом нижнем углу с отступом 10 со всех сторон
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.Center()
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.save_button.Bind(wx.EVT_BUTTON, self.AddUser, id = wx.ID_ANY) #Установка действия при нажатии на кнопку "Сохранить"
			
		#Функция при закрытии окна
		def OnClose(self,event):
			self.Destroy() #Разрушение экрана

		#Функция при нажатии на кнопку "Сохранить"
		def AddUser(self,event):
			login = self.login_textctrl.GetValue()
			password = self.password_textctrl.GetValue()
			question = self.question_textctrl.GetValue()
			answer = self.answer_textctrl.GetValue()
			surname = self.surname_textctrl.GetValue()
			name = self.name_textctrl.GetValue()
			patronymic = self.patronymic_textctrl.GetValue()
			address = self.address_textctrl.GetValue()
			now = datetime.datetime.now()
			date = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
			if login != '' and password != '' and question != '' and answer != '' and surname != '' and name != '' and address != '':
				data_to_add_user = (login,password,question,answer,surname,name,patronymic,date,address)
				repository.add_user(cursor, connection, data_to_add_user)
				wx.MessageBox('Пользователь успешно добавлен!', ' ', wx.OK+wx.ICON_INFORMATION)
				self.Destroy()
			else:
				wx.MessageBox('Не заполнено одно из обязательных полей!', 'Ошибка', wx.OK+wx.ICON_ERROR)

	frm = Frame(None, title="Вход в систему") #Создание элемента класса без предшествующих окон и с названием "Вход в систему"
	frm.SetSize(425,375)
	frm.ShowModal() #Окно становится модальным