# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_DESIGNER.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 847)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Glowna_ramka = QtWidgets.QFrame(self.centralwidget)
        self.Glowna_ramka.setGeometry(QtCore.QRect(10, 10, 741, 781))
        self.Glowna_ramka.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Glowna_ramka.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Glowna_ramka.setObjectName("Glowna_ramka")
        
        self.Widget_Pomiar = QtWidgets.QFrame(self.Glowna_ramka)
        self.Widget_Pomiar.setGeometry(QtCore.QRect(10, 230, 720, 91))
        self.Widget_Pomiar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget_Pomiar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget_Pomiar.setObjectName("Widget_Pomiar")
        
        self.Pomiar_adc_check = QtWidgets.QCheckBox(self.Widget_Pomiar)
        self.Pomiar_adc_check.setGeometry(QtCore.QRect(10, 0, 130, 25))
        self.Pomiar_adc_check.setObjectName("Pomiar_adc_check")
        
        self.lcd_pomiar = QtWidgets.QLCDNumber(self.Widget_Pomiar)
        self.lcd_pomiar.setGeometry(QtCore.QRect(550, 40, 100, 40))
        self.lcd_pomiar.setObjectName("lcd_pomiar")
        
        self.Label_wartosc_pomiar = QtWidgets.QLabel(self.Widget_Pomiar)
        self.Label_wartosc_pomiar.setGeometry(QtCore.QRect(540, 10, 131, 17))
        self.Label_wartosc_pomiar.setObjectName("Label_wartosc_pomiar")
        
        self.comboBox_czestotliwosc_pomiar = QtWidgets.QComboBox(self.Widget_Pomiar)
        self.comboBox_czestotliwosc_pomiar.setGeometry(QtCore.QRect(270, 40, 121, 41))
        self.comboBox_czestotliwosc_pomiar.setObjectName("comboBox_czestotliwosc_pomiar")
        self.comboBox_czestotliwosc_pomiar.addItem("")
        self.comboBox_czestotliwosc_pomiar.addItem("")
        self.comboBox_czestotliwosc_pomiar.addItem("")
        self.comboBox_czestotliwosc_pomiar.addItem("")
        self.comboBox_czestotliwosc_pomiar.addItem("")
        self.comboBox_czestotliwosc_pomiar.addItem("")
        
        self.Label_Czestotliwosc_pomiaru = QtWidgets.QLabel(self.Widget_Pomiar)
        self.Label_Czestotliwosc_pomiaru.setGeometry(QtCore.QRect(280, 20, 101, 17))
        self.Label_Czestotliwosc_pomiaru.setObjectName("Label_Czestotliwosc_pomiaru")
        
        self.comboBox_kanal_pomiar = QtWidgets.QComboBox(self.Widget_Pomiar)
        self.comboBox_kanal_pomiar.setGeometry(QtCore.QRect(20, 50, 86, 25))
        self.comboBox_kanal_pomiar.setObjectName("comboBox_kanal_pomiar")
        self.comboBox_kanal_pomiar.addItem("")
        self.comboBox_kanal_pomiar.addItem("")
        self.comboBox_kanal_pomiar.addItem("")
        self.comboBox_kanal_pomiar.addItem("")
        
        self.Label_Kanal_pomiar = QtWidgets.QLabel(self.Widget_Pomiar)
        self.Label_Kanal_pomiar.setGeometry(QtCore.QRect(40, 30, 41, 17))
        self.Label_Kanal_pomiar.setObjectName("Label_Kanal_pomiar")
        
        self.comboBox_Vref_pomiar = QtWidgets.QComboBox(self.Widget_Pomiar)
        self.comboBox_Vref_pomiar.setGeometry(QtCore.QRect(130, 50, 86, 25))
        self.comboBox_Vref_pomiar.setObjectName("comboBox_Vref_pomiar")
        self.comboBox_Vref_pomiar.addItem("")
        self.comboBox_Vref_pomiar.addItem("")
        
        self.Label_Vref_pomiar = QtWidgets.QLabel(self.Widget_Pomiar)
        self.Label_Vref_pomiar.setGeometry(QtCore.QRect(150, 30, 41, 17))
        self.Label_Vref_pomiar.setObjectName("Label_Vref_pomiar")
        
        self.Widget_PWM1 = QtWidgets.QFrame(self.Glowna_ramka)
        self.Widget_PWM1.setGeometry(QtCore.QRect(10, 330, 721, 161))
        self.Widget_PWM1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget_PWM1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget_PWM1.setObjectName("Widget_PWM1")
        
        self.Generowanie_PWM1_check = QtWidgets.QCheckBox(self.Widget_PWM1)
        self.Generowanie_PWM1_check.setGeometry(QtCore.QRect(10, 0, 211, 25))
        self.Generowanie_PWM1_check.setObjectName("Generowanie_PWM1_check")
        
        self.Slider_wypelnienie_PWM1 = QtWidgets.QSlider(self.Widget_PWM1)
        self.Slider_wypelnienie_PWM1.setGeometry(QtCore.QRect(220, 110, 441, 31))
        self.Slider_wypelnienie_PWM1.setMaximum(100)
        self.Slider_wypelnienie_PWM1.setTracking(False)
        self.Slider_wypelnienie_PWM1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_wypelnienie_PWM1.setInvertedAppearance(False)
        self.Slider_wypelnienie_PWM1.setInvertedControls(False)
        self.Slider_wypelnienie_PWM1.setObjectName("Slider_wypelnienie_PWM1")
        
        self.label_0slider_PWM1 = QtWidgets.QLabel(self.Widget_PWM1)
        self.label_0slider_PWM1.setGeometry(QtCore.QRect(220, 140, 21, 17))
        self.label_0slider_PWM1.setObjectName("label_0slider_PWM1")
        
        self.label_100slider_PWM1 = QtWidgets.QLabel(self.Widget_PWM1)
        self.label_100slider_PWM1.setGeometry(QtCore.QRect(620, 140, 51, 17))
        self.label_100slider_PWM1.setObjectName("label_100slider_PWM1")
        
        self.label_7 = QtWidgets.QLabel(self.Widget_PWM1)
        self.label_7.setGeometry(QtCore.QRect(390, 130, 91, 17))
        self.label_7.setObjectName("label_7")
        
        self.Button_Aktualizacja_PWM1 = QtWidgets.QPushButton(self.Widget_PWM1)
        self.Button_Aktualizacja_PWM1.setGeometry(QtCore.QRect(30, 100, 121, 31))
        self.Button_Aktualizacja_PWM1.setObjectName("Button_Aktualizacja_PWM1")
        
        self.lcd_aktualny_na_pinie_PWM1 = QtWidgets.QLCDNumber(self.Widget_PWM1)
        self.lcd_aktualny_na_pinie_PWM1.setGeometry(QtCore.QRect(260, 50, 100, 40))
        self.lcd_aktualny_na_pinie_PWM1.setObjectName("lcd_aktualny_na_pinie_PWM1")
        
        self.lcd_zadany_PWM1 = QtWidgets.QLCDNumber(self.Widget_PWM1)
        self.lcd_zadany_PWM1.setGeometry(QtCore.QRect(550, 50, 100, 40))
        self.lcd_zadany_PWM1.setObjectName("lcd_zadany_PWM1")
        
        self.label_akt_wyp_PWM1 = QtWidgets.QLabel(self.Widget_PWM1)
        self.label_akt_wyp_PWM1.setGeometry(QtCore.QRect(230, 20, 171, 21))
        self.label_akt_wyp_PWM1.setObjectName("label_akt_wyp_PWM1")
        
        self.label_wybrane_wyp_PWM1 = QtWidgets.QLabel(self.Widget_PWM1)
        self.label_wybrane_wyp_PWM1.setGeometry(QtCore.QRect(520, 20, 171, 21))
        self.label_wybrane_wyp_PWM1.setObjectName("label_wybrane_wyp_PWM1")
        
        self.comboBox_czestotliwosc_PWM1 = QtWidgets.QComboBox(self.Widget_PWM1)
        self.comboBox_czestotliwosc_PWM1.setGeometry(QtCore.QRect(30, 40, 121, 41))
        self.comboBox_czestotliwosc_PWM1.setObjectName("comboBox_czestotliwosc_PWM1")
        self.comboBox_czestotliwosc_PWM1.addItem("")
        self.comboBox_czestotliwosc_PWM1.addItem("")
        self.comboBox_czestotliwosc_PWM1.addItem("")
        self.comboBox_czestotliwosc_PWM1.addItem("")
        self.comboBox_czestotliwosc_PWM1.addItem("")
        self.comboBox_czestotliwosc_PWM1.addItem("")
        
        self.LABEL_TYTULPROGRAMU = QtWidgets.QLabel(self.Glowna_ramka)
        self.LABEL_TYTULPROGRAMU.setGeometry(QtCore.QRect(220, 0, 281, 41))
        
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        
        self.LABEL_TYTULPROGRAMU.setFont(font)
        self.LABEL_TYTULPROGRAMU.setStyleSheet("")
        self.LABEL_TYTULPROGRAMU.setTextFormat(QtCore.Qt.AutoText)
        self.LABEL_TYTULPROGRAMU.setAlignment(QtCore.Qt.AlignCenter)
        self.LABEL_TYTULPROGRAMU.setObjectName("LABEL_TYTULPROGRAMU")
        
        self.Widget_diody5V = QtWidgets.QFrame(self.Glowna_ramka)
        self.Widget_diody5V.setGeometry(QtCore.QRect(10, 50, 720, 81))
        self.Widget_diody5V.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget_diody5V.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget_diody5V.setObjectName("Widget_diody5V")
        
        self.Kontrola_PIN5V_check = QtWidgets.QCheckBox(self.Widget_diody5V)
        self.Kontrola_PIN5V_check.setGeometry(QtCore.QRect(10, 0, 130, 25))
        self.Kontrola_PIN5V_check.setObjectName("Kontrola_PIN5V_check")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Widget_diody5V)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 10, 561, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        
        self.Grupa_dioda1 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.Grupa_dioda1.setObjectName("Grupa_dioda1")
        
        self.Button_ON_P1 = QtWidgets.QRadioButton(self.Grupa_dioda1)
        self.Button_ON_P1.setGeometry(QtCore.QRect(30, 30, 112, 23))
        self.Button_ON_P1.setObjectName("Button_ON_P1")
    
        self.Button_OFF_P1 = QtWidgets.QRadioButton(self.Grupa_dioda1)
        self.Button_OFF_P1.setGeometry(QtCore.QRect(130, 30, 112, 23))
        self.Button_OFF_P1.setObjectName("Button_OFF_P1")
        
        self.horizontalLayout_12.addWidget(self.Grupa_dioda1)
        self.Grupa_dioda2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.Grupa_dioda2.setObjectName("Grupa_dioda2")
        
        self.Button_ON_P2 = QtWidgets.QRadioButton(self.Grupa_dioda2)
        self.Button_ON_P2.setGeometry(QtCore.QRect(40, 30, 112, 23))
        self.Button_ON_P2.setObjectName("Button_ON_P2")
        
        self.Button_OFF_P2 = QtWidgets.QRadioButton(self.Grupa_dioda2)
        self.Button_OFF_P2.setGeometry(QtCore.QRect(110, 30, 112, 23))
        self.Button_OFF_P2.setObjectName("Button_OFF_P2")
        
        self.horizontalLayout_12.addWidget(self.Grupa_dioda2)
        self.Widget_PWM_2 = QtWidgets.QFrame(self.Glowna_ramka)
        self.Widget_PWM_2.setGeometry(QtCore.QRect(10, 500, 721, 161))
        self.Widget_PWM_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget_PWM_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget_PWM_2.setObjectName("Widget_PWM_2")
        
        self.Generowanie_PWM2_check = QtWidgets.QCheckBox(self.Widget_PWM_2)
        self.Generowanie_PWM2_check.setGeometry(QtCore.QRect(10, 0, 211, 25))
        self.Generowanie_PWM2_check.setObjectName("Generowanie_PWM2_check")
        
        self.Slider_wypelnienie_PWM2 = QtWidgets.QSlider(self.Widget_PWM_2)
        self.Slider_wypelnienie_PWM2.setGeometry(QtCore.QRect(220, 110, 441, 31))
        self.Slider_wypelnienie_PWM2.setMaximum(100)
        self.Slider_wypelnienie_PWM2.setTracking(False)
        self.Slider_wypelnienie_PWM2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_wypelnienie_PWM2.setInvertedAppearance(False)
        self.Slider_wypelnienie_PWM2.setInvertedControls(False)
        self.Slider_wypelnienie_PWM2.setObjectName("Slider_wypelnienie_PWM2")
        
        self.label_akt_wyp_PWM2_2 = QtWidgets.QLabel(self.Widget_PWM_2)
        self.label_akt_wyp_PWM2_2.setGeometry(QtCore.QRect(220, 140, 21, 17))
        self.label_akt_wyp_PWM2_2.setObjectName("label_akt_wyp_PWM2_2")
        
        self.label_100slider_PWM2 = QtWidgets.QLabel(self.Widget_PWM_2)
        self.label_100slider_PWM2.setGeometry(QtCore.QRect(620, 140, 51, 17))
        self.label_100slider_PWM2.setObjectName("label_100slider_PWM2")
        
        self.label_9 = QtWidgets.QLabel(self.Widget_PWM_2)
        self.label_9.setGeometry(QtCore.QRect(390, 130, 91, 17))
        self.label_9.setObjectName("label_9")
        
        self.Button_Aktualizacja_PWM2 = QtWidgets.QPushButton(self.Widget_PWM_2)
        self.Button_Aktualizacja_PWM2.setGeometry(QtCore.QRect(30, 100, 121, 31))
        self.Button_Aktualizacja_PWM2.setObjectName("Button_Aktualizacja_PWM2")
        
        self.lcd_aktualny_na_pinie_PWM2 = QtWidgets.QLCDNumber(self.Widget_PWM_2)
        self.lcd_aktualny_na_pinie_PWM2.setGeometry(QtCore.QRect(260, 50, 100, 40))
        self.lcd_aktualny_na_pinie_PWM2.setObjectName("lcd_aktualny_na_pinie_PWM2")
        
        self.lcd_zadany_PWM2 = QtWidgets.QLCDNumber(self.Widget_PWM_2)
        self.lcd_zadany_PWM2.setGeometry(QtCore.QRect(550, 50, 100, 40))
        self.lcd_zadany_PWM2.setObjectName("lcd_zadany_PWM2")
        
        self.label_akt_wyp_PWM2 = QtWidgets.QLabel(self.Widget_PWM_2)
        self.label_akt_wyp_PWM2.setGeometry(QtCore.QRect(230, 20, 171, 21))
        self.label_akt_wyp_PWM2.setObjectName("label_akt_wyp_PWM2")
        
        self.label_wybrane_wyp_PWM2 = QtWidgets.QLabel(self.Widget_PWM_2)
        self.label_wybrane_wyp_PWM2.setGeometry(QtCore.QRect(520, 20, 171, 21))
        self.label_wybrane_wyp_PWM2.setObjectName("label_wybrane_wyp_PWM2")
        
        self.comboBox_czestotliwosc_PWM2 = QtWidgets.QComboBox(self.Widget_PWM_2)
        self.comboBox_czestotliwosc_PWM2.setGeometry(QtCore.QRect(30, 40, 121, 41))
        self.comboBox_czestotliwosc_PWM2.setObjectName("comboBox_czestotliwosc_PWM2")
        self.comboBox_czestotliwosc_PWM2.addItem("")
        self.comboBox_czestotliwosc_PWM2.addItem("")
        self.comboBox_czestotliwosc_PWM2.addItem("")
        self.comboBox_czestotliwosc_PWM2.addItem("")
        self.comboBox_czestotliwosc_PWM2.addItem("")
        self.comboBox_czestotliwosc_PWM2.addItem("")
        
        self.Widget_diody_12V = QtWidgets.QFrame(self.Glowna_ramka)
        self.Widget_diody_12V.setGeometry(QtCore.QRect(10, 140, 720, 81))
        self.Widget_diody_12V.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget_diody_12V.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget_diody_12V.setObjectName("Widget_diody_12V")
        
        self.Kontrola_PIN12V_check = QtWidgets.QCheckBox(self.Widget_diody_12V)
        self.Kontrola_PIN12V_check.setGeometry(QtCore.QRect(10, 0, 130, 25))
        self.Kontrola_PIN12V_check.setObjectName("Kontrola_PIN12V_check")
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Widget_diody_12V)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 10, 561, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.Grupa_dioda2_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.Grupa_dioda2_3.setObjectName("Grupa_dioda2_3")
        
        self.Button_ON_P3 = QtWidgets.QRadioButton(self.Grupa_dioda2_3)
        self.Button_ON_P3.setGeometry(QtCore.QRect(40, 30, 112, 23))
        self.Button_ON_P3.setObjectName("Button_ON_P3")
        
        self.Button_OFF_P3 = QtWidgets.QRadioButton(self.Grupa_dioda2_3)
        self.Button_OFF_P3.setGeometry(QtCore.QRect(130, 30, 112, 23))
        self.Button_OFF_P3.setObjectName("Button_OFF_P3")
        
        self.horizontalLayout_13.addWidget(self.Grupa_dioda2_3)
        self.Grupa_dioda2_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.Grupa_dioda2_2.setObjectName("Grupa_dioda2_2")
        
        self.Button_ON_P4 = QtWidgets.QRadioButton(self.Grupa_dioda2_2)
        self.Button_ON_P4.setGeometry(QtCore.QRect(40, 30, 112, 23))
        self.Button_ON_P4.setObjectName("Button_ON_P4")
        
        self.Button_OFF_P4 = QtWidgets.QRadioButton(self.Grupa_dioda2_2)
        self.Button_OFF_P4.setGeometry(QtCore.QRect(110, 30, 112, 23))
        self.Button_OFF_P4.setObjectName("Button_OFF_P4")
        
        self.horizontalLayout_13.addWidget(self.Grupa_dioda2_2)
        self.Widget_predkosc_obrotowa = QtWidgets.QFrame(self.Glowna_ramka)
        self.Widget_predkosc_obrotowa.setGeometry(QtCore.QRect(10, 670, 721, 91))
        self.Widget_predkosc_obrotowa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget_predkosc_obrotowa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget_predkosc_obrotowa.setObjectName("Widget_predkosc_obrotowa")
       
        self.Pomiar_pr_obrotowej = QtWidgets.QCheckBox(self.Widget_predkosc_obrotowa)
        self.Pomiar_pr_obrotowej.setGeometry(QtCore.QRect(10, 10, 211, 25))
        self.Pomiar_pr_obrotowej.setObjectName("Pomiar_pr_obrotowej")
        
        self.Label_wartosc_pr_obrt = QtWidgets.QLabel(self.Widget_predkosc_obrotowa)
        self.Label_wartosc_pr_obrt.setGeometry(QtCore.QRect(530, 10, 141, 17))
        self.Label_wartosc_pr_obrt.setObjectName("Label_wartosc_pr_obrt")
        
        self.lcd_pomiar_pr_obrt = QtWidgets.QLCDNumber(self.Widget_predkosc_obrotowa)
        self.lcd_pomiar_pr_obrt.setGeometry(QtCore.QRect(550, 30, 100, 40))
        self.lcd_pomiar_pr_obrt.setObjectName("lcd_pomiar_pr_obrt")
        
        self.comboBox_kanal_pr_pomiar = QtWidgets.QComboBox(self.Widget_predkosc_obrotowa)
        self.comboBox_kanal_pr_pomiar.setGeometry(QtCore.QRect(310, 30, 101, 41))
        self.comboBox_kanal_pr_pomiar.setObjectName("comboBox_kanal_pr_pomiar")
        self.comboBox_kanal_pr_pomiar.addItem("")
        self.comboBox_kanal_pr_pomiar.addItem("")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Pomiar_adc_check.setText(_translate("MainWindow", "Pomiar ADC"))
        self.Label_wartosc_pomiar.setText(_translate("MainWindow", "Wartosc pomiaru :"))
        self.comboBox_czestotliwosc_pomiar.setItemText(0, _translate("MainWindow", "1Hz"))
        self.comboBox_czestotliwosc_pomiar.setItemText(1, _translate("MainWindow", "5Hz"))
        self.comboBox_czestotliwosc_pomiar.setItemText(2, _translate("MainWindow", "10Hz"))
        self.comboBox_czestotliwosc_pomiar.setItemText(3, _translate("MainWindow", "20Hz"))
        self.comboBox_czestotliwosc_pomiar.setItemText(4, _translate("MainWindow", "50Hz"))
        self.comboBox_czestotliwosc_pomiar.setItemText(5, _translate("MainWindow", "100Hz"))
        self.Label_Czestotliwosc_pomiaru.setText(_translate("MainWindow", "Częstotliwość"))
        self.comboBox_kanal_pomiar.setItemText(0, _translate("MainWindow", "Pin 5"))
        self.comboBox_kanal_pomiar.setItemText(1, _translate("MainWindow", "Pin 6"))
        self.comboBox_kanal_pomiar.setItemText(2, _translate("MainWindow", "Pin 7"))
        self.comboBox_kanal_pomiar.setItemText(3, _translate("MainWindow", "Pin 8"))
        self.Label_Kanal_pomiar.setText(_translate("MainWindow", "Kanał"))
        self.comboBox_Vref_pomiar.setItemText(0, _translate("MainWindow", "5V"))
        self.comboBox_Vref_pomiar.setItemText(1, _translate("MainWindow", "12V"))
        self.Label_Vref_pomiar.setText(_translate("MainWindow", "Vref"))
        self.Generowanie_PWM1_check.setText(_translate("MainWindow", "Generowanie PWM 1"))
        self.label_0slider_PWM1.setText(_translate("MainWindow", "0%"))
        self.label_100slider_PWM1.setText(_translate("MainWindow", "100%"))
        self.label_7.setText(_translate("MainWindow", "Wypełnienie"))
        self.Button_Aktualizacja_PWM1.setText(_translate("MainWindow", "Aktualizacja"))
        self.label_akt_wyp_PWM1.setText(_translate("MainWindow", "Aktualne wypełnienie % :"))
        self.label_wybrane_wyp_PWM1.setText(_translate("MainWindow", "Wybrane wypełnienie % :"))
        self.comboBox_czestotliwosc_PWM1.setItemText(0, _translate("MainWindow", "1Hz"))
        self.comboBox_czestotliwosc_PWM1.setItemText(1, _translate("MainWindow", "5Hz"))
        self.comboBox_czestotliwosc_PWM1.setItemText(2, _translate("MainWindow", "10Hz"))
        self.comboBox_czestotliwosc_PWM1.setItemText(3, _translate("MainWindow", "20Hz"))
        self.comboBox_czestotliwosc_PWM1.setItemText(4, _translate("MainWindow", "50Hz"))
        self.comboBox_czestotliwosc_PWM1.setItemText(5, _translate("MainWindow", "100Hz"))
        self.LABEL_TYTULPROGRAMU.setText(_translate("MainWindow", "Program główny"))
        self.Kontrola_PIN5V_check.setText(_translate("MainWindow", "PIN (0 - 5V)"))
        self.Grupa_dioda1.setTitle(_translate("MainWindow", "Pin 1"))
        self.Button_ON_P1.setText(_translate("MainWindow", "On"))
        self.Button_OFF_P1.setText(_translate("MainWindow", "Off"))
        self.Grupa_dioda2.setTitle(_translate("MainWindow", "Pin 2"))
        self.Button_ON_P2.setText(_translate("MainWindow", "On"))
        self.Button_OFF_P2.setText(_translate("MainWindow", "Off"))
        self.Generowanie_PWM2_check.setText(_translate("MainWindow", "Generowanie PWM 2"))
        self.label_akt_wyp_PWM2_2.setText(_translate("MainWindow", "0%"))
        self.label_100slider_PWM2.setText(_translate("MainWindow", "100%"))
        self.label_9.setText(_translate("MainWindow", "Wypełnienie"))
        self.Button_Aktualizacja_PWM2.setText(_translate("MainWindow", "Aktualizacja"))
        self.label_akt_wyp_PWM2.setText(_translate("MainWindow", "Aktualne wypełnienie % :"))
        self.label_wybrane_wyp_PWM2.setText(_translate("MainWindow", "Wybrane wypełnienie % :"))
        self.comboBox_czestotliwosc_PWM2.setItemText(0, _translate("MainWindow", "1Hz"))
        self.comboBox_czestotliwosc_PWM2.setItemText(1, _translate("MainWindow", "5Hz"))
        self.comboBox_czestotliwosc_PWM2.setItemText(2, _translate("MainWindow", "10Hz"))
        self.comboBox_czestotliwosc_PWM2.setItemText(3, _translate("MainWindow", "20Hz"))
        self.comboBox_czestotliwosc_PWM2.setItemText(4, _translate("MainWindow", "50Hz"))
        self.comboBox_czestotliwosc_PWM2.setItemText(5, _translate("MainWindow", "100Hz"))
        self.Kontrola_PIN12V_check.setText(_translate("MainWindow", "PIN (0 - 12V)"))
        self.Grupa_dioda2_3.setTitle(_translate("MainWindow", "Pin 3"))
        self.Button_ON_P3.setText(_translate("MainWindow", "On"))
        self.Button_OFF_P3.setText(_translate("MainWindow", "Off"))
        self.Grupa_dioda2_2.setTitle(_translate("MainWindow", "Pin 4"))
        self.Button_ON_P4.setText(_translate("MainWindow", "On"))
        self.Button_OFF_P4.setText(_translate("MainWindow", "Off"))
        self.Pomiar_pr_obrotowej.setText(_translate("MainWindow", "Pomiar prędkości obrotowej"))
        self.Label_wartosc_pr_obrt.setText(_translate("MainWindow", "Prędkość [obr/min] :"))
        self.comboBox_kanal_pr_pomiar.setItemText(0, _translate("MainWindow", "Pin 11"))
        self.comboBox_kanal_pr_pomiar.setItemText(1, _translate("MainWindow", "Pin 12"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
