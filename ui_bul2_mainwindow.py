# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bul2_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Bul2(object):
    def setupUi(self, Bul2):
        if not Bul2.objectName():
            Bul2.setObjectName(u"Bul2")
        Bul2.resize(488, 233)
        self.centralwidget = QWidget(Bul2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 3, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 2, 3, 1, 1)

        self.pushButtonBUL = QPushButton(self.centralwidget)
        self.pushButtonBUL.setObjectName(u"pushButtonBUL")

        self.gridLayout.addWidget(self.pushButtonBUL, 3, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        Bul2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Bul2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 488, 21))
        self.menuBul = QMenu(self.menubar)
        self.menuBul.setObjectName(u"menuBul")
        Bul2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Bul2)
        self.statusbar.setObjectName(u"statusbar")
        Bul2.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.pushButtonBUL)

        self.menubar.addAction(self.menuBul.menuAction())

        self.retranslateUi(Bul2)

        QMetaObject.connectSlotsByName(Bul2)
    # setupUi

    def retranslateUi(self, Bul2):
        Bul2.setWindowTitle(QCoreApplication.translate("Bul2", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Bul2", u"M\u00fc\u015fteri Ad\u0131:", None))
        self.label_4.setText(QCoreApplication.translate("Bul2", u"Ara\u00e7 Model:", None))
        self.label_2.setText(QCoreApplication.translate("Bul2", u"M\u00fc\u015fteri Soyad\u0131:", None))
        self.label_5.setText(QCoreApplication.translate("Bul2", u"Ka\u00e7 G\u00fcn Kiralanacak?:", None))
        self.label_3.setText(QCoreApplication.translate("Bul2", u"Ara\u00e7 Marka:", None))
        self.label_6.setText(QCoreApplication.translate("Bul2", u"Yolculuk Nereye?:", None))
        self.pushButtonBUL.setText(QCoreApplication.translate("Bul2", u"Bul", None))
        self.menuBul.setTitle(QCoreApplication.translate("Bul2", u"Bul", None))
    # retranslateUi

