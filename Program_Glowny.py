#rozbudowany moduł obsługi Aplikacju
import GUI_DESIGNER
import Lista_portow
from functools import partial
from PyQt5 import QtCore, QtWidgets
import serial


class Dodane_funkcje(GUI_DESIGNER.Ui_MainWindow):
	def __init__(self):
		self.porty = []
		self.akcja = []
		self.SERIAL_MENU = 0
		self.baud = 0
		self.podmenu_diod_5V = 0
		self.podmenu_diod_12V = 0
		self.pomiar = 0

		self.PWM1 = 0
		self.PWM2 = 0

		self.port = 0
		self.SERIAL = 0

	def setupUi(self, master):
		super(Dodane_funkcje, self).setupUi(master)

		# DODANIE GORNEGO MENU
		self.SERIAL_MENU = self.menubar.addMenu("&SERIAL")
		# DODAWANIE FUNKCJI PODMENU
		self.porty = Lista_portow.funkcja_zwrotu_portow()
		self.akcja = []
		for obiekt in self.porty:
			self.akcja.append(self.SERIAL_MENU.addAction(obiekt))

		# PREDKOSC TRANSMISJI
		self.baud = 250000
		i = 0
		# Metoda utworzenia zdarzeń dla SerialPortów
		for item in self.akcja:
			item.triggered.connect(partial(self.serial, i))
			i += 1
		self.ustawienia_poczatkowe()

	# Ustawienie przyciskow glownych
	def ustawienia_poczatkowe(self):
		#  USTAWIENIE PODMENU OBSLUGI DIOD
		self.podmenu_diod_5V = Dioda_obsluga(1, self, self.Kontrola_PIN5V_check, self.Button_ON_P1, self.Button_ON_P2, self.Button_OFF_P1, self.Button_OFF_P2, 1, 2)
		self.Kontrola_PIN5V_check.clicked.connect(self.podmenu_diod_5V.ustawienie_check)

		self.podmenu_diod_12V = Dioda_obsluga(2, self, self.Kontrola_PIN12V_check, self.Button_ON_P3, self.Button_ON_P4, self.Button_OFF_P3, self.Button_OFF_P4, 3, 4)
		self.Kontrola_PIN12V_check.clicked.connect(self.podmenu_diod_12V.ustawienie_check)

		# USTAWIENIE PODMENU POMIARU NAPIECIA
		self.pomiar=Pomiar(self)
		self.Pomiar_adc_check.clicked.connect(self.pomiar.pomiar)
		# USTAWIENIE PODMENU PWM
		self.PWM1 = Generowanie_PWM_1(self, "05", self.Generowanie_PWM1_check, self.Slider_wypelnienie_PWM1, self.lcd_zadany_PWM1, self.lcd_aktualny_na_pinie_PWM1, self.Button_Aktualizacja_PWM1)
		self.Generowanie_PWM1_check.clicked.connect(self.PWM1.generowanie_PWM)

		self.PWM2 = Generowanie_PWM_1(self, "06", self.Generowanie_PWM2_check, self.Slider_wypelnienie_PWM2, self.lcd_zadany_PWM2, self.lcd_aktualny_na_pinie_PWM2, self.Button_Aktualizacja_PWM2)
		self.Generowanie_PWM2_check.clicked.connect(self.PWM2.generowanie_PWM)
	# Metoda tworząca polaczenie z portem

	def serial(self, wartosc):
		print("NOWE POLACZENIE Z PORTEM : " + self.porty[wartosc] + ". ")
		self.port = self.porty[wartosc]
		self.SERIAL = serial.Serial(port = self.port,baudrate=self.baud)
		# wyzerowanie pinow
		self.SERIAL.write(b'#01*00-00/000+')
		self.SERIAL.write(b'#01*00-01/000+')

		#      USTAWIENIA POCZATKOWE PRZY NOWYM POLACZENIU

		# WYLACZENIE PRZYCISKU ZATWIERDZAJACEGO ZMIANE PINOW 5V
		if self.Kontrola_PIN5V_check.checkState() == 2:
			self.Kontrola_PIN5V_check.setChecked(False)
			self.podmenu_diod_5V.ustawienie_check()
		# WYLACZENIE PRZYCISKU ZATWIERDZAJACEGO ZMIANE PINOW 12V
		if self.Kontrola_PIN12V_check.checkState() == 2:
			self.Kontrola_PIN12V_check.setChecked(False)
			self.podmenu_diod_12V.ustawienie_check()

		# WYLACZENIE PRZYCISKU ZATWIERDZAJACEGO POMIAR
		if self.Pomiar_adc_check.checkState() == 2:
			self.Pomiar_adc_check.setChecked(False)
			self.pomiar.pomiar()

		# WYLACZENIE PRZYCISKU ZATWIERDZAJACEGO PWM1
		if self.Generowanie_PWM1_check.checkState() ==2:
			self.Generowanie_PWM1_check.setChecked(False)
			self.PWM1.generowanie_PWM()

		# WYLACZENIE PRZYCISKU ZATWIERDZAJACEGO PWM2
		if self.Generowanie_PWM2_check.checkState() == 2:
			self.Generowanie_PWM2_check.setChecked(False)
			self.PWM2.generowanie_PWM()


	def serial_close(self):
		self.SERIAL.close()

class Dioda_obsluga(object):
	def __init__(self, nr_podmenu, master, check, d1_on, d2_on, d1_off, d2_off, nr_pin1, nr_pin2):
		# przypisanie wartosci
		self.master=master
		self.checkbutton = check
		self.nr_menu = nr_podmenu
		self.d1_on = d1_on
		self.d1_off = d1_off
		self.d2_on = d2_on
		self.d2_off = d2_off
		self.nr_pin1 = nr_pin1
		self.nr_pin2 = nr_pin2

		self.stan_checkButton = 0
		self.checked_off()

	def ustawienie_check(self):
		if self.checkbutton.checkState() == 2:
			self.checked_on()
			self.stan_checkButton = 0
			self.ustawienie_funkcji()
		else:
			self.checked_off()
			self.stan_checkButton = 1
			self.reset_funkcji()
			MainWindow.update()

	# GDY CHECKBUTTON WCISNIETY MOZNA DOKONAC WYBORU
	def checked_on(self):
		print("pressed")
		self.d1_on.setCheckable(True)
		self.d2_on.setCheckable(True)

		self.d1_off.setCheckable(True)
		self.d2_off.setCheckable(True)

		self.d1_off.setChecked(True)
		self.d2_off.setChecked(True)

	def checked_off(self):

		self.d1_off.setCheckable(False)
		self.d2_off.setCheckable(False)

		self.d1_on.setCheckable(False)
		self.d2_on.setCheckable(False)

	def ustawienie_funkcji(self):
		#sprawdza czy jest połaczony Port
		try:
			self.master.SERIAL.isOpen()

		except:
			print("sprawdz czy wybrany odpowiedni port")
			return 0

		self.d1_on.clicked.connect(partial(self.led_button_pressed,bytes("#01*0"+ str(self.nr_pin1) +"-01/000+",'utf-8')))
		self.d2_on.clicked.connect(partial(self.led_button_pressed,bytes("#01*0"+ str(self.nr_pin2) +"-01/000+",'utf-8')))

		self.d1_off.clicked.connect(partial(self.led_button_pressed,bytes("#01*0"+ str(self.nr_pin1) +"-00/000+",'utf-8')))
		self.d2_off.clicked.connect(partial(self.led_button_pressed,bytes("#01*0"+ str(self.nr_pin2) +"-00/000+",'utf-8')))

	# reset funkcji gdy checkbutton nie jest wciśnięty
	def reset_funkcji(self):
		try:	self.master.SERIAL.isOpen()
		except:
			print("sprawdz czy wybrany odpowiedni port")
			return 0
		if self.nr_menu == 1:
			self.master.SERIAL.write(b'#01*00-00/000+')
		elif self.nr_menu == 2:
			self.master.SERIAL.write(b'#01*00-01/000+')

		try : self.d1_on.clicked.disconnect()
		except: """"""
		try : self.d2_on.clicked.disconnect()
		except: """"""
		try : self.d1_off.clicked.disconnect()
		except: """"""
		try : self.d2_off.clicked.disconnect()
		except: """"""

	# METODY OBSLUGUJĄCE KLAWISZE
	def led_button_pressed(self,komenda):
		#wyslanie danych
		self.master.SERIAL.write(komenda)
		print("Wyslano komende : "+ komenda.decode('utf-8'))

class Pomiar(object):
	def __init__(self,master):
		self.stan_pomiar = 0
		self.master = master

		# TIMER DLA WYSLANIA ZAPYTANIA O POMIAR
		self.timer = QtCore.QTimer()
		self.watek_zapytania = Watek_zapytania_o_pomiar(self.master)
		self.watek_cykliczny_odbior_danych = Watek_odebrania_danych(self.master)
		self.timer.timeout.connect(self.watek_zapytania.start)
		self.czas=1000

		## DODANE DO CYKLICZNEGO SPRAWDZANIA DANYCH W BUFORZE
		self.timer_odbioru_danych = QtCore.QTimer()
		self.timer_odbioru_danych.timeout.connect(self.watek_cykliczny_odbior_danych.start)

	#metoda pomiaru
	def pomiar(self):
		if self.master.comboBox_czestotliwosc_pomiar.currentIndex() == 0:
			self.czas=1000
		elif self.master.comboBox_czestotliwosc_pomiar.currentIndex() == 1:
			self.czas=200
		elif self.master.comboBox_czestotliwosc_pomiar.currentIndex() == 2:
			self.czas=100
		elif self.master.comboBox_czestotliwosc_pomiar.currentIndex() == 3:
			self.czas=50
		elif self.master.comboBox_czestotliwosc_pomiar.currentIndex() == 4:
			self.czas=20
		elif self.master.comboBox_czestotliwosc_pomiar.currentIndex() == 5:
			self.czas=10


		if self.stan_pomiar == 0:
			self.timer.start(self.czas)
			self.stan_pomiar = 1
			self.master.comboBox_czestotliwosc_pomiar.setEnabled(False)
			self.timer_odbioru_danych.start(1)
		elif self.stan_pomiar == 1:
			self.timer.stop()
			self.timer_odbioru_danych.stop()
			self.stan_pomiar=0
			self.master.comboBox_czestotliwosc_pomiar.setEnabled(True)
		#print(dir(self.master.comboBox_czestotliwosc_pomiar))

	def przycisk_pomiar(self,czas):
		self.timer.setInterval(czas)

	def cykliczny_odbior_danych(self):
		if self.master.SERIAL.in_waiting:
			zdanie = self.master.SERIAL.readline().decode('utf-8')
			if zdanie[0]=="P":
				print(zdanie)
				self.master.lcd_pomiar.display(zdanie)

class Generowanie_PWM(object):
	def __init__(self,master,pin,checkbutton,slider=0,lcd=0):
		self.master = master
		self.checkbutton = checkbutton
		self.slider = slider
		self.lcd = lcd
		self.pin = pin
		self.wypelnienie ="000"
		self.czestotliwosc_PWM_NR = 0
		self.slider.setDisabled(1)
	def generowanie_PWM(self):
		try:	self.master.SERIAL.isOpen()
		except:
			print("sprawdz czy wybrany odpowiedni port")
			return 0
		print("generacja PWM")
		#ustawienie widgetow
		if self.checkbutton.checkState() == 2:

			##self.master.Button_AktualizacjaPWM.clicked.connect(self.pwm_ustawienie)
			self.slider.sliderMoved.connect(self.wyslanie_na_lcd_aktualnego_slidera)
			self.slider.valueChanged.connect(self.wyslanie_na_lcd_aktualnego_slidera)
			self.slider.sliderMoved.connect(self.pwm_ustawienie)
			self.slider.setDisabled(0)
		else:
			#WYZEROWANIE SLIDERA
			self.slider.setSliderPosition(0)
			self.slider.setDisabled(1)
			try: self.slider.sliderMoved.disconnect()
			except:
				""""""
			self.slider.valueChanged.disconnect()


	def pwm_ustawienie(self):
		zdanie = 0

		self.wypelnienie = self.slider.sliderPosition()
		self.czestotliwosc_PWM_NR = self.master.comboBox_czestotliwosc_PWM1.currentIndex()

		#DOPISYWANIE W ZALEZNOSCI OD ILOSCI CYFR
		if self.wypelnienie<10:
			zdanie = ("#03*" + self.pin + "-0" + str(self.czestotliwosc_PWM_NR) + "/00" + str(self.wypelnienie) + "+")
		elif self.wypelnienie<100:
			zdanie = ("#03*" + self.pin + "-0" + str(self.czestotliwosc_PWM_NR) + "/0" + str(self.wypelnienie) + "+")
		elif self.wypelnienie==100:
			zdanie = ("#03*" + self.pin + "-0" + str(self.czestotliwosc_PWM_NR) + "/" + str(self.wypelnienie) + "+")
		print(zdanie)
		self.master.SERIAL.write(bytes(zdanie,'utf-8'))
		self.lcd.display(self.wypelnienie)

	def wyslanie_na_lcd_aktualnego_slidera(self):
		wartosc_slider=self.slider.sliderPosition()
		self.lcd.display(wartosc_slider)
		MainWindow.update()

class Generowanie_PWM_1(Generowanie_PWM):
	def __init__(self,master,pin,checkbutton,slider=0,lcd=0,lcd_wyp=0,butt_akt=0):
		super(Generowanie_PWM_1, self).__init__(master,pin,checkbutton,slider,lcd)
		self.lcd_akt=lcd_wyp
		self.button = butt_akt
	def generowanie_PWM(self):
		super(Generowanie_PWM_1, self).generowanie_PWM()

		try: self.slider.sliderMoved.disconnect()
		except:
			""""""
		else:
			self.slider.sliderMoved.connect(self.wyslanie_na_lcd_aktualnego_slidera)

		if self.checkbutton.checkState() == 2:
			self.button.clicked.connect(self.aktualizacja)
		else:
			self.aktualizacja()
			self.button.clicked.disconnect()

	def aktualizacja(self):
		self.pwm_ustawienie()
		self.lcd_akt.display(self.wypelnienie)

class Watek_zapytania_o_pomiar(QtCore.QThread):
	def __init__(self,master = None, parent = None):
		super(Watek_zapytania_o_pomiar, self).__init__(parent)

		self.master = master

	def run(self):
		try: self.master.SERIAL.isOpen()
		# try: self.master.SERIAL.isOpen()
		except:
			print("Pomiar nie dziala, sprawdz port.")
		else:
			self.master.SERIAL.write(b'#02*00-00/000+')

class Watek_odebrania_danych(QtCore.QThread):
	def __init__(self,master = None, parent = None):
		super(Watek_odebrania_danych, self).__init__(parent)

		self.master = master

	def run(self):
		if self.master.SERIAL.in_waiting:
			zdanie = self.master.SERIAL.readline().decode('utf-8')
			if zdanie[0] == "P":
				print(zdanie)
				self.master.lcd_pomiar.display(zdanie)


import sys
porty = Lista_portow.funkcja_zwrotu_portow()
print(porty)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Dodane_funkcje()
ui.setupUi(MainWindow)

MainWindow.setMaximumSize(MainWindow.size())
MainWindow.show()

sys.exit(app.exec_())
