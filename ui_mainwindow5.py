# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow5.ui'
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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form5(object):
    def setupUi(self, Form5):
        if not Form5.objectName():
            Form5.setObjectName(u"Form5")
        Form5.resize(625, 340)
        self.centralwidget = QWidget(Form5)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.araclisteWidget = QTableWidget(self.centralwidget)
        self.araclisteWidget.setObjectName(u"araclisteWidget")

        self.gridLayout.addWidget(self.araclisteWidget, 1, 0, 1, 1)

        self.kapatbuton = QPushButton(self.centralwidget)
        self.kapatbuton.setObjectName(u"kapatbuton")

        self.gridLayout.addWidget(self.kapatbuton, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        Form5.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Form5)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 625, 21))
        self.menuArac_Kiralama_Bilgileri_Girisi = QMenu(self.menubar)
        self.menuArac_Kiralama_Bilgileri_Girisi.setObjectName(u"menuArac_Kiralama_Bilgileri_Girisi")
        Form5.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Form5)
        self.statusbar.setObjectName(u"statusbar")
        Form5.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArac_Kiralama_Bilgileri_Girisi.menuAction())

        self.retranslateUi(Form5)

        QMetaObject.connectSlotsByName(Form5)
    # setupUi

    def retranslateUi(self, Form5):
        Form5.setWindowTitle(QCoreApplication.translate("Form5", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Form5", u"G\u00fcncel Kirada Olan Ara\u00e7 Listesi", None))
        self.kapatbuton.setText(QCoreApplication.translate("Form5", u"Kapat", None))
        self.menuArac_Kiralama_Bilgileri_Girisi.setTitle(QCoreApplication.translate("Form5", u"Kirada Olan Arac Girisi", None))
    # retranslateUi

