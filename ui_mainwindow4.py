# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow4.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form4(object):
    def setupUi(self, Form4):
        if not Form4.objectName():
            Form4.setObjectName(u"Form4")
        Form4.resize(1057, 639)
        self.centralwidget = QWidget(Form4)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_marka = QLineEdit(self.centralwidget)
        self.lineEdit_marka.setObjectName(u"lineEdit_marka")

        self.gridLayout.addWidget(self.lineEdit_marka, 2, 1, 1, 1)

        self.label_motorno = QLabel(self.centralwidget)
        self.label_motorno.setObjectName(u"label_motorno")

        self.gridLayout.addWidget(self.label_motorno, 1, 4, 1, 1)

        self.label_uretimyili = QLabel(self.centralwidget)
        self.label_uretimyili.setObjectName(u"label_uretimyili")

        self.gridLayout.addWidget(self.label_uretimyili, 4, 0, 1, 1)

        self.lineEdit_uretimyili = QLineEdit(self.centralwidget)
        self.lineEdit_uretimyili.setObjectName(u"lineEdit_uretimyili")

        self.gridLayout.addWidget(self.lineEdit_uretimyili, 4, 1, 1, 1)

        self.pushButton_kaydet = QPushButton(self.centralwidget)
        self.pushButton_kaydet.setObjectName(u"pushButton_kaydet")

        self.gridLayout.addWidget(self.pushButton_kaydet, 2, 7, 1, 1)

        self.label_vites = QLabel(self.centralwidget)
        self.label_vites.setObjectName(u"label_vites")

        self.gridLayout.addWidget(self.label_vites, 0, 2, 1, 1)

        self.label_motorhacmi = QLabel(self.centralwidget)
        self.label_motorhacmi.setObjectName(u"label_motorhacmi")

        self.gridLayout.addWidget(self.label_motorhacmi, 3, 2, 1, 1)

        self.label_yakitturu = QLabel(self.centralwidget)
        self.label_yakitturu.setObjectName(u"label_yakitturu")

        self.gridLayout.addWidget(self.label_yakitturu, 5, 0, 1, 1)

        self.lineEdit_gunlukkira = QLineEdit(self.centralwidget)
        self.lineEdit_gunlukkira.setObjectName(u"lineEdit_gunlukkira")

        self.gridLayout.addWidget(self.lineEdit_gunlukkira, 3, 6, 1, 1)

        self.label_marka = QLabel(self.centralwidget)
        self.label_marka.setObjectName(u"label_marka")

        self.gridLayout.addWidget(self.label_marka, 2, 0, 1, 1)

        self.lineEdit_vites = QLineEdit(self.centralwidget)
        self.lineEdit_vites.setObjectName(u"lineEdit_vites")

        self.gridLayout.addWidget(self.lineEdit_vites, 0, 3, 1, 1)

        self.pushButton_ara = QPushButton(self.centralwidget)
        self.pushButton_ara.setObjectName(u"pushButton_ara")

        self.gridLayout.addWidget(self.pushButton_ara, 4, 7, 1, 1)

        self.lineEdit_kapi = QLineEdit(self.centralwidget)
        self.lineEdit_kapi.setObjectName(u"lineEdit_kapi")

        self.gridLayout.addWidget(self.lineEdit_kapi, 5, 3, 1, 1)

        self.lineEdit_aracturu = QLineEdit(self.centralwidget)
        self.lineEdit_aracturu.setObjectName(u"lineEdit_aracturu")

        self.gridLayout.addWidget(self.lineEdit_aracturu, 1, 1, 1, 1)

        self.lineEdit_cekis = QLineEdit(self.centralwidget)
        self.lineEdit_cekis.setObjectName(u"lineEdit_cekis")

        self.gridLayout.addWidget(self.lineEdit_cekis, 4, 3, 1, 1)

        self.lineEdit_model = QLineEdit(self.centralwidget)
        self.lineEdit_model.setObjectName(u"lineEdit_model")

        self.gridLayout.addWidget(self.lineEdit_model, 3, 1, 1, 1)

        self.lineEdit_motorno = QLineEdit(self.centralwidget)
        self.lineEdit_motorno.setObjectName(u"lineEdit_motorno")

        self.gridLayout.addWidget(self.lineEdit_motorno, 1, 6, 1, 1)

        self.label_kiradami = QLabel(self.centralwidget)
        self.label_kiradami.setObjectName(u"label_kiradami")

        self.gridLayout.addWidget(self.label_kiradami, 4, 4, 1, 1)

        self.pushButton_sil = QPushButton(self.centralwidget)
        self.pushButton_sil.setObjectName(u"pushButton_sil")

        self.gridLayout.addWidget(self.pushButton_sil, 3, 7, 1, 1)

        self.label_sasino = QLabel(self.centralwidget)
        self.label_sasino.setObjectName(u"label_sasino")

        self.gridLayout.addWidget(self.label_sasino, 2, 4, 1, 1)

        self.lineEdit_motorgucu = QLineEdit(self.centralwidget)
        self.lineEdit_motorgucu.setObjectName(u"lineEdit_motorgucu")

        self.gridLayout.addWidget(self.lineEdit_motorgucu, 1, 3, 1, 1)

        self.lineEdit_sasino = QLineEdit(self.centralwidget)
        self.lineEdit_sasino.setObjectName(u"lineEdit_sasino")

        self.gridLayout.addWidget(self.lineEdit_sasino, 2, 6, 1, 1)

        self.label_gunlukkira = QLabel(self.centralwidget)
        self.label_gunlukkira.setObjectName(u"label_gunlukkira")

        self.gridLayout.addWidget(self.label_gunlukkira, 3, 4, 1, 1)

        self.label_motorgucu = QLabel(self.centralwidget)
        self.label_motorgucu.setObjectName(u"label_motorgucu")

        self.gridLayout.addWidget(self.label_motorgucu, 1, 2, 1, 1)

        self.label_kasatipi = QLabel(self.centralwidget)
        self.label_kasatipi.setObjectName(u"label_kasatipi")

        self.gridLayout.addWidget(self.label_kasatipi, 2, 2, 1, 1)

        self.lineEdit_yakitturu = QLineEdit(self.centralwidget)
        self.lineEdit_yakitturu.setObjectName(u"lineEdit_yakitturu")

        self.gridLayout.addWidget(self.lineEdit_yakitturu, 5, 1, 1, 1)

        self.label_aracturu = QLabel(self.centralwidget)
        self.label_aracturu.setObjectName(u"label_aracturu")

        self.gridLayout.addWidget(self.label_aracturu, 1, 0, 1, 1)

        self.lineEdit_motorhacmi = QLineEdit(self.centralwidget)
        self.lineEdit_motorhacmi.setObjectName(u"lineEdit_motorhacmi")

        self.gridLayout.addWidget(self.lineEdit_motorhacmi, 3, 3, 1, 1)

        self.label_kullanimdisimi = QLabel(self.centralwidget)
        self.label_kullanimdisimi.setObjectName(u"label_kullanimdisimi")

        self.gridLayout.addWidget(self.label_kullanimdisimi, 5, 4, 1, 1)

        self.pushButton_yeni = QPushButton(self.centralwidget)
        self.pushButton_yeni.setObjectName(u"pushButton_yeni")

        self.gridLayout.addWidget(self.pushButton_yeni, 0, 7, 1, 1)

        self.pushButton_kapat = QPushButton(self.centralwidget)
        self.pushButton_kapat.setObjectName(u"pushButton_kapat")

        self.gridLayout.addWidget(self.pushButton_kapat, 5, 7, 1, 1)

        self.lineEdit_kasatipi = QLineEdit(self.centralwidget)
        self.lineEdit_kasatipi.setObjectName(u"lineEdit_kasatipi")

        self.gridLayout.addWidget(self.lineEdit_kasatipi, 2, 3, 1, 1)

        self.pushButton_guncelle = QPushButton(self.centralwidget)
        self.pushButton_guncelle.setObjectName(u"pushButton_guncelle")

        self.gridLayout.addWidget(self.pushButton_guncelle, 1, 7, 1, 1)

        self.label_kapi = QLabel(self.centralwidget)
        self.label_kapi.setObjectName(u"label_kapi")

        self.gridLayout.addWidget(self.label_kapi, 5, 2, 1, 1)

        self.label_renk = QLabel(self.centralwidget)
        self.label_renk.setObjectName(u"label_renk")

        self.gridLayout.addWidget(self.label_renk, 0, 4, 1, 1)

        self.label_id = QLabel(self.centralwidget)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.label_cekis = QLabel(self.centralwidget)
        self.label_cekis.setObjectName(u"label_cekis")

        self.gridLayout.addWidget(self.label_cekis, 4, 2, 1, 1)

        self.label_model = QLabel(self.centralwidget)
        self.label_model.setObjectName(u"label_model")

        self.gridLayout.addWidget(self.label_model, 3, 0, 1, 1)

        self.lineEdit_renk = QLineEdit(self.centralwidget)
        self.lineEdit_renk.setObjectName(u"lineEdit_renk")

        self.gridLayout.addWidget(self.lineEdit_renk, 0, 6, 1, 1)

        self.lineEdit_id = QLineEdit(self.centralwidget)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_id, 0, 1, 1, 1)

        self.checkBox_kiradami = QCheckBox(self.centralwidget)
        self.checkBox_kiradami.setObjectName(u"checkBox_kiradami")
        font = QFont()
        font.setBold(False)
        self.checkBox_kiradami.setFont(font)

        self.gridLayout.addWidget(self.checkBox_kiradami, 4, 6, 1, 1)

        self.checkBox_kullanimdisimi = QCheckBox(self.centralwidget)
        self.checkBox_kullanimdisimi.setObjectName(u"checkBox_kullanimdisimi")

        self.gridLayout.addWidget(self.checkBox_kullanimdisimi, 5, 6, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.centralwidget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_2.addWidget(self.tableWidget_2, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        Form4.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Form4)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1057, 21))
        self.menuArac_Bilgileri_Girisi = QMenu(self.menubar)
        self.menuArac_Bilgileri_Girisi.setObjectName(u"menuArac_Bilgileri_Girisi")
        Form4.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form4)
        self.statusbar.setObjectName(u"statusbar")
        Form4.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_aracturu, self.lineEdit_marka)
        QWidget.setTabOrder(self.lineEdit_marka, self.lineEdit_model)
        QWidget.setTabOrder(self.lineEdit_model, self.lineEdit_uretimyili)
        QWidget.setTabOrder(self.lineEdit_uretimyili, self.lineEdit_yakitturu)
        QWidget.setTabOrder(self.lineEdit_yakitturu, self.lineEdit_vites)
        QWidget.setTabOrder(self.lineEdit_vites, self.lineEdit_motorgucu)
        QWidget.setTabOrder(self.lineEdit_motorgucu, self.lineEdit_kasatipi)
        QWidget.setTabOrder(self.lineEdit_kasatipi, self.lineEdit_motorhacmi)
        QWidget.setTabOrder(self.lineEdit_motorhacmi, self.lineEdit_cekis)
        QWidget.setTabOrder(self.lineEdit_cekis, self.lineEdit_kapi)
        QWidget.setTabOrder(self.lineEdit_kapi, self.lineEdit_renk)
        QWidget.setTabOrder(self.lineEdit_renk, self.lineEdit_motorno)
        QWidget.setTabOrder(self.lineEdit_motorno, self.lineEdit_sasino)
        QWidget.setTabOrder(self.lineEdit_sasino, self.lineEdit_gunlukkira)
        QWidget.setTabOrder(self.lineEdit_gunlukkira, self.pushButton_yeni)
        QWidget.setTabOrder(self.pushButton_yeni, self.pushButton_guncelle)
        QWidget.setTabOrder(self.pushButton_guncelle, self.pushButton_kaydet)
        QWidget.setTabOrder(self.pushButton_kaydet, self.pushButton_sil)
        QWidget.setTabOrder(self.pushButton_sil, self.pushButton_ara)
        QWidget.setTabOrder(self.pushButton_ara, self.pushButton_kapat)
        QWidget.setTabOrder(self.pushButton_kapat, self.lineEdit_id)

        self.menubar.addAction(self.menuArac_Bilgileri_Girisi.menuAction())

        self.retranslateUi(Form4)

        QMetaObject.connectSlotsByName(Form4)
    # setupUi

    def retranslateUi(self, Form4):
        Form4.setWindowTitle(QCoreApplication.translate("Form4", u"MainWindow", None))
        self.label_motorno.setText(QCoreApplication.translate("Form4", u"Motor No:", None))
        self.label_uretimyili.setText(QCoreApplication.translate("Form4", u"\u00dcretim Y\u0131l\u0131:", None))
        self.pushButton_kaydet.setText(QCoreApplication.translate("Form4", u"Kaydet", None))
        self.label_vites.setText(QCoreApplication.translate("Form4", u"Vites:", None))
        self.label_motorhacmi.setText(QCoreApplication.translate("Form4", u"Motor Hacmi:", None))
        self.label_yakitturu.setText(QCoreApplication.translate("Form4", u"Yak\u0131t T\u00fcr\u00fc:", None))
        self.label_marka.setText(QCoreApplication.translate("Form4", u"Marka:", None))
        self.pushButton_ara.setText(QCoreApplication.translate("Form4", u"Ara", None))
        self.label_kiradami.setText(QCoreApplication.translate("Form4", u"Kirada m\u0131?", None))
        self.pushButton_sil.setText(QCoreApplication.translate("Form4", u"Sil", None))
        self.label_sasino.setText(QCoreApplication.translate("Form4", u"\u015easi No:", None))
        self.label_gunlukkira.setText(QCoreApplication.translate("Form4", u"G\u00fcnl\u00fck Kiralama Bedeli:", None))
        self.label_motorgucu.setText(QCoreApplication.translate("Form4", u"Motor G\u00fcc\u00fc:", None))
        self.label_kasatipi.setText(QCoreApplication.translate("Form4", u"Kasa Tipi:", None))
        self.label_aracturu.setText(QCoreApplication.translate("Form4", u"Ara\u00e7 T\u00fcr\u00fc:", None))
        self.label_kullanimdisimi.setText(QCoreApplication.translate("Form4", u"Kullan\u0131m D\u0131\u015f\u0131 M\u0131?", None))
        self.pushButton_yeni.setText(QCoreApplication.translate("Form4", u"Yeni", None))
        self.pushButton_kapat.setText(QCoreApplication.translate("Form4", u"Kapat", None))
        self.pushButton_guncelle.setText(QCoreApplication.translate("Form4", u"G\u00fcncelle", None))
        self.label_kapi.setText(QCoreApplication.translate("Form4", u"Kap\u0131:", None))
        self.label_renk.setText(QCoreApplication.translate("Form4", u"Renk:", None))
        self.label_id.setText(QCoreApplication.translate("Form4", u"id:", None))
        self.label_cekis.setText(QCoreApplication.translate("Form4", u"\u00c7eki\u015f:", None))
        self.label_model.setText(QCoreApplication.translate("Form4", u"Model:", None))
        self.checkBox_kiradami.setText("")
        self.checkBox_kullanimdisimi.setText("")
        self.menuArac_Bilgileri_Girisi.setTitle(QCoreApplication.translate("Form4", u"Arac Bilgileri Girisi", None))
    # retranslateUi

