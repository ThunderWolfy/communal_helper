import wx

def show_receipt_photo_window(cursor, connection, repository, WinManager, data):
	#Класс диалогового окна
	class Frame(wx.Frame):
		#Функция при создании диалогого окна
		def __init__(self,*args,**kv):
			super(Frame,self).__init__(*args,**kv) #Прописывается интерфейс окна с наименованием и предшествующим окном
			img = wx.Image(data.photo, wx.BITMAP_TYPE_ANY)
			self.SetMaxSize(wx.Size(img.GetWidth(),img.GetHeight()))
			self.SetMinSize(wx.Size(img.GetWidth(),img.GetHeight()))
			self.panel = wx.Panel(self) #Панель, на которой всё будет располагаться
			self.boxsizer = wx.BoxSizer(wx.HORIZONTAL) #Контейнер для всех виджетов на панели
			self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img))
			self.boxsizer.Add(self.imageCtrl,1,wx.EXPAND)
			self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
			self.panel.SetSizer(self.boxsizer) #Установка контейнера со всеми виджетами на панели главным для панели

	frm = Frame(data.parent, title="Просмотр квитанции") #Создание элемента класса без предшествующих окон и с названием "Вход в систему"
	frm.Show(True) #Окно становится модальным