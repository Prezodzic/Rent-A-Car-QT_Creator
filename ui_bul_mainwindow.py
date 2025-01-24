# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bul_mainwindow.ui'
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

class Ui_Bul(object):
    def setupUi(self, Bul):
        if not Bul.objectName():
            Bul.setObjectName(u"Bul")
        Bul.resize(382, 237)
        self.centralwidget = QWidget(Bul)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.adlabel2 = QLabel(self.centralwidget)
        self.adlabel2.setObjectName(u"adlabel2")

        self.gridLayout.addWidget(self.adlabel2, 0, 0, 1, 1)

        self.adlineEdit2 = QLineEdit(self.centralwidget)
        self.adlineEdit2.setObjectName(u"adlineEdit2")

        self.gridLayout.addWidget(self.adlineEdit2, 0, 1, 1, 1)

        self.telnolabel2 = QLabel(self.centralwidget)
        self.telnolabel2.setObjectName(u"telnolabel2")

        self.gridLayout.addWidget(self.telnolabel2, 0, 2, 1, 1)

        self.telnolineEdit2 = QLineEdit(self.centralwidget)
        self.telnolineEdit2.setObjectName(u"telnolineEdit2")

        self.gridLayout.addWidget(self.telnolineEdit2, 0, 3, 1, 1)

        self.soyadlabel3 = QLabel(self.centralwidget)
        self.soyadlabel3.setObjectName(u"soyadlabel3")

        self.gridLayout.addWidget(self.soyadlabel3, 1, 0, 1, 1)

        self.soyadlineEdit2 = QLineEdit(self.centralwidget)
        self.soyadlineEdit2.setObjectName(u"soyadlineEdit2")

        self.gridLayout.addWidget(self.soyadlineEdit2, 1, 1, 1, 1)

        self.mesleklabel2 = QLabel(self.centralwidget)
        self.mesleklabel2.setObjectName(u"mesleklabel2")

        self.gridLayout.addWidget(self.mesleklabel2, 1, 2, 1, 1)

        self.mesleklineEdit2 = QLineEdit(self.centralwidget)
        self.mesleklineEdit2.setObjectName(u"mesleklineEdit2")

        self.gridLayout.addWidget(self.mesleklineEdit2, 1, 3, 1, 1)

        self.tckimliklabel2 = QLabel(self.centralwidget)
        self.tckimliklabel2.setObjectName(u"tckimliklabel2")

        self.gridLayout.addWidget(self.tckimliklabel2, 2, 0, 1, 1)

        self.tckimliklineEdit2 = QLineEdit(self.centralwidget)
        self.tckimliklineEdit2.setObjectName(u"tckimliklineEdit2")

        self.gridLayout.addWidget(self.tckimliklineEdit2, 2, 1, 1, 1)

        self.ehliyetsinifilabel2 = QLabel(self.centralwidget)
        self.ehliyetsinifilabel2.setObjectName(u"ehliyetsinifilabel2")

        self.gridLayout.addWidget(self.ehliyetsinifilabel2, 2, 2, 1, 1)

        self.ehliyetsinifilineEdit2 = QLineEdit(self.centralwidget)
        self.ehliyetsinifilineEdit2.setObjectName(u"ehliyetsinifilineEdit2")

        self.gridLayout.addWidget(self.ehliyetsinifilineEdit2, 2, 3, 1, 1)

        self.dogumtarihilabel2 = QLabel(self.centralwidget)
        self.dogumtarihilabel2.setObjectName(u"dogumtarihilabel2")

        self.gridLayout.addWidget(self.dogumtarihilabel2, 3, 0, 1, 1)

        self.dogumtarihilineEdit2 = QLineEdit(self.centralwidget)
        self.dogumtarihilineEdit2.setObjectName(u"dogumtarihilineEdit2")

        self.gridLayout.addWidget(self.dogumtarihilineEdit2, 3, 1, 1, 1)

        self.medenidurumulabel2 = QLabel(self.centralwidget)
        self.medenidurumulabel2.setObjectName(u"medenidurumulabel2")

        self.gridLayout.addWidget(self.medenidurumulabel2, 3, 2, 1, 1)

        self.medenidurumulineEdit2 = QLineEdit(self.centralwidget)
        self.medenidurumulineEdit2.setObjectName(u"medenidurumulineEdit2")

        self.gridLayout.addWidget(self.medenidurumulineEdit2, 3, 3, 1, 1)

        self.adreslabel2 = QLabel(self.centralwidget)
        self.adreslabel2.setObjectName(u"adreslabel2")

        self.gridLayout.addWidget(self.adreslabel2, 4, 0, 1, 1)

        self.adreslineEdit2 = QLineEdit(self.centralwidget)
        self.adreslineEdit2.setObjectName(u"adreslineEdit2")

        self.gridLayout.addWidget(self.adreslineEdit2, 4, 1, 1, 1)

        self.egitimdurumulabel2 = QLabel(self.centralwidget)
        self.egitimdurumulabel2.setObjectName(u"egitimdurumulabel2")

        self.gridLayout.addWidget(self.egitimdurumulabel2, 4, 2, 1, 1)

        self.egitimdurumulineEdit2 = QLineEdit(self.centralwidget)
        self.egitimdurumulineEdit2.setObjectName(u"egitimdurumulineEdit2")

        self.gridLayout.addWidget(self.egitimdurumulineEdit2, 4, 3, 1, 1)

        self.bulButton = QPushButton(self.centralwidget)
        self.bulButton.setObjectName(u"bulButton")

        self.gridLayout.addWidget(self.bulButton, 5, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        Bul.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Bul)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 382, 21))
        self.menuAra = QMenu(self.menubar)
        self.menuAra.setObjectName(u"menuAra")
        Bul.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Bul)
        self.statusbar.setObjectName(u"statusbar")
        Bul.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.adlineEdit2, self.soyadlineEdit2)
        QWidget.setTabOrder(self.soyadlineEdit2, self.tckimliklineEdit2)
        QWidget.setTabOrder(self.tckimliklineEdit2, self.dogumtarihilineEdit2)
        QWidget.setTabOrder(self.dogumtarihilineEdit2, self.adreslineEdit2)
        QWidget.setTabOrder(self.adreslineEdit2, self.telnolineEdit2)
        QWidget.setTabOrder(self.telnolineEdit2, self.mesleklineEdit2)
        QWidget.setTabOrder(self.mesleklineEdit2, self.ehliyetsinifilineEdit2)
        QWidget.setTabOrder(self.ehliyetsinifilineEdit2, self.medenidurumulineEdit2)
        QWidget.setTabOrder(self.medenidurumulineEdit2, self.egitimdurumulineEdit2)
        QWidget.setTabOrder(self.egitimdurumulineEdit2, self.bulButton)

        self.menubar.addAction(self.menuAra.menuAction())

        self.retranslateUi(Bul)

        QMetaObject.connectSlotsByName(Bul)
    # setupUi

    def retranslateUi(self, Bul):
        Bul.setWindowTitle(QCoreApplication.translate("Bul", u"MainWindow", None))
        self.adlabel2.setText(QCoreApplication.translate("Bul", u"Ad:", None))
        self.telnolabel2.setText(QCoreApplication.translate("Bul", u"Telefon No:", None))
        self.soyadlabel3.setText(QCoreApplication.translate("Bul", u"Soyad:", None))
        self.mesleklabel2.setText(QCoreApplication.translate("Bul", u"Meslek:", None))
        self.tckimliklabel2.setText(QCoreApplication.translate("Bul", u"TC Kimlik No:", None))
        self.ehliyetsinifilabel2.setText(QCoreApplication.translate("Bul", u"Ehliyet S\u0131nf\u0131:", None))
        self.dogumtarihilabel2.setText(QCoreApplication.translate("Bul", u"Do\u011fum Tarihi:", None))
        self.medenidurumulabel2.setText(QCoreApplication.translate("Bul", u"Medeni Durumu:", None))
        self.adreslabel2.setText(QCoreApplication.translate("Bul", u"Adres:", None))
        self.egitimdurumulabel2.setText(QCoreApplication.translate("Bul", u"E\u011fitim Durumu:", None))
        self.bulButton.setText(QCoreApplication.translate("Bul", u"Bul", None))
        self.menuAra.setTitle(QCoreApplication.translate("Bul", u"Ara", None))
    # retranslateUi

