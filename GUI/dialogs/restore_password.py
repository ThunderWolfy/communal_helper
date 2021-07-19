import wx

def restore_password_window(cursor, connection, repository, WindowsManager, data):
	#Класс диалогового окна
	class Frame(wx.Dialog):
		#Функция при создании диалогого окна
		def __init__(self,*args,**kv):
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			data_for_db = (data.login,)
			self.question_and_answer = repository.search_question_answer_by_login(cursor, connection, data_for_db)
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.VERTICAL) #Контейнер со всеми виджетами на панели
			self.flexgridsizer = wx.FlexGridSizer(3,2,10,10)
			self.question_statictext = wx.StaticText(self.panel,wx.ID_ANY,self.question_and_answer[0])
			self.answer_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.new_password_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Новый пароль')
			self.new_password_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.again_password_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Подтвердить пароль')
			self.again_password_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.save_button = wx.Button(self.panel,wx.ID_ANY,'Сохранить',wx.DefaultPosition,wx.Size(120,21))
			self.flexgridsizer.Add(self.question_statictext)
			self.flexgridsizer.Add(self.answer_textctrl)
			self.flexgridsizer.Add(self.new_password_statictext)
			self.flexgridsizer.Add(self.new_password_textctrl)
			self.flexgridsizer.Add(self.again_password_statictext)
			self.flexgridsizer.Add(self.again_password_textctrl)
			self.boxsizer.AddStretchSpacer(1) #Установка пробела между вверхом окна и контейнером для логина и пароля
			self.boxsizer.Add(self.flexgridsizer,0,wx.ALIGN_CENTER) #Установка контейнера для логина и пароля по середине
			self.boxsizer.AddStretchSpacer(1) #Установка пробела между низом окна и контейнером для логина и пароля
			self.boxsizer.Add(self.save_button,0,wx.ALIGN_RIGHT+wx.ALL,10) #Установка кнопки в правом нижнем углу с отступом 10 со всех сторон
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.Center()
			self.save_button.Bind(wx.EVT_BUTTON, self.SavePassword, id = wx.ID_ANY) #Установка действия при нажатии на кнопку "Сохранить"

		#Функция при закрытии окна
		def OnClose(self,event):
			self.Destroy() #Разрушение экрана

		#Функция при нажатии на кнопку "Сохранить"
		def SavePassword(self,event):
			answer = self.answer_textctrl.GetValue()
			new_password = self.new_password_textctrl.GetValue()
			again_password = self.again_password_textctrl.GetValue()
			if answer != '' and new_password != '' and again_password != '':
				if answer == self.question_and_answer[1]:
					if new_password == again_password:
						data_for_update = (new_password,data.login)
						repository.update_password_by_login(cursor, connection, data_for_update)
						wx.MessageBox('Пароль успешно изменён',' ',wx.OK+wx.ICON_INFORMATION)
						self.Destroy()
					else:
						wx.MessageBox('Пароли не совпадают','Ошибка',wx.OK+wx.ICON_ERROR)
				else:
					wx.MessageBox('Неправильный ответ на секретный вопрос','Ошибка',wx.OK+wx.ICON_ERROR)
			else:
				wx.MessageBox('Не заполнено одно из полей','Ошибка',wx.OK+wx.ICON_ERROR)

	frm = Frame(None, title="Восстановление пароля") #Создание элемента класса без предшествующих окон и с названием "Восстановление пароля"
	frm.SetSize(275,225)
	frm.ShowModal() #Окно становится модальным