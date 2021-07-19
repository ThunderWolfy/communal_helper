import wx
import wx.adv
import datetime
def add_meter_window(cursor, connection, repository, WindowsManager, data):
	class Frame(wx.Frame):
		def __init__(self,*args,**kv):
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.VERTICAL) #Контейнер для всех виджетов на панели
			self.flexgridsizer = wx.FlexGridSizer(5,2,10,10)
			self.serial_number_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Серийный номер')
			self.serial_number_spinctrl = wx.SpinCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.serial_number_spinctrl.SetRange(1,99999999)
			self.type_meter_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Тип счётчика')
			self.type_meter_combobox = wx.ComboBox(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.type_meter_combobox.Append('ГВС')
			self.type_meter_combobox.Append('ХВС')
			self.document_number_statictext = wx.StaticText(self.panel,wx.ID_ANY,'№ договора')
			self.document_number_spinctrl = wx.SpinCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.document_number_spinctrl.SetRange(1,99999999)
			self.tariff_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Тариф (за куб. м.)')
			self.tariff_spinctrl = wx.SpinCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.place_data_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Дата установки',wx.DefaultPosition,wx.Size(120,21))
			self.place_data_datepickerctrl = wx.adv.DatePickerCtrl(self.panel,wx.ID_ANY,wx.DefaultDateTime,wx.DefaultPosition,wx.Size(120,21),wx.adv.DP_DROPDOWN)
			self.flexgridsizer.Add(self.serial_number_statictext)
			self.flexgridsizer.Add(self.serial_number_spinctrl)
			self.flexgridsizer.Add(self.type_meter_statictext)
			self.flexgridsizer.Add(self.type_meter_combobox)
			self.flexgridsizer.Add(self.document_number_statictext)
			self.flexgridsizer.Add(self.document_number_spinctrl)
			self.flexgridsizer.Add(self.tariff_statictext)
			self.flexgridsizer.Add(self.tariff_spinctrl)
			self.flexgridsizer.Add(self.place_data_statictext)
			self.flexgridsizer.Add(self.place_data_datepickerctrl)
			self.save_button = wx.Button(self.panel,wx.ID_ANY,'Добавить',wx.DefaultPosition,wx.Size(120,21))
			self.boxsizer.AddStretchSpacer(1)
			self.boxsizer.Add(self.flexgridsizer,0,wx.CENTER+wx.ALL,10)
			self.boxsizer.AddStretchSpacer(1)
			self.boxsizer.Add(self.save_button,0,wx.ALIGN_RIGHT+wx.ALL,10)
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.save_button.Bind(wx.EVT_BUTTON, self.SaveMeter, id = wx.ID_ANY)
		
		#Функция при закрытии окна
		def OnClose(self,event):
			yes = wx.MessageBox('Отменить изменения?',' ',wx.YES_NO+wx.ICON_INFORMATION)
			if yes == wx.YES:
				self.Destroy()

		#Функция при нажатии кнопки "Добавить"
		def SaveMeter(self,event):
			user_id = data.user_id
			serial_number = self.serial_number_spinctrl.GetValue()
			type_meter = self.type_meter_combobox.GetValue()
			document_number = self.document_number_spinctrl.GetValue()
			datetime = self.place_data_datepickerctrl.GetValue()
			day = datetime.GetDay()
			if day < 10:
				day = '0'+str(day)
			month = datetime.GetMonth()+1
			if month < 10:
				month = '0'+str(month)
			year = datetime.GetYear()
			place_date = str(year)+'-'+str(month)+'-'+str(day)
			tariff = self.tariff_spinctrl.GetValue()
			if data.hot_water_serial_number_textctrl.GetValue() != '' and data.cold_water_serial_number_textctrl.GetValue() != '':
				data_to_update = (data.user_id, type_meter)
				repository.delete_meter(cursor, connection, data_to_update)
			data_to_add = (data.user_id,serial_number,type_meter,document_number,place_date,tariff,'0')
			repository.add_meter(cursor, connection, data_to_add)
			data_to_search = (data.user_id,type_meter)
			meter_id = repository.search_meter_id_by_user_id_type(cursor,connection,data_to_search)
			data_to_add_receipt = (meter_id[0],'0')
			meter_id = repository.add_receipt(cursor,connection,data_to_add_receipt)
			wx.MessageBox('Счётчик успешно добавлен!', ' ', wx.OK+wx.ICON_INFORMATION)
			if type_meter == 'ГВС':
				data.hot_water_serial_number_textctrl.SetValue(str(serial_number))
				data.hot_water_document_number_textctrl.SetValue(str(document_number))
				data.hot_water_place_date_datepickerctrl.SetValue(datetime)
				data.hot_water_tariff_textctrl.SetValue(str(tariff))
				data.hot_water_numbers_1.SetValue('0')
				data.hot_water_numbers_2.SetValue('0')
				data.hot_water_numbers_3.SetValue('0')
				data.hot_water_numbers_4.SetValue('0')
				data.hot_water_numbers_5.SetValue('0')
				data.hot_water_numbers_6.SetValue('0')
				data.hot_water_numbers_7.SetValue('0')
				data.hot_water_numbers_8.SetValue('0')
			elif type_meter == 'ХВС':
				data.cold_water_serial_number_textctrl.SetValue(str(serial_number))
				data.cold_water_document_number_textctrl.SetValue(str(document_number))
				data.cold_water_place_date_datepickerctrl.SetValue(datetime)
				data.cold_water_tariff_textctrl.SetValue(str(tariff))
				data.cold_water_numbers_1.SetValue('0')
				data.cold_water_numbers_2.SetValue('0')
				data.cold_water_numbers_3.SetValue('0')
				data.cold_water_numbers_4.SetValue('0')
				data.cold_water_numbers_5.SetValue('0')
				data.cold_water_numbers_6.SetValue('0')
				data.cold_water_numbers_7.SetValue('0')
				data.cold_water_numbers_8.SetValue('0')
			data.parent.Refresh()
			self.Destroy()

	dialog = Frame(data.parent,title = 'Добавление счётчика')
	dialog.SetMinSize(wx.Size(375,325))
	dialog.SetMaxSize(wx.Size(375,325))
	dialog.Show(True)