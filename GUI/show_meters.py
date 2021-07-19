import wx
import wx.adv
import random
def show_meters_window(cursor, connection, repository, WinManager, data):
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
			self.meters_button.Enable(False)
			self.receipts_button = wx.Button(self.settings_staticbox,wx.ID_ANY,'Квитанции',wx.DefaultPosition,wx.Size(120,21))
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
			self.meters_boxsizer = wx.BoxSizer(wx.VERTICAL)
			self.add_meter_font = wx.Font(24,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False)
			self.add_meter_button = wx.Button(self.panel,wx.ID_ANY,'Добавить счётчик',wx.DefaultPosition,wx.Size(280,40))
			self.add_meter_button.SetFont(self.add_meter_font)
			data_for_meter = (self.user_id[0],)
			self.about_hot_water = repository.show_hot_water_meter_by_user_id(cursor,connection,data_for_meter)
			self.about_cold_water = repository.show_cold_water_meter_by_user_id(cursor,connection,data_for_meter)
			self.waters_box = wx.BoxSizer(wx.HORIZONTAL)
			self.font = wx.Font(48,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False)
			self.hot_water_staticbox = wx.StaticBox(self.panel,wx.ID_ANY,'Счётчик горячей воды')
			self.hot_water_box = wx.BoxSizer(wx.VERTICAL)
			self.hot_water_numbers = wx.BoxSizer(wx.HORIZONTAL)
			self.hot_water_number_1 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_1.SetFont(self.font)
			self.hot_water_number_1.Enable(False)
			self.hot_water_staticline1 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_2 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_2.SetFont(self.font)
			self.hot_water_number_2.Enable(False)
			self.hot_water_staticline2 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_3 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_3.SetFont(self.font)
			self.hot_water_number_3.Enable(False)
			self.hot_water_staticline3 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_4 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_4.SetFont(self.font)
			self.hot_water_number_4.Enable(False)
			self.hot_water_staticline4 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_5 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_5.SetFont(self.font)
			self.hot_water_number_5.Enable(False)
			self.hot_water_staticline5 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_6 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_6.SetFont(self.font)
			self.hot_water_number_6.Enable(False)
			self.hot_water_staticline6 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_7 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_7.SetFont(self.font)
			self.hot_water_number_7.Enable(False)
			self.hot_water_staticline7 = wx.StaticLine(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.hot_water_number_8 = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.hot_water_number_8.SetFont(self.font)
			self.hot_water_number_8.Enable(False)
			self.hot_water_numbers.Add(self.hot_water_number_1)
			self.hot_water_numbers.Add(self.hot_water_staticline1)
			self.hot_water_numbers.Add(self.hot_water_number_2)
			self.hot_water_numbers.Add(self.hot_water_staticline2)
			self.hot_water_numbers.Add(self.hot_water_number_3)
			self.hot_water_numbers.Add(self.hot_water_staticline3)
			self.hot_water_numbers.Add(self.hot_water_number_4)
			self.hot_water_numbers.Add(self.hot_water_staticline4)
			self.hot_water_numbers.Add(self.hot_water_number_5)
			self.hot_water_numbers.Add(self.hot_water_staticline5)
			self.hot_water_numbers.Add(self.hot_water_number_6)
			self.hot_water_numbers.Add(self.hot_water_staticline6)
			self.hot_water_numbers.Add(self.hot_water_number_7)
			self.hot_water_numbers.Add(self.hot_water_staticline7)
			self.hot_water_numbers.Add(self.hot_water_number_8)
			self.hot_water_box.Add(self.hot_water_numbers,0,wx.CENTER+wx.ALL,30)
			self.hot_water_flexgridsizer = wx.FlexGridSizer(4,2,80,20)
			self.hot_water_serial_number_statictext = wx.StaticText(self.hot_water_staticbox,wx.ID_ANY,'Серийный номер')
			self.hot_water_serial_number_textctrl = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(270,21))
			self.hot_water_document_number_statictext = wx.StaticText(self.hot_water_staticbox,wx.ID_ANY,'№ документа')
			self.hot_water_document_number_textctrl = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(270,21))
			self.hot_water_place_date_statictext = wx.StaticText(self.hot_water_staticbox,wx.ID_ANY,'Дата установки')
			self.hot_water_place_date_datepickerctrl = wx.adv.DatePickerCtrl(self.hot_water_staticbox,wx.ID_ANY,wx.DefaultDateTime,wx.DefaultPosition,wx.Size(270,21))
			self.hot_water_tariff_statictext = wx.StaticText(self.hot_water_staticbox,wx.ID_ANY,'Тариф (руб. за кв.м.)')
			self.hot_water_tariff_textctrl = wx.TextCtrl(self.hot_water_staticbox,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(270,21))
			self.hot_water_serial_number_textctrl.Enable(False)
			self.hot_water_document_number_textctrl.Enable(False)
			self.hot_water_place_date_datepickerctrl.Enable(False)
			self.hot_water_tariff_textctrl.Enable(False)
			if self.about_hot_water != None:
				self.hot_water_serial_number_textctrl.SetValue(str(self.about_hot_water[0]))
				self.hot_water_document_number_textctrl.SetValue(str(self.about_hot_water[1]))
				self.hot_water_place_date_datepickerctrl.SetValue(self.about_hot_water[2])
				self.hot_water_tariff_textctrl.SetValue(str(self.about_hot_water[3]))
				if len(str(self.about_hot_water[4])) == 1:
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[0])
				elif len(str(self.about_hot_water[4])) == 2:
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[1])
				elif len(str(self.about_hot_water[4])) == 3:
					self.hot_water_number_6.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[1])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[2])
				elif len(str(self.about_hot_water[4])) == 4:
					self.hot_water_number_5.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_6.SetValue(str(self.about_hot_water[4])[1])
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[2])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[3])
				elif len(str(self.about_hot_water[4])) == 5:
					self.hot_water_number_4.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_5.SetValue(str(self.about_hot_water[4])[1])
					self.hot_water_number_6.SetValue(str(self.about_hot_water[4])[2])
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[3])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[4])
				elif len(str(self.about_hot_water[4])) == 6:
					self.hot_water_number_3.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_4.SetValue(str(self.about_hot_water[4])[1])
					self.hot_water_number_5.SetValue(str(self.about_hot_water[4])[2])
					self.hot_water_number_6.SetValue(str(self.about_hot_water[4])[3])
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[4])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[5])
				elif len(str(self.about_hot_water[4])) == 7:
					self.hot_water_number_2.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_3.SetValue(str(self.about_hot_water[4])[1])
					self.hot_water_number_4.SetValue(str(self.about_hot_water[4])[2])
					self.hot_water_number_5.SetValue(str(self.about_hot_water[4])[3])
					self.hot_water_number_6.SetValue(str(self.about_hot_water[4])[4])
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[5])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[6])
				elif len(str(self.about_hot_water[4])) == 8:
					self.hot_water_number_1.SetValue(str(self.about_hot_water[4])[0])
					self.hot_water_number_2.SetValue(str(self.about_hot_water[4])[1])
					self.hot_water_number_3.SetValue(str(self.about_hot_water[4])[2])
					self.hot_water_number_4.SetValue(str(self.about_hot_water[4])[3])
					self.hot_water_number_5.SetValue(str(self.about_hot_water[4])[4])
					self.hot_water_number_6.SetValue(str(self.about_hot_water[4])[5])
					self.hot_water_number_7.SetValue(str(self.about_hot_water[4])[6])
					self.hot_water_number_8.SetValue(str(self.about_hot_water[4])[7])
				user_id = self.user_id[0]
				serial_number = self.about_hot_water[0]
				type_meter = 'ГВС'
				document_number = self.about_hot_water[1]
				place_date = self.about_hot_water[2]
				tariff = self.about_hot_water[3]
				reading = self.about_hot_water[4]+random.randint(1,10)
				data_for_add = (str(reading),str(user_id),'ГВС')
				repository.update_meter(cursor,connection,data_for_add)
			self.hot_water_flexgridsizer.Add(self.hot_water_serial_number_statictext)
			self.hot_water_flexgridsizer.Add(self.hot_water_serial_number_textctrl)
			self.hot_water_flexgridsizer.Add(self.hot_water_document_number_statictext)
			self.hot_water_flexgridsizer.Add(self.hot_water_document_number_textctrl)
			self.hot_water_flexgridsizer.Add(self.hot_water_place_date_statictext)
			self.hot_water_flexgridsizer.Add(self.hot_water_place_date_datepickerctrl)
			self.hot_water_flexgridsizer.Add(self.hot_water_tariff_statictext)
			self.hot_water_flexgridsizer.Add(self.hot_water_tariff_textctrl)
			self.hot_water_box.Add(self.hot_water_flexgridsizer,0,wx.CENTER+wx.ALL,30)
			self.hot_water_staticbox.SetSizer(self.hot_water_box)
			self.cold_water_staticbox = wx.StaticBox(self.panel,wx.ID_ANY,'Счётчик холодной воды')
			self.cold_water_box = wx.BoxSizer(wx.VERTICAL)
			self.cold_water_numbers = wx.BoxSizer(wx.HORIZONTAL)
			self.cold_water_number_1 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_1.SetFont(self.font)
			self.cold_water_number_1.Enable(False)
			self.cold_water_staticline1 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_2 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_2.SetFont(self.font)
			self.cold_water_number_2.Enable(False)
			self.cold_water_staticline2 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_3 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_3.SetFont(self.font)
			self.cold_water_number_3.Enable(False)
			self.cold_water_staticline3 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_4 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_4.SetFont(self.font)
			self.cold_water_number_4.Enable(False)
			self.cold_water_staticline4 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_5 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_5.SetFont(self.font)
			self.cold_water_number_5.Enable(False)
			self.cold_water_staticline5 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_6 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_6.SetFont(self.font)
			self.cold_water_number_6.Enable(False)
			self.cold_water_staticline6 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_7 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_7.SetFont(self.font)
			self.cold_water_number_7.Enable(False)
			self.cold_water_staticline7 = wx.StaticLine(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultPosition,wx.Size(1,75))
			self.cold_water_number_8 = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'0',wx.DefaultPosition,wx.Size(50,75))
			self.cold_water_number_8.SetFont(self.font)
			self.cold_water_number_8.Enable(False)
			self.cold_water_numbers.Add(self.cold_water_number_1)
			self.cold_water_numbers.Add(self.cold_water_staticline1)
			self.cold_water_numbers.Add(self.cold_water_number_2)
			self.cold_water_numbers.Add(self.cold_water_staticline2)
			self.cold_water_numbers.Add(self.cold_water_number_3)
			self.cold_water_numbers.Add(self.cold_water_staticline3)
			self.cold_water_numbers.Add(self.cold_water_number_4)
			self.cold_water_numbers.Add(self.cold_water_staticline4)
			self.cold_water_numbers.Add(self.cold_water_number_5)
			self.cold_water_numbers.Add(self.cold_water_staticline5)
			self.cold_water_numbers.Add(self.cold_water_number_6)
			self.cold_water_numbers.Add(self.cold_water_staticline6)
			self.cold_water_numbers.Add(self.cold_water_number_7)
			self.cold_water_numbers.Add(self.cold_water_staticline7)
			self.cold_water_numbers.Add(self.cold_water_number_8)
			self.cold_water_box.Add(self.cold_water_numbers,0,wx.CENTER+wx.ALL,30)
			self.cold_water_flexgridsizer = wx.FlexGridSizer(4,2,80,20)
			self.cold_water_serial_number_statictext = wx.StaticText(self.cold_water_staticbox,wx.ID_ANY,'Серийный номер')
			self.cold_water_serial_number_textctrl = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(270,21))
			self.cold_water_document_number_statictext = wx.StaticText(self.cold_water_staticbox,wx.ID_ANY,'№ документа')
			self.cold_water_document_number_textctrl = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(270,21))
			self.cold_water_place_date_statictext = wx.StaticText(self.cold_water_staticbox,wx.ID_ANY,'Дата установки')
			self.cold_water_place_date_datepickerctrl = wx.adv.DatePickerCtrl(self.cold_water_staticbox,wx.ID_ANY,wx.DefaultDateTime,wx.DefaultPosition,wx.Size(270,21))
			self.cold_water_tariff_statictext = wx.StaticText(self.cold_water_staticbox,wx.ID_ANY,'Тариф (руб. за кв.м.)')
			self.cold_water_tariff_textctrl = wx.TextCtrl(self.cold_water_staticbox,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(270,21))
			self.cold_water_serial_number_textctrl.Enable(False)
			self.cold_water_document_number_textctrl.Enable(False)
			self.cold_water_place_date_datepickerctrl.Enable(False)
			self.cold_water_tariff_textctrl.Enable(False)
			if self.about_cold_water != None:
				self.cold_water_serial_number_textctrl.SetValue(str(self.about_cold_water[0]))
				self.cold_water_document_number_textctrl.SetValue(str(self.about_cold_water[1]))
				self.cold_water_place_date_datepickerctrl.SetValue(self.about_cold_water[2])
				self.cold_water_tariff_textctrl.SetValue(str(self.about_cold_water[3]))
				if len(str(self.about_cold_water[4])) == 1:
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[0])
				elif len(str(self.about_cold_water[4])) == 2:
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[1])
				elif len(str(self.about_cold_water[4])) == 3:
					self.cold_water_number_6.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[1])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[2])
				elif len(str(self.about_cold_water[4])) == 4:
					self.cold_water_number_5.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_6.SetValue(str(self.about_cold_water[4])[1])
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[2])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[3])
				elif len(str(self.about_cold_water[4])) == 5:
					self.cold_water_number_4.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_5.SetValue(str(self.about_cold_water[4])[1])
					self.cold_water_number_6.SetValue(str(self.about_cold_water[4])[2])
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[3])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[4])
				elif len(str(self.about_cold_water[4])) == 6:
					self.cold_water_number_3.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_4.SetValue(str(self.about_cold_water[4])[1])
					self.cold_water_number_5.SetValue(str(self.about_cold_water[4])[2])
					self.cold_water_number_6.SetValue(str(self.about_cold_water[4])[3])
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[4])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[5])
				elif len(str(self.about_cold_water[4])) == 7:
					self.cold_water_number_2.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_3.SetValue(str(self.about_cold_water[4])[1])
					self.cold_water_number_4.SetValue(str(self.about_cold_water[4])[2])
					self.cold_water_number_5.SetValue(str(self.about_cold_water[4])[3])
					self.cold_water_number_6.SetValue(str(self.about_cold_water[4])[4])
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[5])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[6])
				elif len(str(self.about_cold_water[4])) == 8:
					self.cold_water_number_1.SetValue(str(self.about_cold_water[4])[0])
					self.cold_water_number_2.SetValue(str(self.about_cold_water[4])[1])
					self.cold_water_number_3.SetValue(str(self.about_cold_water[4])[2])
					self.cold_water_number_4.SetValue(str(self.about_cold_water[4])[3])
					self.cold_water_number_5.SetValue(str(self.about_cold_water[4])[4])
					self.cold_water_number_6.SetValue(str(self.about_cold_water[4])[5])
					self.cold_water_number_7.SetValue(str(self.about_cold_water[4])[6])
					self.cold_water_number_8.SetValue(str(self.about_cold_water[4])[7])
				user_id = self.user_id[0]
				serial_number = self.about_cold_water[0]
				type_meter = 'ХВС'
				document_number = self.about_cold_water[1]
				place_date = self.about_cold_water[2]
				tariff = self.about_cold_water[3]
				reading = self.about_cold_water[4]+random.randint(1,10)
				data_for_delete = (user_id,'ХВС')
				data_for_add = (str(reading),str(user_id),'ХВС')
				repository.update_meter(cursor,connection,data_for_add)
			self.cold_water_flexgridsizer.Add(self.cold_water_serial_number_statictext)
			self.cold_water_flexgridsizer.Add(self.cold_water_serial_number_textctrl)
			self.cold_water_flexgridsizer.Add(self.cold_water_document_number_statictext)
			self.cold_water_flexgridsizer.Add(self.cold_water_document_number_textctrl)
			self.cold_water_flexgridsizer.Add(self.cold_water_place_date_statictext)
			self.cold_water_flexgridsizer.Add(self.cold_water_place_date_datepickerctrl)
			self.cold_water_flexgridsizer.Add(self.cold_water_tariff_statictext)
			self.cold_water_flexgridsizer.Add(self.cold_water_tariff_textctrl)
			self.cold_water_box.Add(self.cold_water_flexgridsizer,0,wx.CENTER+wx.ALL,30)
			self.cold_water_staticbox.SetSizer(self.cold_water_box)
			self.waters_box.Add(self.hot_water_staticbox,0,wx.LEFT)
			self.waters_box.AddSpacer(50)
			self.waters_box.Add(self.cold_water_staticbox,0,wx.RIGHT)
			self.meters_boxsizer.Add(self.add_meter_button,0,wx.ALIGN_RIGHT+wx.ALL,10)
			self.meters_boxsizer.Add(self.waters_box,0,wx.ALIGN_CENTER+wx.ALL,50)
			self.boxsizer.Add(self.settings_boxsizer)
			self.boxsizer.Add(self.boxes_staticline,0,wx.ALL,10)
			self.boxsizer.Add(self.meters_boxsizer,1,wx.EXPAND)
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.Center()
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.personal_button.Bind(wx.EVT_BUTTON,self.ShowPersonal, id = wx.ID_ANY)
			self.receipts_button.Bind(wx.EVT_BUTTON,self.ShowReceipts, id = wx.ID_ANY)
			self.add_meter_button.Bind(wx.EVT_BUTTON,self.AddMeter, id = wx.ID_ANY)

		#Функция при закрытии окна
		def OnClose(self,event):
			yes = wx.MessageBox('Желаете закончить работу приложения?',' ',wx.YES_NO+wx.ICON_INFORMATION)
			if yes == wx.YES:
				self.Destroy()

		def ShowPersonal(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class new_data:
				def __init__(self,login):
					self.login = login
			need_data = new_data(data.login)
			self.Destroy()
			WindowsManager.On_Next('show_meters_window','show_personal_window',need_data)

		def ShowReceipts(self,event):
			if self.hot_water_serial_number_textctrl.GetValue() != '' and self.cold_water_serial_number_textctrl.GetValue() != '':
				WindowsManager = WinManager(cursor,connection,repository)
				class new_data:
					def __init__(self,login):
						self.login = login
				need_data = new_data(data.login)
				self.Destroy()
				WindowsManager.On_Next('show_meters_window','show_receipts_window',need_data)
			else:
				wx.MessageBox('Не добавлены счётчики','Ошибка',wx.OK+wx.ICON_ERROR)

		#Функция при нажатии на кнопку "Добавить счётчик"
		def AddMeter(self,event):
			WindowsManager = WinManager(cursor,connection,repository)
			class new_data:
				def __init__(self,user_id, parent, hot_water_serial_number_textctrl, hot_water_document_number_textctrl, hot_water_place_date_datepickerctrl, hot_water_tariff_textctrl, cold_water_serial_number_textctrl, cold_water_document_number_textctrl, cold_water_place_date_datepickerctrl, cold_water_tariff_textctrl, hot_water_numbers1, hot_water_numbers2, hot_water_numbers3, hot_water_numbers4, hot_water_numbers5, hot_water_numbers6, hot_water_numbers7, hot_water_numbers8, cold_water_numbers1, cold_water_numbers2, cold_water_numbers3, cold_water_numbers4, cold_water_numbers5, cold_water_numbers6, cold_water_numbers7, cold_water_numbers8):
					self.user_id = user_id
					self.parent = parent
					self.hot_water_serial_number_textctrl = hot_water_serial_number_textctrl
					self.hot_water_document_number_textctrl = hot_water_document_number_textctrl
					self.hot_water_place_date_datepickerctrl = hot_water_place_date_datepickerctrl
					self.hot_water_tariff_textctrl = hot_water_tariff_textctrl
					self.cold_water_serial_number_textctrl = cold_water_serial_number_textctrl
					self.cold_water_document_number_textctrl = cold_water_document_number_textctrl
					self.cold_water_place_date_datepickerctrl = cold_water_place_date_datepickerctrl
					self.cold_water_tariff_textctrl = cold_water_tariff_textctrl
					self.hot_water_numbers_1 = hot_water_numbers1
					self.hot_water_numbers_2 = hot_water_numbers2
					self.hot_water_numbers_3 = hot_water_numbers3
					self.hot_water_numbers_4 = hot_water_numbers4
					self.hot_water_numbers_5 = hot_water_numbers5
					self.hot_water_numbers_6 = hot_water_numbers6
					self.hot_water_numbers_7 = hot_water_numbers7
					self.hot_water_numbers_8 = hot_water_numbers8
					self.cold_water_numbers_1 = cold_water_numbers1
					self.cold_water_numbers_2 = cold_water_numbers2
					self.cold_water_numbers_3 = cold_water_numbers3
					self.cold_water_numbers_4 = cold_water_numbers4
					self.cold_water_numbers_5 = cold_water_numbers5
					self.cold_water_numbers_6 = cold_water_numbers6
					self.cold_water_numbers_7 = cold_water_numbers7
					self.cold_water_numbers_8 = cold_water_numbers8
			need_data = new_data(self.user_id[0],self,self.hot_water_serial_number_textctrl,self.hot_water_document_number_textctrl,self.hot_water_place_date_datepickerctrl,self.hot_water_tariff_textctrl,self.cold_water_serial_number_textctrl,self.cold_water_document_number_textctrl,self.cold_water_place_date_datepickerctrl,self.cold_water_tariff_textctrl, self.hot_water_number_1, self.hot_water_number_2, self.hot_water_number_3, self.hot_water_number_4, self.hot_water_number_5, self.hot_water_number_6, self.hot_water_number_7, self.hot_water_number_8, self.cold_water_number_1, self.cold_water_number_2, self.cold_water_number_3, self.cold_water_number_4, self.cold_water_number_5, self.cold_water_number_6, self.cold_water_number_7, self.cold_water_number_8)
			WindowsManager.On_Next('show_meters_window','add_meter_window',need_data)


	frm = Frame(None, title=" ") #Создание элемента класса без предшествующих окон и с названием "Вход в систему"
	frm.SetMinSize(wx.Size(1280,720))
	frm.SetMaxSize(wx.Size(1280,720))
	frm.Show(True) #Окно становится модальным