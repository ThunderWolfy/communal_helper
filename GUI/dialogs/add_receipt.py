import wx
import wx.adv
import datetime
from shutil import copyfile
def add_receipt_window(cursor, connection, repository, WindowsManager, data):
	class Frame(wx.Frame):
		def __init__(self,*args,**kv):
			self.hot_water_id = data.hot_water_id
			self.cold_water_id = data.cold_water_id
			self.grid = data.grid
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.VERTICAL) #Контейнер для всех виджетов на панели
			self.flexgridsizer = wx.FlexGridSizer(4,3,60,15)
			self.type_meter_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Тип счётчика')
			self.type_meter_combobox = wx.ComboBox(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.type_meter_combobox.Append('ГВС')
			self.type_meter_combobox.Append('ХВС')
			self.end_reading_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Показания при сдаче')
			self.end_reading_spinctrl = wx.SpinCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.end_reading_spinctrl.SetRange(1,99999999)
			self.receipt_date_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Дата сдачи')
			self.receipt_date_datepickerctrl = wx.adv.DatePickerCtrl(self.panel,wx.ID_ANY,wx.DefaultDateTime,wx.DefaultPosition,wx.Size(120,21),wx.adv.DP_DROPDOWN)
			self.receipt_photo_statictext = wx.StaticText(self.panel,wx.ID_ANY,'Фотография\nквитанции')
			self.receipt_photo_textctrl = wx.TextCtrl(self.panel,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(120,21))
			self.receipt_photo_textctrl.Enable(False)
			self.receipt_photo_button = wx.Button(self.panel,wx.ID_ANY,'Загрузить',wx.DefaultPosition,wx.Size(120,21))
			self.flexgridsizer.Add(self.type_meter_statictext)
			self.flexgridsizer.Add(self.type_meter_combobox)
			self.flexgridsizer.AddSpacer(0)
			self.flexgridsizer.Add(self.end_reading_statictext)
			self.flexgridsizer.Add(self.end_reading_spinctrl)
			self.flexgridsizer.AddSpacer(0)
			self.flexgridsizer.Add(self.receipt_date_statictext)
			self.flexgridsizer.Add(self.receipt_date_datepickerctrl)
			self.flexgridsizer.AddSpacer(0)
			self.flexgridsizer.Add(self.receipt_photo_statictext)
			self.flexgridsizer.Add(self.receipt_photo_textctrl)
			self.flexgridsizer.Add(self.receipt_photo_button)
			self.save_button = wx.Button(self.panel,wx.ID_ANY,'Добавить',wx.DefaultPosition,wx.Size(120,21))
			self.boxsizer.Add(self.flexgridsizer,0,wx.CENTER+wx.ALL,10)
			self.boxsizer.Add(self.save_button,0,wx.ALIGN_RIGHT+wx.ALL,10)
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели
			self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
			self.Bind(wx.EVT_CLOSE, self.OnClose) #Установка действия при закрытии окна
			self.receipt_photo_button.Bind(wx.EVT_BUTTON, self.SearchPhoto, id = wx.ID_ANY)
			self.save_button.Bind(wx.EVT_BUTTON, self.SaveReceipt, id = wx.ID_ANY)

		#Функция при закрытии окна
		def OnClose(self,event):
			yes = wx.MessageBox('Отменить изменения?',' ',wx.YES_NO+wx.ICON_INFORMATION)
			if yes == wx.YES:
				self.Destroy()

		def SearchPhoto(self,event):
			types = "Фотография (*.jpg;*.png)|*.jpg;*.png"
			file = wx.FileDialog(self, "Выберите фотографию", "", "", types, wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
			file.ShowModal()
			self.receipt_photo_textctrl.SetValue(file.GetPath())

		def SaveReceipt(self,event):
			type_meter = self.type_meter_combobox.GetValue()
			end_reading = self.end_reading_spinctrl.GetValue()
			datetime = self.receipt_date_datepickerctrl.GetValue()
			day = datetime.GetDay()
			if day < 10:
				day = '0'+str(day)
			month = datetime.GetMonth()+1
			if month < 10:
				month = '0'+str(month)
			year = datetime.GetYear()
			place_date = str(year)+'-'+str(month)+'-'+str(day)
			receipt_photo = self.receipt_photo_textctrl.GetValue()
			if type_meter != '' and end_reading != '' and receipt_photo != '':
				meter = ''
				if type_meter == 'ГВС':
					meter = str(self.hot_water_id)
				elif type_meter == 'ХВС':
					meter = str(self.cold_water_id)
				data_for_meter = (meter,)
				receipts_id_with_meter = repository.show_id_receipts_by_meter(cursor,connection,data_for_meter)
				folder = repository.select_save_folder(cursor,connection)
				need_id = "".join(c for c in str(receipts_id_with_meter[-1]) if c.isalnum())
				need_folder = folder[0]+'/photos'+'/'+str(need_id)+'.jpg'
				copyfile(receipt_photo, need_folder)
				data = (end_reading,meter,need_id)
				repository.update_reading(cursor,connection,data)
				data = (place_date,meter,need_id)
				repository.update_date(cursor,connection,data)
				data = (need_folder,meter,need_id)
				repository.update_receipt(cursor,connection,data)
				data = (str(meter),str(end_reading))
				repository.add_receipt(cursor,connection,data)
				wx.MessageBox('Квитанция успешно добавлена',' ',wx.OK+wx.ICON_INFORMATION)
				if self.grid.GetNumberRows()>0:
					self.grid.DeleteRows(0,self.grid.GetNumberRows())
				data_for_receipts = (self.hot_water_id,self.cold_water_id)
				self.receipts = repository.show_receipts_by_meter_id(cursor,connection,data_for_receipts)
				self.need_receipts = []
				for i in range(len(self.receipts)):
					if self.receipts[i][2] != None and self.receipts[i][2] != '' and self.receipts[i][3] != None and self.receipts[i][3] != '':
						self.need_receipts.append(self.receipts[i])
				self.need_receipts.sort(key = lambda tup: tup[1])
				lenght = int(len(self.need_receipts))
				for i in range(lenght):
					self.grid.AppendRows()
					if self.need_receipts[i][0] == self.hot_water_id:
						self.grid.SetCellValue(i,0,'ГВС')
					elif self.need_receipts[i][0] == self.cold_water_id:
						self.grid.SetCellValue(i,0,'ХВС')
					self.grid.SetCellValue(i,1,str(self.need_receipts[i][1]))
					self.grid.SetCellValue(i,2,str(self.need_receipts[i][2]))
					self.grid.SetCellValue(i,3,str(self.need_receipts[i][3]))
				self.Destroy()
			else:
				wx.MessageBox('Не заполнено одно из полей','',wx.OK+wx.ICON_ERROR)

	dialog = Frame(data.parent,title = 'Добавление квитанции')
	dialog.SetMinSize(wx.Size(425,375))
	dialog.SetMaxSize(wx.Size(425,375))
	dialog.Show(True)