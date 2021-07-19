import wx
import wx.adv
import wx.grid
import datetime
import os
def receipts_window(cursor, connection, repository, WinManager, data):
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
			self.receipts_button.Enable(False)
			self.personal_button = wx.Button(self.settings_staticbox,wx.ID_ANY,'Личный кабинет',wx.DefaultPosition,wx.Size(120,21))
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
			self.receipts_boxsizer = wx.BoxSizer(wx.VERTICAL)
			self.add_receipt_font = wx.Font(24,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False)
			self.add_receipt_button = wx.Button(self.panel,wx.ID_ANY,'Добавить квитанцию',wx.DefaultPosition,wx.Size(320,40))
			self.add_receipt_button.SetFont(self.add_receipt_font)
			self.search_receipt_flexgridsizer = wx.FlexGridSizer(2,7,10,10)
			self.type_meter_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Тип счётчика')
			self.type_meter_combobox = wx.ComboBox(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.type_meter_combobox.Append('ГВС')
			self.type_meter_combobox.Append('ХВС')
			self.before_check_meter_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Показания от')
			self.before_check_meter_spinctrl = wx.SpinCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.before_check_meter_spinctrl.SetRange(1,99999999)
			self.before_check_meter_spinctrl.SetValue('')
			self.before_date_receipt_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Квитанции от')
			self.before_date_receipt_datepickerctrl = wx.adv.DatePickerCtrl(self.panel,wx.ID_ANY,wx.DefaultDateTime,wx.DefaultPosition,wx.Size(120,21),wx.adv.DP_DROPDOWN)
			self.after_check_meter_statictext = wx.StaticText(self.panel,wx.ID_ANY,'До')
			self.after_check_meter_spinctrl = wx.SpinCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.after_check_meter_spinctrl.SetRange(1,99999999)
			self.after_check_meter_spinctrl.SetValue('')
			self.after_date_receipt_statictext = wx.StaticText(self.panel,wx.ID_ANY,'До')
			self.after_date_receipt_datepickerctrl = wx.adv.DatePickerCtrl(self.panel,wx.ID_ANY,wx.DefaultDateTime,wx.DefaultPosition,wx.Size(120,21),wx.adv.DP_DROPDOWN)
			self.search_button = wx.Button(self.panel,wx.ID_ANY,'Найти',wx.DefaultPosition,wx.Size(120,21))
			self.drop_button = wx.Button(self.panel,wx.ID_ANY,'Сброс',wx.DefaultPosition,wx.Size(120,21))
			self.search_receipt_flexgridsizer.Add(self.type_meter_statictext)
			self.search_receipt_flexgridsizer.Add(self.type_meter_combobox)
			self.search_receipt_flexgridsizer.Add(self.before_check_meter_statictext)
			self.search_receipt_flexgridsizer.Add(self.before_check_meter_spinctrl)
			self.search_receipt_flexgridsizer.Add(self.before_date_receipt_statictext)
			self.search_receipt_flexgridsizer.Add(self.before_date_receipt_datepickerctrl)
			self.search_receipt_flexgridsizer.Add(self.search_button)
			self.search_receipt_flexgridsizer.AddSpacer(0)
			self.search_receipt_flexgridsizer.AddSpacer(0)
			self.search_receipt_flexgridsizer.Add(self.after_check_meter_statictext)
			self.search_receipt_flexgridsizer.Add(self.after_check_meter_spinctrl)
			self.search_receipt_flexgridsizer.Add(self.after_date_receipt_statictext)
			self.search_receipt_flexgridsizer.Add(self.after_date_receipt_datepickerctrl)
			self.search_receipt_flexgridsizer.Add(self.drop_button)
			data_for_meter = (self.user_id[0],)
			self.hot_water_id = repository.show_hot_water_meter_id_by_user_id(cursor,connection,data_for_meter)
			self.cold_water_id = repository.show_cold_water_meter_id_by_user_id(cursor,connection,data_for_meter)
			data_for_receipts = (self.hot_water_id[0],self.cold_water_id[0])
			self.receipts = repository.show_receipts_by_meter_id(cursor,connection,data_for_receipts)
			self.receipts_grid = wx.grid.Grid(self.panel,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,1))
			self.need_receipts = []
			for i in range(len(self.receipts)):
				if self.receipts[i][2] != None and self.receipts[i][2] != '' and self.receipts[i][3] != None and self.receipts[i][3] != '':
					self.need_receipts.append(self.receipts[i])
			self.need_receipts.sort(key = lambda tup: tup[1])
			lenght = int(len(self.need_receipts))
			self.receipts_grid.CreateGrid(lenght,4)
			self.receipts_grid.SetColLabelValue(0,'Тип счётчика')
			self.receipts_grid.SetColSize(0,245)
			self.receipts_grid.SetColLabelValue(1,'Начальное показание')
			self.receipts_grid.SetColSize(1,245)
			self.receipts_grid.SetColLabelValue(2,'Показание при оплате')
			self.receipts_grid.SetColSize(2,245)
			self.receipts_grid.SetColLabelValue(3,'Дата сдачи')
			self.receipts_grid.SetColSize(3,245)
			self.receipts_grid.EnableEditing(False)
			j = 0
			for i in range(lenght):
				if self.need_receipts[i][0] == self.hot_water_id[0]:
					self.receipts_grid.SetCellValue(i,0,'ГВС')
				elif self.need_receipts[i][0] == self.cold_water_id[0]:
					self.receipts_grid.SetCellValue(i,0,'ХВС')
				self.receipts_grid.SetCellValue(i,1,str(self.need_receipts[i][1]))
				self.receipts_grid.SetCellValue(i,2,str(self.need_receipts[i][2]))
				self.receipts_grid.SetCellValue(i,3,str(self.need_receipts[i][3]))
			self.receipts_boxsizer.Add(self.add_receipt_button,0,wx.ALIGN_RIGHT+wx.ALL,10)
			self.receipts_boxsizer.Add(self.search_receipt_flexgridsizer,0,wx.ALIGN_RIGHT+wx.ALL,10)
			self.receipts_boxsizer.Add(self.receipts_grid,1,wx.EXPAND)
			self.boxsizer.Add(self.settings_boxsizer)
			self.boxsizer.Add(self.boxes_staticline,0,wx.ALL,10)
			self.boxsizer.Add(self.receipts_boxsizer,1,wx.EXPAND)
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.Center()
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.meters_button.Bind(wx.EVT_BUTTON,self.ShowMeters, id = wx.ID_ANY)
			self.personal_button.Bind(wx.EVT_BUTTON,self.ShowPersonal, id = wx.ID_ANY)
			self.add_receipt_button.Bind(wx.EVT_BUTTON,self.AddReceipt, id = wx.ID_ANY)
			self.search_button.Bind(wx.EVT_BUTTON,self.SearchReceipt, id = wx.ID_ANY)
			self.drop_button.Bind(wx.EVT_BUTTON,self.DropReceipt, id = wx.ID_ANY)
			self.receipts_grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.ShowReceiptPhoto, id = wx.ID_ANY)

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
			WindowsManager.On_Next('show_receipts_window','show_meters_window',need_data)

		def ShowPersonal(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class new_data:
				def __init__(self,login):
					self.login = login
			need_data = new_data(data.login)
			self.Destroy()
			WindowsManager.On_Next('show_receipts_window','show_personal_window',need_data)

		def AddReceipt(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class data_to_add:
				def __init__(self,parent,hot_water_id,cold_water_id,grid):
					self.parent = parent
					self.hot_water_id = hot_water_id
					self.cold_water_id = cold_water_id
					self.grid = grid
			need_data = data_to_add(self,self.hot_water_id[0],self.cold_water_id[0],self.receipts_grid)
			WindowsManager.On_Next('show_receipts_window','add_receipt_window',need_data)

		def ShowReceiptPhoto(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class new_data:
				def __init__(self,photo,parent):
					self.photo = photo
					self.parent = parent
			row = event.GetRow()
			need_data = new_data(self.need_receipts[row][4],self)
			WindowsManager.On_Next('show_receipts_window','show_receipt_photo_window',need_data)

		def SearchReceipt(self,event):
			type_meter = self.type_meter_combobox.GetValue()
			if type_meter == 'ГВС':
				type_meter = self.hot_water_id[0]
			elif type_meter == 'ХВС':
				type_meter = self.cold_water_id[0]
			before_check_meter = self.before_check_meter_spinctrl.GetValue()
			after_check_meter = self.after_check_meter_spinctrl.GetValue()
			before_date_receipt_date = self.before_date_receipt_datepickerctrl.GetValue()
			after_date_receipt_date = self.after_date_receipt_datepickerctrl.GetValue()
			now = datetime.datetime.now()
			rows = []
			if type_meter != '':
				for i in range(len(self.need_receipts)):
					if self.need_receipts[i][0] == type_meter:
						rows.append(self.need_receipts[i])
				if self.receipts_grid.GetNumberRows()>0:
					self.receipts_grid.DeleteRows(0,self.receipts_grid.GetNumberRows())
			elif before_check_meter != '' and after_check_meter > 0:
				for i in range(len(self.need_receipts)):
					if self.need_receipts[i][1] >= before_check_meter and self.need_receipts[i][2] <= after_check_meter:
						rows.append(self.need_receipts[i])
				if self.receipts_grid.GetNumberRows()>0:
					self.receipts_grid.DeleteRows(0,self.receipts_grid.GetNumberRows())
			elif before_date_receipt_date != datetime.date(now.year,now.month,now.day) and after_date_receipt_date != datetime.date(now.year,now.month,now.day):
				before_date = 0
				before_day = before_date_receipt_date.GetDay()
				before_month = before_date_receipt_date.GetMonth()+1
				before_year = before_date_receipt_date.GetYear()
				before_date = datetime.date(before_year,before_month,before_day)
				after_date = 0
				after_day = after_date_receipt_date.GetDay()
				after_month = after_date_receipt_date.GetMonth()+1
				after_year = after_date_receipt_date.GetYear()
				after_date = datetime.date(after_year,after_month,after_day)
				for i in range(len(self.need_receipts)):
					if self.need_receipts[i][3] >= before_date and self.need_receipts[i][3] <= after_date:
						rows.append(self.need_receipts[i])
				if self.receipts_grid.GetNumberRows()>0:
					self.receipts_grid.DeleteRows(0,self.receipts_grid.GetNumberRows())
			for i in range(len(rows)):
				self.receipts_grid.AppendRows()
				if rows[i][0] == self.hot_water_id[0]:
					self.receipts_grid.SetCellValue(i,0,'ГВС')
				elif rows[i][0] == self.cold_water_id[0]:
					self.receipts_grid.SetCellValue(i,0,'ХВС')
				self.receipts_grid.SetCellValue(i,1,str(rows[i][1]))
				self.receipts_grid.SetCellValue(i,2,str(rows[i][2]))
				self.receipts_grid.SetCellValue(i,3,str(rows[i][3]))


		def DropReceipt(self,event):
			self.type_meter_combobox.SetValue('')
			self.before_check_meter_spinctrl.SetValue('')
			self.after_check_meter_spinctrl.SetValue('')
			datetime = wx.DateTime.Today()
			self.before_date_receipt_datepickerctrl.SetValue(datetime)
			self.after_date_receipt_datepickerctrl.SetValue(datetime)
			if self.receipts_grid.GetNumberRows()>0:
				self.receipts_grid.DeleteRows(0,self.receipts_grid.GetNumberRows())
			for i in range(len(self.need_receipts)):
				self.receipts_grid.AppendRows()
				if self.need_receipts[i][0] == self.hot_water_id[0]:
					self.receipts_grid.SetCellValue(i,0,'ГВС')
				elif self.need_receipts[i][0] == self.cold_water_id[0]:
					self.receipts_grid.SetCellValue(i,0,'ХВС')
				self.receipts_grid.SetCellValue(i,1,str(self.need_receipts[i][1]))
				self.receipts_grid.SetCellValue(i,2,str(self.need_receipts[i][2]))
				self.receipts_grid.SetCellValue(i,3,str(self.need_receipts[i][3]))

	frm = Frame(None, title=" ") #Создание элемента класса без предшествующих окон и с названием "Вход в систему"
	frm.SetMinSize(wx.Size(1280,720))
	frm.SetMaxSize(wx.Size(1280,720))
	frm.Show(True) #Окно становится модальным