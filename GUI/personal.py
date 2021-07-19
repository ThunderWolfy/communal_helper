import wx
import os
def personal_window(cursor, connection, repository, WinManager, data):
	#Класс диалогового окна
	class Frame(wx.Frame):
		#Функция при создании диалогого окна
		def __init__(self,*args,**kv):
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			data_for_db = (data.login,)
			self.user_id = repository.search_user_id_by_login(cursor, connection, data_for_db)
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.HORIZONTAL) #Контейнер для всех виджетов на панели
			self.settings_boxsizer = wx.BoxSizer(wx.VERTICAL) #Контейнер для настроек
			self.settings_staticbox = wx.StaticBox(self.panel,wx.ID_ANY,'')
			self.settings_staticbox_boxsizer = wx.BoxSizer(wx.VERTICAL)
			self.staticline = wx.StaticLine(self.settings_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(120,1))
			self.staticline1 = wx.StaticLine(self.settings_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(120,1))
			self.meters_button = wx.Button(self.settings_staticbox,wx.ID_ANY,'Счётчики',wx.DefaultPosition,wx.Size(120,21))
			self.receipts_button = wx.Button(self.settings_staticbox,wx.ID_ANY,'Квитанции',wx.DefaultPosition,wx.Size(120,21))
			self.personal_button = wx.Button(self.settings_staticbox,wx.ID_ANY,'Личный кабинет',wx.DefaultPosition,wx.Size(120,21))
			self.personal_button.Enable(False)
			self.settings_staticbox_boxsizer.AddStretchSpacer(1)
			self.settings_staticbox_boxsizer.AddSpacer(5)
			self.settings_staticbox_boxsizer.Add(self.meters_button,0,wx.CENTER+wx.ALL,10)
			self.settings_staticbox_boxsizer.Add(self.staticline,0,wx.CENTER)
			self.settings_staticbox_boxsizer.Add(self.receipts_button,0,wx.CENTER+wx.ALL,10)
			self.settings_staticbox_boxsizer.Add(self.staticline1,0,wx.CENTER)
			self.settings_staticbox_boxsizer.Add(self.personal_button,0,wx.CENTER+wx.ALL,10)
			self.settings_staticbox_boxsizer.AddStretchSpacer(1)
			self.settings_staticbox.SetSizer(self.settings_staticbox_boxsizer)
			self.settings_boxsizer.AddStretchSpacer(1)
			self.settings_boxsizer.Add(self.settings_staticbox,1,wx.ALIGN_LEFT+wx.ALL,10)
			self.settings_boxsizer.AddStretchSpacer(1)
			self.boxes_staticline = wx.StaticLine(self.panel,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,715))
			data_for_personal = (self.user_id[0],)
			self.personal = repository.show_personal(cursor,connection,data_for_personal)
			self.personal_flexgridsizer = wx.FlexGridSizer(6,2,10,10)
			self.question_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Секретный вопрос')
			self.question_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,self.personal[2],wx.DefaultPosition,wx.Size(500,21))
			self.answer_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Ответ на секретный вопрос')
			self.answer_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,self.personal[3],wx.DefaultPosition,wx.Size(500,21))
			self.surname_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Фамилия')
			self.surname_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,self.personal[4],wx.DefaultPosition,wx.Size(500,21))
			self.name_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Имя')
			self.name_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,self.personal[5],wx.DefaultPosition,wx.Size(500,21))
			self.patronymic_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Отчество (при наличии)')
			self.patronymic_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,self.personal[6],wx.DefaultPosition,wx.Size(500,21))
			self.address_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Адрес проживания')
			self.address_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,self.personal[8],wx.DefaultPosition,wx.Size(500,21))
			self.personal_flexgridsizer.Add(self.question_statictext)
			self.personal_flexgridsizer.Add(self.question_textctrl)
			self.personal_flexgridsizer.Add(self.answer_statictext)
			self.personal_flexgridsizer.Add(self.answer_textctrl)
			self.personal_flexgridsizer.Add(self.surname_statictext)
			self.personal_flexgridsizer.Add(self.surname_textctrl)
			self.personal_flexgridsizer.Add(self.name_statictext)
			self.personal_flexgridsizer.Add(self.name_textctrl)
			self.personal_flexgridsizer.Add(self.patronymic_statictext)
			self.personal_flexgridsizer.Add(self.patronymic_textctrl)
			self.personal_flexgridsizer.Add(self.address_statictext)
			self.personal_flexgridsizer.Add(self.address_textctrl)
			self.for_buttons_box = wx.BoxSizer(wx.VERTICAL)
			self.buttons_box = wx.BoxSizer(wx.HORIZONTAL)
			self.change_button = wx.Button(self.panel,wx.ID_ANY,'Изменить данные',wx.DefaultPosition,wx.Size(150,21))
			self.delete_button = wx.Button(self.panel,wx.ID_ANY,'Удалить аккаунт',wx.DefaultPosition,wx.Size(150,21))
			self.buttons_box.Add(self.change_button,0)
			self.buttons_box.AddSpacer(10)
			self.buttons_box.Add(self.delete_button,0)
			self.for_buttons_box.Add(self.buttons_box,0,wx.CENTER+wx.TOP,625)
			self.boxsizer.Add(self.settings_boxsizer)
			self.boxsizer.Add(self.boxes_staticline,0,wx.ALL,10)
			self.boxsizer.Add(self.personal_flexgridsizer,0,wx.CENTER+wx.LEFT,100)
			self.boxsizer.Add(self.for_buttons_box,0,wx.ALL,10)
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.Center()
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.meters_button.Bind(wx.EVT_BUTTON,self.ShowMeters, id = wx.ID_ANY)
			self.receipts_button.Bind(wx.EVT_BUTTON,self.ShowReceipts, id = wx.ID_ANY)
			self.change_button.Bind(wx.EVT_BUTTON, self.ChangePersonal, id = wx.ID_ANY)
			self.delete_button.Bind(wx.EVT_BUTTON, self.DeletePersonal, id = wx.ID_ANY)

		#Функция при закрытии окна
		def OnClose(self,event):
			yes = wx.MessageBox('Желаете закончить работу приложения?',' ',wx.YES_NO+wx.ICON_INFORMATION)
			if yes == wx.YES:
				self.Destroy()

		def ShowMeters(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class new_data:
				def __init__(self,login):
					self.login = login
			need_data = new_data(data.login)
			self.Destroy()
			WindowsManager.On_Next('show_personal_window','show_meters_window',need_data)

		def ShowReceipts(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class new_data:
				def __init__(self,login):
					self.login = login
			need_data = new_data(data.login)
			self.Destroy()
			WindowsManager.On_Next('show_personal_window','show_receipts_window',need_data)

		def ChangePersonal(self,event):
			question = str(self.question_textctrl.GetValue())
			answer = str(self.answer_textctrl.GetValue())
			surname = str(self.surname_textctrl.GetValue())
			name = str(self.name_textctrl.GetValue())
			patronymic = str(self.patronymic_textctrl.GetValue())
			address = str(self.address_textctrl.GetValue())
			user_id = str(self.user_id[0])
			if question != '' and answer != '' and surname != '' and name != '' and address != '':
				data_to_change = (question,user_id)
				repository.update_user_question(cursor,connection,data_to_change)
				data_to_change = (answer,user_id)
				repository.update_user_answer(cursor,connection,data_to_change)
				data_to_change = (surname,user_id)
				repository.update_user_surname(cursor,connection,data_to_change)
				data_to_change = (name,user_id)
				repository.update_user_name(cursor,connection,data_to_change)
				data_to_change = (patronymic,user_id)
				repository.update_user_patronymic(cursor,connection,data_to_change)
				data_to_change = (address,user_id)
				repository.update_user_address(cursor,connection,data_to_change)
				wx.MessageBox('Данные успешно обновлены',' ',wx.OK+wx.ICON_INFORMATION)
			else:
				wx.MessageBox('Не заполнено одно из полей','Ошибка',wx.OK+wx.ICON_ERROR)

		def DeletePersonal(self,event):
			repository.delete_settings(cursor,connection)
			data_to_delete = (str(self.user_id[0]),)
			meters = repository.show_meters_by_user_id(cursor,connection,data_to_delete)
			for item in range(len(meters)):
				need_id = "".join(c for c in str(meters[item]) if c.isalnum())
				meter_to_delete = (str(need_id),)
				receipts = repository.show_receipts_to_delete_by_meter_id(cursor,connection,meter_to_delete)
				os.remove(receipts[0])
				repository.delete_receipts(cursor,connection,meter_to_delete)
			repository.delete_meters(cursor,connection,data_to_delete)
			repository.delete_user(cursor,connection,data_to_delete)
			wx.MessageBox('Пользователь успешно удалён',' ',wx.OK+wx.ICON_INFORMATION)
			self.Destroy()


	frm = Frame(None, title=" ") #Создание элемента класса без предшествующих окон и с названием "Вход в систему"
	frm.SetMinSize(wx.Size(1280,720))
	frm.SetMaxSize(wx.Size(1280,720))
	frm.Show(True) #Окно становится модальным