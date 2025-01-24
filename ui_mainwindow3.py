# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow3.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form3(object):
    def setupUi(self, Form3):
        if not Form3.objectName():
            Form3.setObjectName(u"Form3")
        Form3.resize(774, 443)
        self.centralwidget = QWidget(Form3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.aracmarka_comboBox = QComboBox(self.centralwidget)
        self.aracmarka_comboBox.setObjectName(u"aracmarka_comboBox")

        self.gridLayout.addWidget(self.aracmarka_comboBox, 0, 4, 1, 1)

        self.id_label = QLabel(self.centralwidget)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout.addWidget(self.id_label, 1, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.centralwidget)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.id_lineEdit, 1, 1, 1, 1)

        self.yeni_pushButton = QPushButton(self.centralwidget)
        self.yeni_pushButton.setObjectName(u"yeni_pushButton")

        self.gridLayout.addWidget(self.yeni_pushButton, 0, 5, 1, 1)

        self.saat_lcdNumber = QLCDNumber(self.centralwidget)
        self.saat_lcdNumber.setObjectName(u"saat_lcdNumber")

        self.gridLayout.addWidget(self.saat_lcdNumber, 0, 0, 1, 1)

        self.aracmarka_label = QLabel(self.centralwidget)
        self.aracmarka_label.setObjectName(u"aracmarka_label")

        self.gridLayout.addWidget(self.aracmarka_label, 0, 3, 1, 1)

        self.musterisoyadi_comboBox = QComboBox(self.centralwidget)
        self.musterisoyadi_comboBox.setObjectName(u"musterisoyadi_comboBox")

        self.gridLayout.addWidget(self.musterisoyadi_comboBox, 5, 1, 1, 1)

        self.tarih_lcdNumber = QLCDNumber(self.centralwidget)
        self.tarih_lcdNumber.setObjectName(u"tarih_lcdNumber")

        self.gridLayout.addWidget(self.tarih_lcdNumber, 0, 1, 1, 1)

        self.kacgunkiralanacak_lineEdit = QLineEdit(self.centralwidget)
        self.kacgunkiralanacak_lineEdit.setObjectName(u"kacgunkiralanacak_lineEdit")

        self.gridLayout.addWidget(self.kacgunkiralanacak_lineEdit, 3, 4, 1, 1)

        self.musterisoyadi_label = QLabel(self.centralwidget)
        self.musterisoyadi_label.setObjectName(u"musterisoyadi_label")

        self.gridLayout.addWidget(self.musterisoyadi_label, 5, 0, 1, 1)

        self.aracmodel_comboBox = QComboBox(self.centralwidget)
        self.aracmodel_comboBox.setObjectName(u"aracmodel_comboBox")

        self.gridLayout.addWidget(self.aracmodel_comboBox, 1, 4, 1, 1)

        self.yolculuknereye_label = QLabel(self.centralwidget)
        self.yolculuknereye_label.setObjectName(u"yolculuknereye_label")

        self.gridLayout.addWidget(self.yolculuknereye_label, 5, 3, 1, 1)

        self.musteriadi_label = QLabel(self.centralwidget)
        self.musteriadi_label.setObjectName(u"musteriadi_label")

        self.gridLayout.addWidget(self.musteriadi_label, 3, 0, 1, 1)

        self.yolculuknereye_lineEdit = QLineEdit(self.centralwidget)
        self.yolculuknereye_lineEdit.setObjectName(u"yolculuknereye_lineEdit")

        self.gridLayout.addWidget(self.yolculuknereye_lineEdit, 5, 4, 1, 1)

        self.kapat_pushButton = QPushButton(self.centralwidget)
        self.kapat_pushButton.setObjectName(u"kapat_pushButton")

        self.gridLayout.addWidget(self.kapat_pushButton, 5, 5, 1, 1)

        self.sil_pushButton = QPushButton(self.centralwidget)
        self.sil_pushButton.setObjectName(u"sil_pushButton")

        self.gridLayout.addWidget(self.sil_pushButton, 3, 5, 1, 1)

        self.musteriadi_comboBox = QComboBox(self.centralwidget)
        self.musteriadi_comboBox.setObjectName(u"musteriadi_comboBox")

        self.gridLayout.addWidget(self.musteriadi_comboBox, 3, 1, 1, 1)

        self.kacgunkiralanacak_label = QLabel(self.centralwidget)
        self.kacgunkiralanacak_label.setObjectName(u"kacgunkiralanacak_label")

        self.gridLayout.addWidget(self.kacgunkiralanacak_label, 3, 3, 1, 1)

        self.aracmodel_label = QLabel(self.centralwidget)
        self.aracmodel_label.setObjectName(u"aracmodel_label")

        self.gridLayout.addWidget(self.aracmodel_label, 1, 3, 1, 1)

        self.arabtn = QPushButton(self.centralwidget)
        self.arabtn.setObjectName(u"arabtn")

        self.gridLayout.addWidget(self.arabtn, 1, 5, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.akbg_tableWidget = QTableWidget(self.centralwidget)
        self.akbg_tableWidget.setObjectName(u"akbg_tableWidget")

        self.gridLayout_2.addWidget(self.akbg_tableWidget, 3, 0, 1, 2)

        self.kaydet_pushButton = QPushButton(self.centralwidget)
        self.kaydet_pushButton.setObjectName(u"kaydet_pushButton")

        self.gridLayout_2.addWidget(self.kaydet_pushButton, 1, 0, 1, 1)

        self.guncelle_pushButton = QPushButton(self.centralwidget)
        self.guncelle_pushButton.setObjectName(u"guncelle_pushButton")

        self.gridLayout_2.addWidget(self.guncelle_pushButton, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        Form3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Form3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 774, 21))
        self.menuArac_Kiralama_Bilgileri_Girisi = QMenu(self.menubar)
        self.menuArac_Kiralama_Bilgileri_Girisi.setObjectName(u"menuArac_Kiralama_Bilgileri_Girisi")
        Form3.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form3)
        self.statusbar.setObjectName(u"statusbar")
        Form3.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.id_lineEdit, self.musteriadi_comboBox)
        QWidget.setTabOrder(self.musteriadi_comboBox, self.musterisoyadi_comboBox)
        QWidget.setTabOrder(self.musterisoyadi_comboBox, self.aracmarka_comboBox)
        QWidget.setTabOrder(self.aracmarka_comboBox, self.aracmodel_comboBox)
        QWidget.setTabOrder(self.aracmodel_comboBox, self.kacgunkiralanacak_lineEdit)
        QWidget.setTabOrder(self.kacgunkiralanacak_lineEdit, self.yolculuknereye_lineEdit)
        QWidget.setTabOrder(self.yolculuknereye_lineEdit, self.yeni_pushButton)
        QWidget.setTabOrder(self.yeni_pushButton, self.sil_pushButton)
        QWidget.setTabOrder(self.sil_pushButton, self.kapat_pushButton)
        QWidget.setTabOrder(self.kapat_pushButton, self.kaydet_pushButton)
        QWidget.setTabOrder(self.kaydet_pushButton, self.akbg_tableWidget)

        self.menubar.addAction(self.menuArac_Kiralama_Bilgileri_Girisi.menuAction())

        self.retranslateUi(Form3)

        QMetaObject.connectSlotsByName(Form3)
    # setupUi

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(QCoreApplication.translate("Form3", u"MainWindow", None))
        self.id_label.setText(QCoreApplication.translate("Form3", u"id:", None))
        self.yeni_pushButton.setText(QCoreApplication.translate("Form3", u"Yeni", None))
        self.aracmarka_label.setText(QCoreApplication.translate("Form3", u"Ara\u00e7 Marka:", None))
        self.musterisoyadi_label.setText(QCoreApplication.translate("Form3", u"M\u00fc\u015fteri Soyad\u0131:", None))
        self.yolculuknereye_label.setText(QCoreApplication.translate("Form3", u"Yolculuk Nereye?:", None))
        self.musteriadi_label.setText(QCoreApplication.translate("Form3", u"M\u00fc\u015fteri Ad\u0131:", None))
        self.kapat_pushButton.setText(QCoreApplication.translate("Form3", u"Kapat", None))
        self.sil_pushButton.setText(QCoreApplication.translate("Form3", u"Sil", None))
        self.kacgunkiralanacak_label.setText(QCoreApplication.translate("Form3", u"Ka\u00e7 G\u00fcn Kiralanacak?:", None))
        self.aracmodel_label.setText(QCoreApplication.translate("Form3", u"Ara\u00e7 Model:", None))
        self.arabtn.setText(QCoreApplication.translate("Form3", u"Ara", None))
        self.kaydet_pushButton.setText(QCoreApplication.translate("Form3", u"Kaydet", None))
        self.guncelle_pushButton.setText(QCoreApplication.translate("Form3", u"G\u00fcncelle", None))
        self.menuArac_Kiralama_Bilgileri_Girisi.setTitle(QCoreApplication.translate("Form3", u"Arac Kiralama Bilgileri Girisi", None))
    # retranslateUi

