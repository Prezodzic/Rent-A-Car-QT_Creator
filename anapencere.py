# This Python file uses the following encoding: utf-8
import sys
import mysql.connector

from datetime import datetime
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
# pyside6-uic form.ui -o ui_form.py, or
# pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_anaPencere
from ui_mainwindow2 import Ui_Form2
from ui_mainwindow3 import Ui_Form3
from ui_mainwindow4 import Ui_Form4
from ui_mainwindow5 import Ui_Form5
from ui_bul_mainwindow import Ui_Bul
from ui_bul2_mainwindow import Ui_Bul2
from ui_bul3_mainwindow import Ui_Bul3



class anaPencere(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaPencere()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        self.ui.musteriGirisButton.clicked.connect(self.musteriGirisButton)
        self.ui.araclistesiButton.clicked.connect(self.araclistesiButton)
        self.ui.aracbilgiGirisButton.clicked.connect(self.aracbilgiGirisButton)
        self.ui.arackirabilgiButton.clicked.connect(self.arackirabilgiButton)
        self.ui.cikisButton.clicked.connect(self.cikisButton)
                
        self.sqlBaglan()
        self.dbCheckAndCreateTables()

    def sqlBaglan(self):
        self.dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="deneme"
        )

    def dbCheckAndCreateTables(self):
        if self.dbConn.is_connected():
            self.mycursor = self.dbConn.cursor()
            self.target_db = "db90220000250"
        
        try:
            self.mycursor.execute(f"USE {self.target_db}")
        except mysql.connector.Error:
            self.mycursor.execute(f"CREATE DATABASE {self.target_db}")
            self.mycursor.execute(f"USE {self.target_db}")

        tables = {
            "musteri_bilgileri_girisi": """
                CREATE TABLE IF NOT EXISTS `musteri_bilgileri_girisi` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `Ad` VARCHAR(45) NOT NULL,
                    `Soyad` VARCHAR(45) NOT NULL,
                    `TC_Kimlik_No` VARCHAR(11) NOT NULL,
                    `Dogum_Tarihi` DATE NOT NULL,
                    `Adres` VARCHAR(45) NOT NULL,
                    `Telefon_No` VARCHAR(11) NOT NULL,
                    `Meslek` VARCHAR(45) NOT NULL,
                    `Ehliyet_Sinifi` VARCHAR(45) NOT NULL,
                    `Medeni_Durumu` VARCHAR(45) NOT NULL,
                    `Egitim_Durumu` VARCHAR(45) NOT NULL
                );
            """,
            "arac_kiralama_bilgileri_girisi": """
                CREATE TABLE IF NOT EXISTS `arac_kiralama_bilgileri_girisi` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `Müşteri Adı` VARCHAR(45) NOT NULL,
                    `Müşteri Soyadı` VARCHAR(45) NOT NULL,
                    `Araç Marka` VARCHAR(45) NOT NULL,
                    `Araç Model` VARCHAR(45) NOT NULL,
                    `Kaç Gün Kiralanacak?` VARCHAR(45) NOT NULL,
                    `Yolculuk Nereye?` VARCHAR(45) NOT NULL
                );
            """,
            "arac_bilgileri_girisi": """
                CREATE TABLE IF NOT EXISTS `arac_bilgileri_girisi` (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `Araç Türü` VARCHAR(45) NOT NULL,
                    `Marka` VARCHAR(45) NOT NULL,
                    `Model` VARCHAR(45) NOT NULL,
                    `Üretim Yılı` VARCHAR(45) NOT NULL,
                    `Yakıt Türü` VARCHAR(45) NOT NULL,
                    `Vites` VARCHAR(45) NOT NULL,
                    `Motor Gücü` VARCHAR(45) NOT NULL,
                    `Kasa Tipi` VARCHAR(45) NOT NULL,
                    `Motor Hacmi` VARCHAR(45) NOT NULL,
                    `Çekiş` VARCHAR(45) NOT NULL,
                    `Kapı` VARCHAR(45) NOT NULL,
                    `Renk` VARCHAR(45) NOT NULL,
                    `Motor No` VARCHAR(45) NOT NULL,
                    `Şasi No` VARCHAR(45) NOT NULL,
                    `Günlük Kiralama Bedeli` VARCHAR(45) NOT NULL,
                    `Kirada Mı?` VARCHAR(45) NOT NULL,
                    `Kullanım Dışı Mı?` VARCHAR(45) NOT NULL
                );
            """
        }

        for table_name, create_query in tables.items():
            self.mycursor.execute(create_query)

    def musteriGirisButton(self):
        self.w = ikinciPencere(self)
        self.w.show()

    def araclistesiButton(self):
        self.w = ucuncuPencere(self)
        self.w.show()

    def aracbilgiGirisButton(self):
        self.w = dorduncuPencere(self)
        self.w.show()

    def arackirabilgiButton(self):
        self.w = besinciPencere(self)
        self.w.show()

    def cikisButton(self):
        self.close()

    def closeEvent(self, event):
        self.mycursor.close()
        self.dbConn.close()
        
        

class ikinciPencere(QMainWindow):
    def __init__(self, deger):
        super().__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger
       
        self.ui.kapatButton.clicked.connect(self.kapatButton)
        self.ui.yeniButton.clicked.connect(self.yeniButton)
        self.ui.guncelleButton.clicked.connect(self.guncelleButton)
        self.ui.kaydetButton.clicked.connect(self.kaydetButton)
        self.ui.silButton.clicked.connect(self.silButton)
        self.ui.araButton.clicked.connect(self.araButton)

        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setRowCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["id", "Ad", "Soyad", "TC_Kimlik_No", "Dogum_Tarihi", "Adres", "Telefon_No", "Meslek", "Ehliyet_Sinifi", "Medeni_Durumu", "Egitim_Durumu"]
        )
        for i in range(11):
            self.ui.tableWidget.setColumnWidth(0, 10)
            self.ui.tableWidget.setColumnWidth(1, 50)
            self.ui.tableWidget.setColumnWidth(2, 50)
            self.ui.tableWidget.setColumnWidth(3, 100)
            self.ui.tableWidget.setColumnWidth(4, 100)
            self.ui.tableWidget.setColumnWidth(5, 150)
            self.ui.tableWidget.setColumnWidth(6, 100)
            self.ui.tableWidget.setColumnWidth(7, 100)
            self.ui.tableWidget.setColumnWidth(8, 100)
            self.ui.tableWidget.setColumnWidth(9, 100)
            self.ui.tableWidget.setColumnWidth(10, 100)
        self.ui.tableWidget.cellDoubleClicked.connect(self.cellDoubleClicked)
        self.ui.tableWidget.cellChanged.connect(self.cellChanged)
        
    def showEvent(self, event):
        self.loadIkinciPencereData()
        super().showEvent(event)

    def loadIkinciPencereData(self):
        query = "SELECT * FROM musteri_bilgileri_girisi"
        self.loadDataIntoTableWidget(self.ui.tableWidget, query)

    def loadDataIntoTableWidget(self, tableWidget, query):
        self.dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="deneme",
            database="db90220000250"
        )
        cursor = self.dbConn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        tableWidget.setRowCount(len(rows))
        for rowIndex, row in enumerate(rows):
            for colIndex, data in enumerate(row):
                tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(data)))
        
        cursor.close()
        self.dbConn.close()

    def yeniButton(self):
        self.ui.idlineEdit.clear()
        self.ui.adlineEdit.clear()
        self.ui.soyadlineEdit.clear()
        self.ui.tckimliklineEdit.clear()
        self.ui.dtarihilineEdit.clear()
        self.ui.adreslineEdit.clear()
        self.ui.telnolineEdit.clear()
        self.ui.mesleklineEdit.clear()
        self.ui.ehliyetlineEdit.clear()
        self.ui.medenidurumulineEdit.clear()
        self.ui.egitimdurumulineEdit.clear()
        self.ui.silButton.setEnabled(False)
        self.ui.guncelleButton.setEnabled(False)

    def guncelleButton(self):
        id = self.ui.idlineEdit.text()
        Ad = self.ui.adlineEdit.text()
        Soyad = self.ui.soyadlineEdit.text()
        TC_Kimlik_No = self.ui.tckimliklineEdit.text()
        Dogum_Tarihi = self.ui.dtarihilineEdit.text()
        Adres = self.ui.adreslineEdit.text()
        Telefon_No = self.ui.telnolineEdit.text()
        Meslek = self.ui.mesleklineEdit.text()
        Ehliyet_Sinifi = self.ui.ehliyetlineEdit.text()
        Medeni_Durumu = self.ui.medenidurumulineEdit.text()
        Egitim_Durumu = self.ui.egitimdurumulineEdit.text()

        self.deger.mycursor.execute(f"""
            UPDATE `{self.deger.target_db}`.`musteri_bilgileri_girisi` 
            SET `Ad` = %s, `Soyad` = %s, `TC_Kimlik_No` = %s, `Dogum_Tarihi` = %s, `Adres` = %s, `Telefon_No` = %s, `Meslek` = %s, `Ehliyet_Sinifi` = %s, `Medeni_Durumu` = %s, `Egitim_Durumu` = %s 
            WHERE `id` = %s
        """, (Ad, Soyad, TC_Kimlik_No, Dogum_Tarihi, Adres, Telefon_No, Meslek, Ehliyet_Sinifi, Medeni_Durumu, Egitim_Durumu, id))
    
        self.deger.dbConn.commit()
        QMessageBox.information(self, "Başarılı", "Güncelleme işlemi başarılı.")
        self.ui.guncelleButton.setEnabled(False)
        
        # Tabloyu güncelle
        currentRow = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.setItem(currentRow, 1, QTableWidgetItem(Ad))
        self.ui.tableWidget.setItem(currentRow, 2, QTableWidgetItem(Soyad))
        self.ui.tableWidget.setItem(currentRow, 3, QTableWidgetItem(TC_Kimlik_No))
        self.ui.tableWidget.setItem(currentRow, 4, QTableWidgetItem(Dogum_Tarihi))
        self.ui.tableWidget.setItem(currentRow, 5, QTableWidgetItem(Adres))
        self.ui.tableWidget.setItem(currentRow, 6, QTableWidgetItem(Telefon_No))
        self.ui.tableWidget.setItem(currentRow, 7, QTableWidgetItem(Meslek))
        self.ui.tableWidget.setItem(currentRow, 8, QTableWidgetItem(Ehliyet_Sinifi))
        self.ui.tableWidget.setItem(currentRow, 9, QTableWidgetItem(Medeni_Durumu))
        self.ui.tableWidget.setItem(currentRow, 10, QTableWidgetItem(Egitim_Durumu))
            
    def kaydetButton(self):
        if self.ui.idlineEdit.text() != "":
            result = self.mesaj("Bu kayıt mevcut. Güncelleme yapmak istediğinize emin misiniz?")
            if result == QMessageBox.Yes:
                self.guncelleButton()
            else:
                QMessageBox.information(self, "İptal", "Güncelleme işlemi iptal edildi.")
        else:
            # Mevcut satır sayısına göre yeni id belirle
            rowCount = self.ui.tableWidget.rowCount()
            new_id = rowCount + 1
    
            self.sql = """
                INSERT INTO `musteri_bilgileri_girisi` 
                (`id`, `Ad`, `Soyad`, `TC_Kimlik_No`, `Dogum_Tarihi`, `Adres`, `Telefon_No`, `Meslek`, `Ehliyet_Sinifi`, `Medeni_Durumu`, `Egitim_Durumu`) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.veri = (
                new_id,
                self.ui.adlineEdit.text(), 
                self.ui.soyadlineEdit.text(), 
                self.ui.tckimliklineEdit.text(), 
                self.ui.dtarihilineEdit.text(), 
                self.ui.adreslineEdit.text(), 
                self.ui.telnolineEdit.text(), 
                self.ui.mesleklineEdit.text(), 
                self.ui.ehliyetlineEdit.text(), 
                self.ui.medenidurumulineEdit.text(), 
                self.ui.egitimdurumulineEdit.text()
            )
            self.deger.mycursor.execute(self.sql, self.veri)
            self.deger.dbConn.commit()
            QMessageBox.information(self, "Başarılı", "Kayıt işlemi başarılı.")   
            
            # Yeni eklenen veriyi tabloya ekle
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(new_id)))
            self.ui.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(self.ui.adlineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(self.ui.soyadlineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(self.ui.tckimliklineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(self.ui.dtarihilineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(self.ui.adreslineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(self.ui.telnolineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 7, QTableWidgetItem(self.ui.mesleklineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 8, QTableWidgetItem(self.ui.ehliyetlineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 9, QTableWidgetItem(self.ui.medenidurumulineEdit.text()))
            self.ui.tableWidget.setItem(rowPosition, 10, QTableWidgetItem(self.ui.egitimdurumulineEdit.text()))
    
            # Form alanlarını temizle
            self.ui.idlineEdit.clear()
            self.ui.adlineEdit.clear()
            self.ui.soyadlineEdit.clear()
            self.ui.tckimliklineEdit.clear()
            self.ui.dtarihilineEdit.clear()
            self.ui.adreslineEdit.clear()
            self.ui.telnolineEdit.clear()
            self.ui.mesleklineEdit.clear()
            self.ui.ehliyetlineEdit.clear()
            self.ui.medenidurumulineEdit.clear()
            self.ui.egitimdurumulineEdit.clear()    
            
    def silButton(self):
        result = self.mesaj("Seçili kaydı silmek istediğinize emin misiniz?")
        if result == QMessageBox.Yes:
            id = int(self.ui.idlineEdit.text())
            self.deger.mycursor.execute(f"DELETE FROM `db90220000250`.`musteri_bilgileri_girisi` WHERE `id` = {id};")
            self.deger.dbConn.commit()
        
            # Tablodan ilgili satırı kaldır
            currentRow = self.ui.tableWidget.currentRow()
            self.ui.tableWidget.removeRow(currentRow)
        
            self.ui.silButton.setEnabled(False)
            QMessageBox.information(self, "Başarılı", "Silme işlemi başarılı.")
        else:
            QMessageBox.information(self, "İptal", "Silme işlemi iptal edildi.")

    def araButton(self):
        self.bulPencere = Bul(self.deger, self)
        self.bulPencere.show()
        
    def tableDoldur(self):
        araTable = [arama for arama in self.deger.mycursor.fetchall()]
        self.ui.tableWidget.setRowCount(len(araTable))
        if(araTable!=[]):
            for x in range(len(araTable)):
                item_id = QTableWidgetItem(str(araTable[x][0]))
                item_ad = QTableWidgetItem(str(araTable[x][1]))
                item_soyad = QTableWidgetItem(str(araTable[x][2]))
                item_tckimlik = QTableWidgetItem(str(araTable[x][3]))
                item_dtarih = QTableWidgetItem(str(araTable[x][4]))
                item_adres = QTableWidgetItem(str(araTable[x][5]))
                item_telno = QTableWidgetItem(str(araTable[x][6]))
                item_meslek = QTableWidgetItem(str(araTable[x][7]))
                item_ehliyet = QTableWidgetItem(str(araTable[x][8]))
                item_medenidurumu = QTableWidgetItem(str(araTable[x][9]))
                item_egitimdurumu = QTableWidgetItem(str(araTable[x][10]))
                self.ui.tableWidget.setItem(x,0,item_id)
                self.ui.tableWidget.setItem(x,1,item_ad)
                self.ui.tableWidget.setItem(x,2,item_soyad)
                self.ui.tableWidget.setItem(x,3,item_tckimlik)
                self.ui.tableWidget.setItem(x,4,item_dtarih)
                self.ui.tableWidget.setItem(x,5,item_adres)
                self.ui.tableWidget.setItem(x,6,item_telno)
                self.ui.tableWidget.setItem(x,7,item_meslek)
                self.ui.tableWidget.setItem(x,8,item_ehliyet)
                self.ui.tableWidget.setItem(x,9,item_medenidurumu)
                self.ui.tableWidget.setItem(x,10,item_egitimdurumu)
        QMessageBox.information(f"{len(araTable)} Kayıt bulundu.")

    def kapatButton(self):
        self.close()

    def cellDoubleClicked(self):
        self.ui.silButton.setEnabled(True)
        self.ui.guncelleButton.setEnabled(True)
        rowSec=int(self.ui.tableWidget.currentRow())
        if(rowSec>=0):
            self.ui.idlineEdit.setText(str(self.ui.tableWidget.item(rowSec,0).text()))
            self.ui.adlineEdit.setText(str(self.ui.tableWidget.item(rowSec,1).text()))
            self.ui.soyadlineEdit.setText(str(self.ui.tableWidget.item(rowSec,2).text()))
            self.ui.tckimliklineEdit.setText(str(self.ui.tableWidget.item(rowSec,3).text()))
            self.ui.dtarihilineEdit.setText(str(self.ui.tableWidget.item(rowSec,4).text()))
            self.ui.adreslineEdit.setText(str(self.ui.tableWidget.item(rowSec,5).text()))
            self.ui.telnolineEdit.setText(str(self.ui.tableWidget.item(rowSec,6).text()))
            self.ui.mesleklineEdit.setText(str(self.ui.tableWidget.item(rowSec,7).text()))
            self.ui.ehliyetlineEdit.setText(str(self.ui.tableWidget.item(rowSec,8).text()))
            self.ui.medenidurumulineEdit.setText(str(self.ui.tableWidget.item(rowSec,9).text()))
            self.ui.egitimdurumulineEdit.setText(str(self.ui.tableWidget.item(rowSec,10).text()))           

    def cellChanged(self):
        rowSec=int(self.ui.tableWidget.currentRow())
        if(rowSec>=0):
            self.ui.idlineEdit.setText(str(self.ui.tableWidget.item(rowSec,0).text()))
            self.ui.adlineEdit.setText(str(self.ui.tableWidget.item(rowSec,1).text()))
            self.ui.soyadlineEdit.setText(str(self.ui.tableWidget.item(rowSec,2).text()))
            self.ui.tckimliklineEdit.setText(str(self.ui.tableWidget.item(rowSec,3).text()))
            self.ui.dtarihilineEdit.setText(str(self.ui.tableWidget.item(rowSec,4).text()))
            self.ui.adreslineEdit.setText(str(self.ui.tableWidget.item(rowSec,5).text()))
            self.ui.telnolineEdit.setText(str(self.ui.tableWidget.item(rowSec,6).text()))
            self.ui.mesleklineEdit.setText(str(self.ui.tableWidget.item(rowSec,7).text()))
            self.ui.ehliyetlineEdit.setText(str(self.ui.tableWidget.item(rowSec,8).text()))
            self.ui.medenidurumulineEdit.setText(str(self.ui.tableWidget.item(rowSec,9).text()))
            self.ui.egitimdurumulineEdit.setText(str(self.ui.tableWidget.item(rowSec,10).text())) 
            self.ui.guncelleButton.setEnabled(True)

    def mesaj(self, metin):
        self.message_box = QMessageBox()
        self.message_box.setText(metin)
        self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.message_box.setDefaultButton(QMessageBox.No)
        return(self.message_box.exec())

        

class besinciPencere(QMainWindow):
    def __init__(self, deger):
        super().__init__()
        self.ui = Ui_Form3()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger
        
        self.ui.yeni_pushButton.clicked.connect(self.yeni_pushButton)
        self.ui.guncelle_pushButton.clicked.connect(self.guncelle_pushButton)
        self.ui.kaydet_pushButton.clicked.connect(self.kaydet_pushButton)
        self.ui.kapat_pushButton.clicked.connect(self.kapat_pushButton) 
        self.ui.sil_pushButton.clicked.connect(self.sil_pushButton)
        self.ui.arabtn.clicked.connect(self.arabtn)
        
        self.date_widget = self.ui.tarih_lcdNumber
        self.time_widget = self.ui.saat_lcdNumber
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_datetime)
        
        interval = 1000  
        self.timer.start(interval)
        
        self.ui.akbg_tableWidget.setColumnCount(7)
        self.ui.akbg_tableWidget.setRowCount(11)
        self.ui.akbg_tableWidget.setHorizontalHeaderLabels(["id", "Müşteri Adı", "Müşteri Soyadı", "Araç Marka", "Araç Model", "Kaç Gün Kiralanacak?", "Yolculuk Nereye?"])
        for i in range(11):
            self.ui.akbg_tableWidget.setColumnWidth(0, 10)
            self.ui.akbg_tableWidget.setColumnWidth(1, 100)
            self.ui.akbg_tableWidget.setColumnWidth(2, 100)
            self.ui.akbg_tableWidget.setColumnWidth(3, 100)
            self.ui.akbg_tableWidget.setColumnWidth(4, 100)
            self.ui.akbg_tableWidget.setColumnWidth(5, 150)
            self.ui.akbg_tableWidget.setColumnWidth(6, 150)
        self.ui.akbg_tableWidget.cellDoubleClicked.connect(self.cellDoubleClicked)
        self.ui.akbg_tableWidget.cellChanged.connect(self.cellChanged)
        
        self.musteriadi_comboBox()
        self.musterisoyadi_comboBox()
        self.aracmarka_comboBox()
        self.aracmodel_comboBox()
            
    def showEvent(self, event):
        self.loadBesinciPencereData()
        super().showEvent(event)
        
    def loadBesinciPencereData(self):
        query = "SELECT * FROM arac_kiralama_bilgileri_girisi"
        self.loadDataIntoTableWidget(self.ui.akbg_tableWidget, query)

    def loadDataIntoTableWidget(self, tableWidget, query):
        self.dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="deneme",
            database="db90220000250"
        )
        cursor = self.dbConn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        tableWidget.setRowCount(len(rows))
        for rowIndex, row in enumerate(rows):
            for colIndex, data in enumerate(row):
                tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(data)))
        
        cursor.close()
        self.dbConn.close()

    def musteriadi_comboBox(self):
        query = "SELECT `Ad` FROM `musteri_bilgileri_girisi`"
        self.deger.mycursor.execute(query)
        
        self.ui.musteriadi_comboBox.clear()  
        
        for (ad,) in self.deger.mycursor:
            self.ui.musteriadi_comboBox.addItem(ad)
            
    def musterisoyadi_comboBox(self):
        query = "SELECT `Soyad` FROM `musteri_bilgileri_girisi`"
        self.deger.mycursor.execute(query)
        
        self.ui.musterisoyadi_comboBox.clear()  
        
        for (soyad,) in self.deger.mycursor:
            self.ui.musterisoyadi_comboBox.addItem(soyad)
    
    def aracmarka_comboBox(self):
        query = "SELECT `Marka` FROM `arac_bilgileri_girisi` WHERE `Kirada mı?` = '1' AND `Kullanım Dışı Mı?` = '0'"
        self.deger.mycursor.execute(query)
        
        self.ui.aracmarka_comboBox.clear()  
        
        for (marka,) in self.deger.mycursor:
            self.ui.aracmarka_comboBox.addItem(marka)
    
    def aracmodel_comboBox(self):
        query = "SELECT `Model` FROM `arac_bilgileri_girisi` WHERE `Kirada mı?` = '1' AND `Kullanım Dışı Mı?` = '0'"
        self.deger.mycursor.execute(query)
        
        self.ui.aracmodel_comboBox.clear()  
        
        for (model,) in self.deger.mycursor:
            self.ui.aracmodel_comboBox.addItem(model)    
        
    def update_datetime(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M")
        self.date_widget.display(current_date)
        self.time_widget.display(current_time)
     
    def yeni_pushButton(self):
        self.ui.sil_pushButton.setEnabled(False)
        self.ui.guncelle_pushButton.setEnabled(False)
        self.ui.id_lineEdit.clear()
        self.ui.kacgunkiralanacak_lineEdit.clear()
        self.ui.yolculuknereye_lineEdit.clear()
            
    def guncelle_pushButton(self):
        id = self.ui.id_lineEdit.text()
        Musteri_Adi = self.ui.musteriadi_comboBox.currentText()
        Musteri_Soyadı = self.ui.musterisoyadi_comboBox.currentText()
        Araç_Marka = self.ui.aracmarka_comboBox.currentText()
        Araç_Model = self.ui.aracmodel_comboBox.currentText()
        Kaç_Gün_Kiralanacak = self.ui.kacgunkiralanacak_lineEdit.text()
        Yolculuk_Nereye = self.ui.yolculuknereye_lineEdit.text()
    
        self.deger.mycursor.execute("""
            UPDATE `db90220000250`.`arac_kiralama_bilgileri_girisi` 
            SET `Müşteri Adı` = %s, `Müşteri Soyadı` = %s, `Araç Marka` = %s, `Araç Model` = %s, `Kaç Gün Kiralanacak?` = %s, `Yolculuk Nereye?` = %s
            WHERE `id` = %s
        """, (Musteri_Adi, Musteri_Soyadı, Araç_Marka, Araç_Model, Kaç_Gün_Kiralanacak, Yolculuk_Nereye, id))
    
        self.deger.dbConn.commit()
        QMessageBox.information(self, "Başarılı", "Güncelleme işlemi başarılı.")
        self.ui.guncelle_pushButton.setEnabled(False)
    
        currentRow = self.ui.akbg_tableWidget.currentRow()
        self.ui.akbg_tableWidget.setItem(currentRow, 0, QTableWidgetItem(id))
        self.ui.akbg_tableWidget.setItem(currentRow, 1, QTableWidgetItem(Musteri_Adi))
        self.ui.akbg_tableWidget.setItem(currentRow, 2, QTableWidgetItem(Musteri_Soyadı))
        self.ui.akbg_tableWidget.setItem(currentRow, 3, QTableWidgetItem(Araç_Marka))
        self.ui.akbg_tableWidget.setItem(currentRow, 4, QTableWidgetItem(Araç_Model))
        self.ui.akbg_tableWidget.setItem(currentRow, 5, QTableWidgetItem(Kaç_Gün_Kiralanacak))
        self.ui.akbg_tableWidget.setItem(currentRow, 6, QTableWidgetItem(Yolculuk_Nereye))
        
    def kaydet_pushButton(self):
        if self.ui.id_lineEdit.text() != "":
            result = self.mesaj("Bu kayıt mevcut. Güncelleme yapmak istediğinize emin misiniz?")
            if result == QMessageBox.Yes:
                self.guncelle_pushButton()
            else:
                QMessageBox.information(self, "İptal", "Güncelleme işlemi iptal edildi.")
        else:
            self.deger.mycursor.execute("SELECT MAX(id) FROM `arac_kiralama_bilgileri_girisi`")
            max_id = self.deger.mycursor.fetchone()[0]
            if max_id is None:
                new_id = 1
            else:
                new_id = max_id + 1
    
            self.sql = """
                INSERT INTO `arac_kiralama_bilgileri_girisi` 
                (`id`, `Müşteri Adı`, `Müşteri Soyadı`, `Araç Marka`, `Araç Model`, `Kaç Gün Kiralanacak?`, `Yolculuk Nereye?`) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.veri = (
                new_id,
                self.ui.musteriadi_comboBox.currentText(), 
                self.ui.musterisoyadi_comboBox.currentText(),
                self.ui.aracmarka_comboBox.currentText(),
                self.ui.aracmodel_comboBox.currentText(),
                self.ui.kacgunkiralanacak_lineEdit.text(),
                self.ui.yolculuknereye_lineEdit.text()
            )
            self.deger.mycursor.execute(self.sql, self.veri)
            self.deger.dbConn.commit()
            QMessageBox.information(self, "Başarılı", "Kayıt işlemi başarılı.")   
            
            rowPosition = self.ui.akbg_tableWidget.rowCount()
            self.ui.akbg_tableWidget.insertRow(rowPosition)
            self.ui.akbg_tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(new_id)))
            self.ui.akbg_tableWidget.setItem(rowPosition, 1, QTableWidgetItem(self.ui.id_lineEdit.text()))
            self.ui.akbg_tableWidget.setItem(rowPosition, 2, QTableWidgetItem(self.ui.musteriadi_comboBox.currentText()))
            self.ui.akbg_tableWidget.setItem(rowPosition, 3, QTableWidgetItem(self.ui.musterisoyadi_comboBox.currentText()))
            self.ui.akbg_tableWidget.setItem(rowPosition, 4, QTableWidgetItem(self.ui.aracmarka_comboBox.currentText()))
            self.ui.akbg_tableWidget.setItem(rowPosition, 5, QTableWidgetItem(self.ui.aracmodel_comboBox.currentText()))
            self.ui.akbg_tableWidget.setItem(rowPosition, 6, QTableWidgetItem(self.ui.kacgunkiralanacak_lineEdit.text()))
            self.ui.akbg_tableWidget.setItem(rowPosition, 7, QTableWidgetItem(self.ui.yolculuknereye_lineEdit.text()))
             
            self.ui.id_lineEdit.clear()
            self.ui.kacgunkiralanacak_lineEdit.clear()
            self.ui.yolculuknereye_lineEdit.clear()
                                       
    def kapat_pushButton(self):
        self.close()
        
    def sil_pushButton(self):
        result = self.mesaj("Seçili kaydı silmek istediğinize emin misiniz?")
        if result == QMessageBox.Yes:
            id = int(self.ui.id_lineEdit.text())
            self.deger.mycursor.execute(f"DELETE FROM `db90220000250`.`arac_kiralama_bilgileri_girisi` WHERE `id` = {id};")
            self.deger.dbConn.commit()
        
            currentRow = self.ui.akbg_tableWidget.currentRow()
            self.ui.akbg_tableWidget.removeRow(currentRow)
        
            self.ui.sil_pushButton.setEnabled(False)
            QMessageBox.information(self, "Başarılı", "Silme işlemi başarılı.")
            
            self.ui.id_lineEdit.clear()
            self.ui.musteriadi_comboBox.clear()
            self.ui.musterisoyadi_comboBox.clear()
            self.ui.aracmarka_comboBox.clear()
            self.ui.aracmodel_comboBox.clear()
            self.ui.kacgunkiralanacak_lineEdit.clear()
            self.ui.yolculuknereye_lineEdit.clear()
           
        else:
            QMessageBox.information(self, "İptal", "Silme işlemi iptal edildi.")
            
    def cellDoubleClicked(self):
        self.ui.guncelle_pushButton.setEnabled(True)
        self.ui.sil_pushButton.setEnabled(True)
        rowSec=int(self.ui.akbg_tableWidget.currentRow())
        if(rowSec>=0):
            self.ui.id_lineEdit.setText(str(self.ui.akbg_tableWidget.item(rowSec,0).text()))
            self.ui.musteriadi_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,1).text()))
            self.ui.musterisoyadi_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,2).text()))
            self.ui.aracmarka_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,3).text()))
            self.ui.aracmodel_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,4).text()))
            self.ui.kacgunkiralanacak_lineEdit.setText(str(self.ui.akbg_tableWidget.item(rowSec,5).text()))
            self.ui.yolculuknereye_lineEdit.setText(str(self.ui.akbg_tableWidget.item(rowSec,6).text()))
            
    def cellChanged(self):
        rowSec=int(self.ui.akbg_tableWidget.currentRow())
        if(rowSec>=0):
            self.ui.id_lineEdit.setText(str(self.ui.akbg_tableWidget.item(rowSec,0).text()))
            self.ui.musteriadi_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,1).text()))
            self.ui.musterisoyadi_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,2).text()))
            self.ui.aracmarka_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,3).text()))
            self.ui.aracmodel_comboBox.setCurrentText(str(self.ui.akbg_tableWidget.item(rowSec,4).text()))
            self.ui.kacgunkiralanacak_lineEdit.setText(str(self.ui.akbg_tableWidget.item(rowSec,5).text()))
            self.ui.yolculuknereye_lineEdit.setText(str(self.ui.akbg_tableWidget.item(rowSec,6).text()))
            self.ui.guncelle_pushButton.setEnabled(True)
            
    def arabtn(self):
        self.bulPencere = Bul2(self.deger, self)
        self.bulPencere.show()
                   
    def mesaj(self, metin):
        self.message_box = QMessageBox()
        self.message_box.setText(metin)
        self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.message_box.setDefaultButton(QMessageBox.No)
        return self.message_box.exec()
    
       
   
class dorduncuPencere(QMainWindow):
    def __init__(self, deger):
        super().__init__()
        self.ui = Ui_Form4()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger

        self.ui.pushButton_yeni.clicked.connect(self.pushButton_yeni)
        self.ui.pushButton_guncelle.clicked.connect(self.pushButton_guncelle)
        self.ui.pushButton_kaydet.clicked.connect(self.pushButton_kaydet)
        self.ui.pushButton_sil.clicked.connect(self.pushButton_sil)
        self.ui.pushButton_ara.clicked.connect(self.pushButton_ara)
        self.ui.pushButton_kapat.clicked.connect(self.pushButton_kapat)
        
        self.ui.tableWidget_2.cellDoubleClicked.connect(self.cellDoubleClicked)
        self.ui.tableWidget_2.cellChanged.connect(self.cellChanged)
        
        self.ui.tableWidget_2.setColumnCount(18)
        self.ui.tableWidget_2.setRowCount(11)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(
            ["id", "Araç Türü", "Marka", "Model", "Üretim Yılı", "Yakıt Türü", "Vites", "Motor Gücü", "Kasa Tipi", "Motor Hacmi", "Çekiş", "Kapı", "Renk", "Motor No", "Şasi No", "Günlük Kiralama Bedeli", "Kirada Mı?", "Kullanım Dışı Mı?"]
        )
        for i in range(11):
            self.ui.tableWidget_2.setColumnWidth(0, 10)
            self.ui.tableWidget_2.setColumnWidth(1, 85)
            self.ui.tableWidget_2.setColumnWidth(2, 100)
            self.ui.tableWidget_2.setColumnWidth(3, 100)
            self.ui.tableWidget_2.setColumnWidth(4, 75)
            self.ui.tableWidget_2.setColumnWidth(5, 75)
            self.ui.tableWidget_2.setColumnWidth(6, 50)
            self.ui.tableWidget_2.setColumnWidth(7, 100)
            self.ui.tableWidget_2.setColumnWidth(8, 100)
            self.ui.tableWidget_2.setColumnWidth(9, 100)
            self.ui.tableWidget_2.setColumnWidth(10, 100)
            self.ui.tableWidget_2.setColumnWidth(11, 100)
            self.ui.tableWidget_2.setColumnWidth(12, 100)
            self.ui.tableWidget_2.setColumnWidth(13, 150)
            self.ui.tableWidget_2.setColumnWidth(14, 150)
            self.ui.tableWidget_2.setColumnWidth(15, 100)
            self.ui.tableWidget_2.setColumnWidth(16, 100)
            self.ui.tableWidget_2.setColumnWidth(17, 100)
            self.ui.tableWidget_2.setColumnWidth(18, 100)
            
    def showEvent(self, event):
        self.loadDorduncuPencereData()
        super().showEvent(event)

    def loadDorduncuPencereData(self):
        query = "SELECT * FROM arac_bilgileri_girisi"
        self.loadDataIntoTableWidget(self.ui.tableWidget_2, query)

    def loadDataIntoTableWidget(self, tableWidget, query):
        self.dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="deneme",
            database="db90220000250"
        )
        cursor = self.dbConn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        tableWidget.setRowCount(len(rows))
        for rowIndex, row in enumerate(rows):
            for colIndex, data in enumerate(row):
                tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(data)))
        
        cursor.close()
        self.dbConn.close()

    def pushButton_yeni(self):
        self.ui.pushButton_sil.setEnabled(False)
        self.ui.pushButton_guncelle.setEnabled(False)
        self.ui.lineEdit_id.clear()
        self.ui.lineEdit_aracturu.clear()   
        self.ui.lineEdit_marka.clear()
        self.ui.lineEdit_model.clear()
        self.ui.lineEdit_uretimyili.clear()
        self.ui.lineEdit_yakitturu.clear()
        self.ui.lineEdit_vites.clear()
        self.ui.lineEdit_motorgucu.clear()
        self.ui.lineEdit_kasatipi.clear()
        self.ui.lineEdit_motorhacmi.clear()
        self.ui.lineEdit_cekis.clear()
        self.ui.lineEdit_kapi.clear()
        self.ui.lineEdit_renk.clear()
        self.ui.lineEdit_motorno.clear()
        self.ui.lineEdit_sasino.clear()
        self.ui.lineEdit_gunlukkira.clear()
        self.ui.checkBox_kiradami.setChecked(False)
        self.ui.checkBox_kullanimdisimi.setChecked(False)
    
    def pushButton_guncelle(self):
        id = self.ui.lineEdit_id.text()
        Araç_Türü = self.ui.lineEdit_aracturu.text()
        Marka = self.ui.lineEdit_marka.text()
        Model = self.ui.lineEdit_model.text()
        Üretim_Yılı = self.ui.lineEdit_uretimyili.text()
        Yakıt_Türü = self.ui.lineEdit_yakitturu.text()
        Vites = self.ui.lineEdit_vites.text()
        Motor_Gücü = self.ui.lineEdit_motorgucu.text()
        Kasa_Tipi = self.ui.lineEdit_kasatipi.text()
        Motor_Hacmi = self.ui.lineEdit_motorhacmi.text()
        Çekiş = self.ui.lineEdit_cekis.text()
        Kapı = self.ui.lineEdit_kapi.text()
        Renk = self.ui.lineEdit_renk.text()
        Motor_No = self.ui.lineEdit_motorno.text()
        Şasi_No = self.ui.lineEdit_sasino.text()
        Günlük_Kiralama_Bedeli = self.ui.lineEdit_gunlukkira.text()
        Kirada_Mı = self.ui.checkBox_kiradami.isChecked()
        Kullanım_Dışı_Mı = self.ui.checkBox_kullanimdisimi.isChecked()
    
        self.deger.mycursor.execute("""
            UPDATE `db90220000250`.`arac_bilgileri_girisi` 
            SET `Araç Türü` = %s, `Marka` = %s, `Model` = %s, `Üretim Yılı` = %s, `Yakıt Türü` = %s, `Vites` = %s, `Motor Gücü` = %s, `Kasa Tipi` = %s, `Motor Hacmi` = %s, `Çekiş` = %s, `Kapı` = %s, `Renk` = %s, `Motor No` = %s, `Şasi No` = %s, `Günlük Kiralama Bedeli` = %s, `Kirada Mı?` = %s, `Kullanım Dışı Mı?` = %s
            WHERE `id` = %s
        """, (Araç_Türü, Marka, Model, Üretim_Yılı, Yakıt_Türü, Vites, Motor_Gücü, Kasa_Tipi, Motor_Hacmi, Çekiş, Kapı, Renk, Motor_No, Şasi_No, Günlük_Kiralama_Bedeli, Kirada_Mı, Kullanım_Dışı_Mı, id))
    
        self.deger.dbConn.commit()
        QMessageBox.information(self, "Başarılı", "Güncelleme işlemi başarılı.")
        self.ui.pushButton_guncelle.setEnabled(False)
    
        currentRow = self.ui.tableWidget_2.currentRow()
        self.ui.tableWidget_2.setItem(currentRow, 0, QTableWidgetItem(id))
        self.ui.tableWidget_2.setItem(currentRow, 1, QTableWidgetItem(Araç_Türü))
        self.ui.tableWidget_2.setItem(currentRow, 2, QTableWidgetItem(Marka))
        self.ui.tableWidget_2.setItem(currentRow, 3, QTableWidgetItem(Model))
        self.ui.tableWidget_2.setItem(currentRow, 4, QTableWidgetItem(Üretim_Yılı))
        self.ui.tableWidget_2.setItem(currentRow, 5, QTableWidgetItem(Yakıt_Türü))
        self.ui.tableWidget_2.setItem(currentRow, 6, QTableWidgetItem(Vites))
        self.ui.tableWidget_2.setItem(currentRow, 7, QTableWidgetItem(Motor_Gücü))
        self.ui.tableWidget_2.setItem(currentRow, 8, QTableWidgetItem(Kasa_Tipi))
        self.ui.tableWidget_2.setItem(currentRow, 9, QTableWidgetItem(Motor_Hacmi))
        self.ui.tableWidget_2.setItem(currentRow, 10, QTableWidgetItem(Çekiş))
        self.ui.tableWidget_2.setItem(currentRow, 11, QTableWidgetItem(Kapı))
        self.ui.tableWidget_2.setItem(currentRow, 12, QTableWidgetItem(Renk))
        self.ui.tableWidget_2.setItem(currentRow, 13, QTableWidgetItem(Motor_No))
        self.ui.tableWidget_2.setItem(currentRow, 14, QTableWidgetItem(Şasi_No))
        self.ui.tableWidget_2.setItem(currentRow, 15, QTableWidgetItem(Günlük_Kiralama_Bedeli))
        self.ui.tableWidget_2.setItem(currentRow, 16, QTableWidgetItem("Evet" if Kirada_Mı else "Hayır"))
        self.ui.tableWidget_2.setItem(currentRow, 17, QTableWidgetItem("Evet" if Kullanım_Dışı_Mı else "Hayır"))    
    
    def pushButton_kaydet(self):
        if self.ui.lineEdit_id.text() != "":
            result = self.mesaj("Bu kayıt mevcut. Güncelleme yapmak istediğinize emin misiniz?")
            if result == QMessageBox.Yes:
                self.pushButton_guncelle()
            else:
                QMessageBox.information(self, "İptal", "Güncelleme işlemi iptal edildi.")
        else:
            self.deger.mycursor.execute("SELECT MAX(id) FROM `arac_bilgileri_girisi`")
            max_id = self.deger.mycursor.fetchone()[0]
            if max_id is None:
                new_id = 1
            else:
                new_id = max_id + 1
    
            self.sql = """
                INSERT INTO `arac_bilgileri_girisi` 
                (`id`, `Araç Türü`, `Marka`, `Model`, `Üretim Yılı`, `Yakıt Türü`, `Vites`, `Motor Gücü`, `Kasa Tipi`, `Motor Hacmi`, `Çekiş`, `Kapı`, `Renk`, `Motor No`, `Şasi No`, `Günlük Kiralama Bedeli`, `Kirada Mı?`, `Kullanım Dışı Mı?`) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.veri = (
                new_id,
                self.ui.lineEdit_aracturu.text(), 
                self.ui.lineEdit_marka.text(), 
                self.ui.lineEdit_model.text(), 
                self.ui.lineEdit_uretimyili.text(), 
                self.ui.lineEdit_yakitturu.text(), 
                self.ui.lineEdit_vites.text(), 
                self.ui.lineEdit_motorgucu.text(), 
                self.ui.lineEdit_kasatipi.text(),
                self.ui.lineEdit_motorhacmi.text(),
                self.ui.lineEdit_cekis.text(), 
                self.ui.lineEdit_kapi.text(),
                self.ui.lineEdit_renk.text(),
                self.ui.lineEdit_motorno.text(),
                self.ui.lineEdit_sasino.text(),
                self.ui.lineEdit_gunlukkira.text(),
                self.ui.checkBox_kiradami.isChecked(),
                self.ui.checkBox_kullanimdisimi.isChecked()
            )
            self.deger.mycursor.execute(self.sql, self.veri)
            self.deger.dbConn.commit()
            QMessageBox.information(self, "Başarılı", "Kayıt işlemi başarılı.")   
            
            rowPosition = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(rowPosition)
            self.ui.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(str(new_id)))
            self.ui.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(self.ui.lineEdit_aracturu.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(self.ui.lineEdit_marka.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(self.ui.lineEdit_model.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 4, QTableWidgetItem(self.ui.lineEdit_uretimyili.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 5, QTableWidgetItem(self.ui.lineEdit_yakitturu.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 6, QTableWidgetItem(self.ui.lineEdit_vites.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 7, QTableWidgetItem(self.ui.lineEdit_motorgucu.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 8, QTableWidgetItem(self.ui.lineEdit_kasatipi.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 9, QTableWidgetItem(self.ui.lineEdit_motorhacmi.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 10, QTableWidgetItem(self.ui.lineEdit_cekis.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 11, QTableWidgetItem(self.ui.lineEdit_kapi.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 12, QTableWidgetItem(self.ui.lineEdit_renk.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 13, QTableWidgetItem(self.ui.lineEdit_motorno.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 14, QTableWidgetItem(self.ui.lineEdit_sasino.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 15, QTableWidgetItem(self.ui.lineEdit_gunlukkira.text()))
            self.ui.tableWidget_2.setItem(rowPosition, 16, QTableWidgetItem("Evet" if self.ui.checkBox_kiradami.isChecked() else "Hayır"))
            self.ui.tableWidget_2.setItem(rowPosition, 17, QTableWidgetItem("Evet" if self.ui.checkBox_kullanimdisimi.isChecked() else "Hayır"))
    
            self.ui.lineEdit_id.clear()
            self.ui.lineEdit_aracturu.clear()
            self.ui.lineEdit_marka.clear()
            self.ui.lineEdit_model.clear()
            self.ui.lineEdit_uretimyili.clear()
            self.ui.lineEdit_yakitturu.clear()
            self.ui.lineEdit_vites.clear()
            self.ui.lineEdit_motorgucu.clear()
            self.ui.lineEdit_kasatipi.clear()
            self.ui.lineEdit_motorhacmi.clear()
            self.ui.lineEdit_cekis.clear()
            self.ui.lineEdit_kapi.clear()
            self.ui.lineEdit_renk.clear()
            self.ui.lineEdit_motorno.clear()
            self.ui.lineEdit_sasino.clear()
            self.ui.lineEdit_gunlukkira.clear()
            self.ui.checkBox_kiradami.setChecked(False)
            self.ui.checkBox_kullanimdisimi.setChecked(False)                   
    
    def pushButton_sil(self):
        result = self.mesaj("Seçili kaydı silmek istediğinize emin misiniz?")
        if result == QMessageBox.Yes:
            id = int(self.ui.lineEdit_id.text())
            self.deger.mycursor.execute(f"DELETE FROM `db90220000250`.`arac_bilgileri_girisi` WHERE `id` = {id};")
            self.deger.dbConn.commit()
        
            currentRow = self.ui.tableWidget_2.currentRow()
            self.ui.tableWidget_2.removeRow(currentRow)
        
            self.ui.pushButton_sil.setEnabled(False)
            QMessageBox.information(self, "Başarılı", "Silme işlemi başarılı.")
            
            self.ui.lineEdit_id.clear()
            self.ui.lineEdit_aracturu.clear()
            self.ui.lineEdit_marka.clear()
            self.ui.lineEdit_model.clear()
            self.ui.lineEdit_uretimyili.clear()
            self.ui.lineEdit_yakitturu.clear()
            self.ui.lineEdit_vites.clear()
            self.ui.lineEdit_motorgucu.clear()
            self.ui.lineEdit_kasatipi.clear()
            self.ui.lineEdit_motorhacmi.clear()
            self.ui.lineEdit_cekis.clear()
            self.ui.lineEdit_kapi.clear()
            self.ui.lineEdit_renk.clear()
            self.ui.lineEdit_motorno.clear()
            self.ui.lineEdit_sasino.clear()
            self.ui.lineEdit_gunlukkira.clear()
            self.ui.checkBox_kiradami.setChecked(False)
            self.ui.checkBox_kullanimdisimi.setChecked(False)
        else:
            QMessageBox.information(self, "İptal", "Silme işlemi iptal edildi.")               
    
    def pushButton_ara(self):
        self.dorduncuPencere = Bul3(self.deger, self)
        self.dorduncuPencere.show()

    def pushButton_kapat(self):
        self.close()

    def cellDoubleClicked(self):
        self.ui.pushButton_guncelle.setEnabled(True)
        self.ui.pushButton_sil.setEnabled(True)
        rowSec=int(self.ui.tableWidget_2.currentRow())
        if(rowSec>=0):
            self.ui.lineEdit_id.setText(str(self.ui.tableWidget_2.item(rowSec,0).text()))
            self.ui.lineEdit_aracturu.setText(str(self.ui.tableWidget_2.item(rowSec,1).text()))
            self.ui.lineEdit_marka.setText(str(self.ui.tableWidget_2.item(rowSec,2).text()))
            self.ui.lineEdit_model.setText(str(self.ui.tableWidget_2.item(rowSec,3).text()))
            self.ui.lineEdit_uretimyili.setText(str(self.ui.tableWidget_2.item(rowSec,4).text()))
            self.ui.lineEdit_yakitturu.setText(str(self.ui.tableWidget_2.item(rowSec,5).text()))
            self.ui.lineEdit_vites.setText(str(self.ui.tableWidget_2.item(rowSec,6).text()))
            self.ui.lineEdit_motorgucu.setText(str(self.ui.tableWidget_2.item(rowSec,7).text()))
            self.ui.lineEdit_kasatipi.setText(str(self.ui.tableWidget_2.item(rowSec,8).text()))
            self.ui.lineEdit_motorhacmi.setText(str(self.ui.tableWidget_2.item(rowSec,9).text()))
            self.ui.lineEdit_cekis.setText(str(self.ui.tableWidget_2.item(rowSec,10).text()))
            self.ui.lineEdit_kapi.setText(str(self.ui.tableWidget_2.item(rowSec,11).text()))
            self.ui.lineEdit_renk.setText(str(self.ui.tableWidget_2.item(rowSec,12).text()))
            self.ui.lineEdit_motorno.setText(str(self.ui.tableWidget_2.item(rowSec,13).text()))
            self.ui.lineEdit_sasino.setText(str(self.ui.tableWidget_2.item(rowSec,14).text()))
            self.ui.lineEdit_gunlukkira.setText(str(self.ui.tableWidget_2.item(rowSec,15).text()))
            self.ui.checkBox_kiradami.setText(str(self.ui.tableWidget_2.item(rowSec,16).text()))
            self.ui.checkBox_kullanimdisimi.setText(str(self.ui.tableWidget_2.item(rowSec,17).text()))
            
    def cellChanged(self):
        rowSec=int(self.ui.tableWidget_2.currentRow())
        if(rowSec>=0):
            self.ui.lineEdit_id.setText(str(self.ui.tableWidget_2.item(rowSec,0).text()))
            self.ui.lineEdit_aracturu.setText(str(self.ui.tableWidget_2.item(rowSec,1).text()))
            self.ui.lineEdit_marka.setText(str(self.ui.tableWidget_2.item(rowSec,2).text()))
            self.ui.lineEdit_model.setText(str(self.ui.tableWidget_2.item(rowSec,3).text()))
            self.ui.lineEdit_uretimyili.setText(str(self.ui.tableWidget_2.item(rowSec,4).text()))
            self.ui.lineEdit_yakitturu.setText(str(self.ui.tableWidget_2.item(rowSec,5).text()))
            self.ui.lineEdit_vites.setText(str(self.ui.tableWidget_2.item(rowSec,6).text()))
            self.ui.lineEdit_motorgucu.setText(str(self.ui.tableWidget_2.item(rowSec,7).text()))
            self.ui.lineEdit_kasatipi.setText(str(self.ui.tableWidget_2.item(rowSec,8).text()))
            self.ui.lineEdit_motorhacmi.setText(str(self.ui.tableWidget_2.item(rowSec,9).text()))
            self.ui.lineEdit_cekis.setText(str(self.ui.tableWidget_2.item(rowSec,10).text()))
            self.ui.lineEdit_kapi.setText(str(self.ui.tableWidget_2.item(rowSec,11).text()))
            self.ui.lineEdit_renk.setText(str(self.ui.tableWidget_2.item(rowSec,12).text()))
            self.ui.lineEdit_motorno.setText(str(self.ui.tableWidget_2.item(rowSec,13).text()))
            self.ui.lineEdit_sasino.setText(str(self.ui.tableWidget_2.item(rowSec,14).text()))
            self.ui.lineEdit_gunlukkira.setText(str(self.ui.tableWidget_2.item(rowSec,15).text()))
            self.ui.checkBox_kiradami.setText(str(self.ui.tableWidget_2.item(rowSec,16).text()))
            self.ui.checkBox_kullanimdisimi.setText(str(self.ui.tableWidget_2.item(rowSec,17).text()))
            
    def mesaj(self, metin):
        self.message_box = QMessageBox()
        self.message_box.setText(metin)
        self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.message_box.setDefaultButton(QMessageBox.No)
        return self.message_box.exec()
            
            
            
class ucuncuPencere(QMainWindow):
    def __init__(self, deger):
        super().__init__()
        self.ui = Ui_Form5()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger
        
        self.ui.kapatbuton.clicked.connect(self.kapatbuton)
        
        self.ui.araclisteWidget.setColumnCount(6)
        self.ui.araclisteWidget.setRowCount(11)
        self.ui.araclisteWidget.setHorizontalHeaderLabels(
            ["id", "Müşteri Adı", "Müşteri Soyadı", "Araç Marka", "Araç Model", "Kaç Gün Kiralanacak?", "Yolculuk Nereye?"]
        )
        for i in range(11):
            self.ui.araclisteWidget.setColumnWidth(0, 10)
            self.ui.araclisteWidget.setColumnWidth(1, 100)
            self.ui.araclisteWidget.setColumnWidth(2, 100)
            self.ui.araclisteWidget.setColumnWidth(3, 100)
            self.ui.araclisteWidget.setColumnWidth(4, 100)
            self.ui.araclisteWidget.setColumnWidth(5, 150)
            self.ui.araclisteWidget.setColumnWidth(6, 150)
            self.ui.araclisteWidget.setColumnWidth(7, 100)
            
    def showEvent(self, event):
        self.loadBesinciPencereData()
        super().showEvent(event)
        
    def loadBesinciPencereData(self):
        query = "SELECT * FROM arac_kiralama_bilgileri_girisi"
        self.loadDataIntoTableWidget(self.ui.araclisteWidget, query)

    def loadDataIntoTableWidget(self, tableWidget, query):
        self.dbConn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="deneme",
            database="db90220000250"
        )
        cursor = self.dbConn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        
        tableWidget.setRowCount(len(rows))
        for rowIndex, row in enumerate(rows):
            for colIndex, data in enumerate(row):
                tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(data)))
        
        cursor.close()
        self.dbConn.close()
        
    def kapatbuton(self):
        self.close()
    
    
        
class Bul(QMainWindow):
    def __init__(self, deger, ikinciPencere):
        super().__init__()
        self.ui = Ui_Bul()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger
        self.ikinciPencere = ikinciPencere
        
        self.ui.bulButton.clicked.connect(self.bulButton)
        
    def bulButton(self):
        self.ad = self.ui.adlineEdit2.text()
        self.soyad = self.ui.soyadlineEdit2.text()
        self.tc = self.ui.tckimliklineEdit2.text()
        self.dtarih = self.ui.dogumtarihilineEdit2.text()
        self.adres = self.ui.adreslineEdit2.text()
        self.telno = self.ui.telnolineEdit2.text()
        self.meslek = self.ui.mesleklineEdit2.text()
        self.ehliyet = self.ui.ehliyetsinifilineEdit2.text()
        self.medenidurumu = self.ui.medenidurumulineEdit2.text()
        self.egitimdurumu = self.ui.egitimdurumulineEdit2.text()
        
        if (self.ad == "") and (self.soyad == "") and (self.tc == "") and (self.dtarih == "") and (self.adres == "") and (self.telno == "") and (self.meslek == "") and (self.ehliyet == "") and (self.medenidurumu == "") and (self.egitimdurumu == ""):
            QMessageBox.warning(self, "Hata", "Lütfen arama yapmak için en az bir kriter giriniz.")
        else:
            conditions = []
            if self.ad:
                conditions.append(f"`Ad`='{self.ad}'")
            if self.soyad:
                conditions.append(f"`Soyad`='{self.soyad}'")
            if self.tc:
                conditions.append(f"`TC_Kimlik_No`='{self.tc}'")
            if self.dtarih:
                conditions.append(f"`Dogum_Tarihi`='{self.dtarih}'")
            if self.adres:
                conditions.append(f"`Adres`='{self.adres}'")
            if self.telno:
                conditions.append(f"`Telefon_No`='{self.telno}'")
            if self.meslek:
                conditions.append(f"`Meslek`='{self.meslek}'")
            if self.ehliyet:
                conditions.append(f"`Ehliyet_Sinifi`='{self.ehliyet}'")
            if self.medenidurumu:
                conditions.append(f"`Medeni_Durumu`='{self.medenidurumu}'")
            if self.egitimdurumu:
                conditions.append(f"`Egitim_Durumu`='{self.egitimdurumu}'")
            
            query = f"SELECT * FROM `musteri_bilgileri_girisi` WHERE {' OR '.join(conditions)}"
            self.deger.mycursor.execute(query)
            results = self.deger.mycursor.fetchall()
            
            if results:
                self.ikinciPencere.ui.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(results):
                    self.ikinciPencere.ui.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ikinciPencere.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.close()
            else:
                QMessageBox.information(self, "Sonuç Yok", "Arama kriterlerine uygun kayıt bulunamadı.")          
          
   
          
class Bul2(QMainWindow):
    def __init__(self, deger, besinciPencere):
        super().__init__()
        self.ui = Ui_Bul2()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger
        self.besinciPencere = besinciPencere
        
        self.ui.pushButtonBUL.clicked.connect(self.pushButtonBUL)
        
    def pushButtonBUL(self):
        self.musteri_adi = self.ui.lineEdit.text()
        self.musteri_soyadi = self.ui.lineEdit_2.text()
        self.arac_marka = self.ui.lineEdit_3.text()
        self.arac_model = self.ui.lineEdit_4.text() 
        self.kacgunkira = self.ui.lineEdit_5.text()
        self.yolculuknereye = self.ui.lineEdit_6.text()
        
        if (self.musteri_adi == "") and (self.musteri_soyadi == "") and (self.arac_marka == "") and (self.arac_model == "") and (self.kacgunkira == "") and (self.yolculuknereye == ""):
            QMessageBox.warning(self, "Hata", "Lütfen arama yapmak için en az bir kriter giriniz.")
        else:
            conditions = []
            if self.musteri_adi:
                conditions.append(f"`Müşteri Adı`='{self.musteri_adi}'")
            if self.musteri_soyadi:
                conditions.append(f"`Müşteri Soyadı`='{self.musteri_soyadi}'")
            if self.arac_marka:
                conditions.append(f"`Araç Marka`='{self.arac_marka}'")
            if self.arac_model:
                conditions.append(f"`Araç Model`='{self.arac_model}'")
            if self.kacgunkira:
                conditions.append(f"`Kaç Gün Kiralanacak?`='{self.kacgunkira}'")
            if self.yolculuknereye:
                conditions.append(f"`Yolculuk Nereye?`='{self.yolculuknereye}'")
            
            query = f"SELECT * FROM `arac_kiralama_bilgileri_girisi` WHERE {' OR '.join(conditions)}"
            self.deger.mycursor.execute(query)
            results = self.deger.mycursor.fetchall()
            
            if results:
                self.besinciPencere.ui.akbg_tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(results):
                    self.besinciPencere.ui.akbg_tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.besinciPencere.ui.akbg_tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.close()
            else:
                QMessageBox.information(self, "Sonuç Yok", "Arama kriterlerine uygun kayıt bulunamadı.")          
        
        
        
class Bul3(QMainWindow):
    def __init__(self, deger, dorduncuPencere):
        super().__init__()
        self.ui = Ui_Bul3()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.deger = deger
        self.dorduncuPencere = dorduncuPencere
        
        self.ui.pushButtonBuL.clicked.connect(self.pushButtonBuL)
        
    def pushButtonBuL(self):
        self.aracturu = self.ui.aracturulineEdit.text()
        self.marka = self.ui.markalineEdit.text()
        self.model = self.ui.modellineEdit.text()
        self.uretimyili = self.ui.uretimyililineEdit.text()
        self.yakitturu = self.ui.yakitturulineEdit.text()
        self.vites = self.ui.viteslineEdit.text()
        self.motorgucu = self.ui.motorguculineEdit.text()
        self.kasatipi = self.ui.kasatipilineEdit.text()
        self.motorhacmi = self.ui.motorhacmilineEdit.text()
        self.cekis = self.ui.cekislineEdit.text()
        self.kapi = self.ui.kapilineEdit.text()
        self.renk = self.ui.renklineEdit.text()
        self.motorno = self.ui.motornolineEdit.text()
        self.sasino = self.ui.sasinolineEdit.text()
        self.gunlukkira = self.ui.gunlukkiralamabedelilineEdit.text()
        self.kiradami = self.ui.kiradamicheckBox.isChecked()
        self.kullanimdisimi = self.ui.kullanimdisimicheckBox.isChecked()
          
        if (self.aracturu == "" and self.marka == "" and self.model == "" and self.uretimyili == "" and 
            self.yakitturu == "" and self.vites == "" and self.motorgucu == "" and self.kasatipi == "" and 
            self.motorhacmi == "" and self.cekis == "" and self.kapi == "" and self.renk == "" and 
            self.motorno == "" and self.sasino == "" and self.gunlukkira == "" and not self.kiradami and 
            not self.kullanimdisimi):
            QMessageBox.warning(self, "Hata", "Lütfen arama yapmak için en az bir kriter giriniz.")
        else:
            conditions = []
            if self.aracturu:
                conditions.append(f"`Araç Türü`='{self.aracturu}'")
            if self.marka:
                conditions.append(f"`Marka`='{self.marka}'")
            if self.model:
                conditions.append(f"`Model`='{self.model}'")
            if self.uretimyili:
                conditions.append(f"`Üretim Yılı`='{self.uretimyili}'")
            if self.yakitturu:
                conditions.append(f"`Yakıt Türü`='{self.yakitturu}'")
            if self.vites:
                conditions.append(f"`Vites`='{self.vites}'")
            if self.motorgucu:
                conditions.append(f"`Motor Gücü`='{self.motorgucu}'")
            if self.kasatipi:
                conditions.append(f"`Kasa Tipi`='{self.kasatipi}'")
            if self.motorhacmi:
                conditions.append(f"`Motor Hacmi`='{self.motorhacmi}'")
            if self.cekis:
                conditions.append(f"`Çekiş`='{self.cekis}'")
            if self.kapi:
                conditions.append(f"`Kapı`='{self.kapi}'")
            if self.renk:
                conditions.append(f"`Renk`='{self.renk}'")
            if self.motorno:
                conditions.append(f"`Motor No`='{self.motorno}'")
            if self.sasino:
                conditions.append(f"`Şasi No`='{self.sasino}'")
            if self.gunlukkira:
                conditions.append(f"`Günlük Kiralama Bedeli`='{self.gunlukkira}'")
            if self.kiradami:
                conditions.append("`Kirada Mı?`=1")
            else:
                conditions.append("`Kirada Mı?`=0")
            if self.kullanimdisimi:
                conditions.append("`Kullanım Dışı Mı?`=1")
            else:
                conditions.append("`Kullanım Dışı Mı?`=0")
                        
            query = f"SELECT * FROM `arac_bilgileri_girisi` WHERE {' AND '.join(conditions)}"
            self.deger.mycursor.execute(query)
            results = self.deger.mycursor.fetchall()
        
            if results:
                self.dorduncuPencere.ui.tableWidget_2.setRowCount(0)
                for row_number, row_data in enumerate(results):
                    self.dorduncuPencere.ui.tableWidget_2.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.dorduncuPencere.ui.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.close()
            else:
                QMessageBox.information(self, "Sonuç Yok", "Arama kriterlerine uygun kayıt bulunamadı.")          



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaPencere()
    widget.show()
    sys.exit(app.exec())
