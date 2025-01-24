# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form2(object):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(1025, 586)
        self.centralwidget = QWidget(Form2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tckimliklabel = QLabel(self.centralwidget)
        self.tckimliklabel.setObjectName(u"tckimliklabel")
        self.tckimliklabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.tckimliklabel, 3, 0, 1, 1)

        self.medenidurumulabel = QLabel(self.centralwidget)
        self.medenidurumulabel.setObjectName(u"medenidurumulabel")
        self.medenidurumulabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.medenidurumulabel, 3, 2, 1, 1)

        self.soyadlineEdit = QLineEdit(self.centralwidget)
        self.soyadlineEdit.setObjectName(u"soyadlineEdit")
        self.soyadlineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.soyadlineEdit, 2, 1, 1, 1)

        self.egitimdurumulineEdit = QLineEdit(self.centralwidget)
        self.egitimdurumulineEdit.setObjectName(u"egitimdurumulineEdit")
        self.egitimdurumulineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.egitimdurumulineEdit, 4, 3, 1, 1)

        self.soyadlabel = QLabel(self.centralwidget)
        self.soyadlabel.setObjectName(u"soyadlabel")
        self.soyadlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.soyadlabel, 2, 0, 1, 1)

        self.idlabel = QLabel(self.centralwidget)
        self.idlabel.setObjectName(u"idlabel")
        self.idlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.idlabel, 0, 0, 1, 1)

        self.adlineEdit = QLineEdit(self.centralwidget)
        self.adlineEdit.setObjectName(u"adlineEdit")
        self.adlineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.adlineEdit, 1, 1, 1, 1)

        self.ehliyetlineEdit = QLineEdit(self.centralwidget)
        self.ehliyetlineEdit.setObjectName(u"ehliyetlineEdit")
        self.ehliyetlineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.ehliyetlineEdit, 2, 3, 1, 1)

        self.kaydetButton = QPushButton(self.centralwidget)
        self.kaydetButton.setObjectName(u"kaydetButton")

        self.gridLayout.addWidget(self.kaydetButton, 2, 4, 1, 1)

        self.medenidurumulineEdit = QLineEdit(self.centralwidget)
        self.medenidurumulineEdit.setObjectName(u"medenidurumulineEdit")
        self.medenidurumulineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.medenidurumulineEdit, 3, 3, 1, 1)

        self.adreslabel = QLabel(self.centralwidget)
        self.adreslabel.setObjectName(u"adreslabel")
        self.adreslabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.adreslabel, 5, 0, 1, 1)

        self.yeniButton = QPushButton(self.centralwidget)
        self.yeniButton.setObjectName(u"yeniButton")

        self.gridLayout.addWidget(self.yeniButton, 0, 4, 1, 1)

        self.tckimliklineEdit = QLineEdit(self.centralwidget)
        self.tckimliklineEdit.setObjectName(u"tckimliklineEdit")
        self.tckimliklineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.tckimliklineEdit, 3, 1, 1, 1)

        self.mesleklineEdit = QLineEdit(self.centralwidget)
        self.mesleklineEdit.setObjectName(u"mesleklineEdit")
        self.mesleklineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.mesleklineEdit, 1, 3, 1, 1)

        self.telnolineEdit = QLineEdit(self.centralwidget)
        self.telnolineEdit.setObjectName(u"telnolineEdit")
        self.telnolineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.telnolineEdit, 0, 3, 1, 1)

        self.guncelleButton = QPushButton(self.centralwidget)
        self.guncelleButton.setObjectName(u"guncelleButton")

        self.gridLayout.addWidget(self.guncelleButton, 1, 4, 1, 1)

        self.adlabel = QLabel(self.centralwidget)
        self.adlabel.setObjectName(u"adlabel")
        self.adlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.adlabel, 1, 0, 1, 1)

        self.ehliyetlabel = QLabel(self.centralwidget)
        self.ehliyetlabel.setObjectName(u"ehliyetlabel")
        self.ehliyetlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.ehliyetlabel, 2, 2, 1, 1)

        self.adreslineEdit = QLineEdit(self.centralwidget)
        self.adreslineEdit.setObjectName(u"adreslineEdit")
        self.adreslineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.adreslineEdit, 5, 1, 1, 1)

        self.egitimdurumulabel = QLabel(self.centralwidget)
        self.egitimdurumulabel.setObjectName(u"egitimdurumulabel")
        self.egitimdurumulabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.egitimdurumulabel, 4, 2, 1, 1)

        self.idlineEdit = QLineEdit(self.centralwidget)
        self.idlineEdit.setObjectName(u"idlineEdit")
        self.idlineEdit.setEnabled(False)
        self.idlineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.idlineEdit, 0, 1, 1, 1)

        self.dtarihilineEdit = QLineEdit(self.centralwidget)
        self.dtarihilineEdit.setObjectName(u"dtarihilineEdit")
        self.dtarihilineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.dtarihilineEdit, 4, 1, 1, 1)

        self.silButton = QPushButton(self.centralwidget)
        self.silButton.setObjectName(u"silButton")

        self.gridLayout.addWidget(self.silButton, 3, 4, 1, 1)

        self.mesleklabel = QLabel(self.centralwidget)
        self.mesleklabel.setObjectName(u"mesleklabel")
        self.mesleklabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.mesleklabel, 1, 2, 1, 1)

        self.araButton = QPushButton(self.centralwidget)
        self.araButton.setObjectName(u"araButton")

        self.gridLayout.addWidget(self.araButton, 4, 4, 1, 1)

        self.dtarihilabel = QLabel(self.centralwidget)
        self.dtarihilabel.setObjectName(u"dtarihilabel")
        self.dtarihilabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.dtarihilabel, 4, 0, 1, 1)

        self.telnolabel = QLabel(self.centralwidget)
        self.telnolabel.setObjectName(u"telnolabel")
        self.telnolabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.telnolabel, 0, 2, 1, 1)

        self.kapatButton = QPushButton(self.centralwidget)
        self.kapatButton.setObjectName(u"kapatButton")

        self.gridLayout.addWidget(self.kapatButton, 5, 4, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        Form2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Form2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1025, 21))
        self.menuMusteri_Bilgileri_Girisi = QMenu(self.menubar)
        self.menuMusteri_Bilgileri_Girisi.setObjectName(u"menuMusteri_Bilgileri_Girisi")
        Form2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form2)
        self.statusbar.setObjectName(u"statusbar")
        Form2.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.adlineEdit, self.soyadlineEdit)
        QWidget.setTabOrder(self.soyadlineEdit, self.tckimliklineEdit)
        QWidget.setTabOrder(self.tckimliklineEdit, self.dtarihilineEdit)
        QWidget.setTabOrder(self.dtarihilineEdit, self.adreslineEdit)
        QWidget.setTabOrder(self.adreslineEdit, self.telnolineEdit)
        QWidget.setTabOrder(self.telnolineEdit, self.mesleklineEdit)
        QWidget.setTabOrder(self.mesleklineEdit, self.ehliyetlineEdit)
        QWidget.setTabOrder(self.ehliyetlineEdit, self.medenidurumulineEdit)
        QWidget.setTabOrder(self.medenidurumulineEdit, self.egitimdurumulineEdit)
        QWidget.setTabOrder(self.egitimdurumulineEdit, self.yeniButton)
        QWidget.setTabOrder(self.yeniButton, self.guncelleButton)
        QWidget.setTabOrder(self.guncelleButton, self.kaydetButton)
        QWidget.setTabOrder(self.kaydetButton, self.silButton)
        QWidget.setTabOrder(self.silButton, self.araButton)
        QWidget.setTabOrder(self.araButton, self.kapatButton)
        QWidget.setTabOrder(self.kapatButton, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.idlineEdit)

        self.menubar.addAction(self.menuMusteri_Bilgileri_Girisi.menuAction())

        self.retranslateUi(Form2)

        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"MainWindow", None))
        self.tckimliklabel.setText(QCoreApplication.translate("Form2", u"TC Kimlik No:", None))
        self.medenidurumulabel.setText(QCoreApplication.translate("Form2", u"Medeni Durumu:", None))
        self.soyadlabel.setText(QCoreApplication.translate("Form2", u"Soyad:", None))
        self.idlabel.setText(QCoreApplication.translate("Form2", u"id:", None))
        self.kaydetButton.setText(QCoreApplication.translate("Form2", u"Kaydet", None))
        self.adreslabel.setText(QCoreApplication.translate("Form2", u"Adres:", None))
        self.yeniButton.setText(QCoreApplication.translate("Form2", u"Yeni", None))
        self.guncelleButton.setText(QCoreApplication.translate("Form2", u"G\u00fcncelle", None))
        self.adlabel.setText(QCoreApplication.translate("Form2", u"Ad:", None))
        self.ehliyetlabel.setText(QCoreApplication.translate("Form2", u"Ehliyet S\u0131n\u0131f\u0131:", None))
        self.egitimdurumulabel.setText(QCoreApplication.translate("Form2", u"E\u011fitim Durumu:", None))
        self.silButton.setText(QCoreApplication.translate("Form2", u"Sil", None))
        self.mesleklabel.setText(QCoreApplication.translate("Form2", u"Meslek:", None))
        self.araButton.setText(QCoreApplication.translate("Form2", u"Ara", None))
        self.dtarihilabel.setText(QCoreApplication.translate("Form2", u"Do\u011fum Tarihi:", None))
        self.telnolabel.setText(QCoreApplication.translate("Form2", u"Telefon No:", None))
        self.kapatButton.setText(QCoreApplication.translate("Form2", u"Kapat", None))
        self.menuMusteri_Bilgileri_Girisi.setTitle(QCoreApplication.translate("Form2", u"M\u00fcsteri Bilgileri Girisi", None))
    # retranslateUi

