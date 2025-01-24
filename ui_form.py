# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_anaPencere(object):
    def setupUi(self, anaPencere):
        if not anaPencere.objectName():
            anaPencere.setObjectName(u"anaPencere")
        anaPencere.resize(460, 231)
        self.centralwidget = QWidget(anaPencere)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.musteriGirisButton = QPushButton(self.centralwidget)
        self.musteriGirisButton.setObjectName(u"musteriGirisButton")

        self.gridLayout.addWidget(self.musteriGirisButton, 0, 0, 1, 1)

        self.aracbilgiGirisButton = QPushButton(self.centralwidget)
        self.aracbilgiGirisButton.setObjectName(u"aracbilgiGirisButton")

        self.gridLayout.addWidget(self.aracbilgiGirisButton, 1, 0, 1, 1)

        self.arackirabilgiButton = QPushButton(self.centralwidget)
        self.arackirabilgiButton.setObjectName(u"arackirabilgiButton")

        self.gridLayout.addWidget(self.arackirabilgiButton, 1, 1, 1, 1)

        self.araclistesiButton = QPushButton(self.centralwidget)
        self.araclistesiButton.setObjectName(u"araclistesiButton")

        self.gridLayout.addWidget(self.araclistesiButton, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.bilgiLabel = QLabel(self.centralwidget)
        self.bilgiLabel.setObjectName(u"bilgiLabel")
        self.bilgiLabel.setEnabled(True)
        self.bilgiLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.bilgiLabel, 0, 0, 1, 1)

        self.cikisButton = QPushButton(self.centralwidget)
        self.cikisButton.setObjectName(u"cikisButton")

        self.gridLayout_2.addWidget(self.cikisButton, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        anaPencere.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(anaPencere)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 21))
        self.menuAna_Menu = QMenu(self.menubar)
        self.menuAna_Menu.setObjectName(u"menuAna_Menu")
        anaPencere.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(anaPencere)
        self.statusbar.setObjectName(u"statusbar")
        anaPencere.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAna_Menu.menuAction())

        self.retranslateUi(anaPencere)

        QMetaObject.connectSlotsByName(anaPencere)
    # setupUi

    def retranslateUi(self, anaPencere):
        anaPencere.setWindowTitle(QCoreApplication.translate("anaPencere", u"anaPencere", None))
        self.musteriGirisButton.setText(QCoreApplication.translate("anaPencere", u"M\u00fc\u015fteri Bilgileri Giri\u015fi", None))
        self.aracbilgiGirisButton.setText(QCoreApplication.translate("anaPencere", u"Ara\u00e7 Bilgileri Giri\u015fi", None))
        self.arackirabilgiButton.setText(QCoreApplication.translate("anaPencere", u"Ara\u00e7 Kiralama Bilgileri Giri\u015fi", None))
        self.araclistesiButton.setText(QCoreApplication.translate("anaPencere", u"Kirada Olan Ara\u00e7lar\u0131n Giri\u015fi", None))
        self.bilgiLabel.setText(QCoreApplication.translate("anaPencere", u"Yapmak istedi\u011finiz i\u015fleme t\u0131klay\u0131n\u0131z.", None))
        self.cikisButton.setText(QCoreApplication.translate("anaPencere", u"\u00c7\u0131k\u0131\u015f", None))
        self.menuAna_Menu.setTitle(QCoreApplication.translate("anaPencere", u"Ana Menu", None))
    # retranslateUi

