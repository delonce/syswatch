# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\swimix\PycharmProjects\pythonProject2\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import re
from main import find_clients, get_report
from reports import Correcting_report, word_report, pdf_report, html_report, xml_report


ip_match = r'\b(?:\d{1,3}\.){3}\d{1,3}\/\d+\b, \d+'
COMPUTERS = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #snap

        # Create a QTextEdit widget to display the text from the file
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(50, 80, 700, 300))
        self.text_edit.setReadOnly(True)
        self.text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_edit.setVisible(False)
        font = self.text_edit.font()
        font.setPointSize(font.pointSize() + 3)
        self.text_edit.setFont(font)

        #кнопка старта
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(320, 440, 151, 51))
        self.start_button.clicked.connect(self.ClickedStart)




        font = QtGui.QFont()
        font.setPointSize(13)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")

        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(290, 25, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)

        self.name.setFont(font)
        self.name.setObjectName("name")
        #выберите формат
        self.colecting_description = QtWidgets.QLabel(self.centralwidget)
        self.colecting_description.setGeometry(QtCore.QRect(25, 875, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colecting_description.setFont(font)
        self.colecting_description.setObjectName("colecting_description")
        #харки устр-ва
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(100, 25, 650, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description.setFont(font)
        self.description.setObjectName("description")

        #надпись второго окна
        self.ip_input = QtWidgets.QLabel(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(175, 25, 650, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ip_input.setFont(font)
        self.ip_input.setObjectName("ip_input")
        self.ip_input.setVisible(False)

        # надпись сбора данных
        self.grep_text = QtWidgets.QLabel(self.centralwidget)
        self.grep_text.setGeometry(QtCore.QRect(35, 75, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grep_text.setFont(font)
        self.grep_text.setObjectName("grep_text")
        self.grep_text.setVisible(False)


        #ввод айпи
        self.input_field = QtWidgets.QLineEdit(self.centralwidget)
        self.input_field.setVisible(False)
        self.input_field.setGeometry(QtCore.QRect(175, 250, 400, 35))

        #кнопка подтверждения
        self.accept = QtWidgets.QPushButton(self.centralwidget)
        self.accept.setGeometry(QtCore.QRect(300, 300, 151, 40))
        self.accept.clicked.connect(self.ClickedAccept)
        self.accept.setVisible(False)

        #кнопка сбора всех отчетов
        '''
        self.colecting_button = QtWidgets.QPushButton(self.centralwidget)
        self.colecting_button.setGeometry(QtCore.QRect(300, 300, 151, 40))
        #self.colecting_button.clicked.connect(self.ClickedAccept)
        self.colecting_button.setVisible(False)'''

        #кнопка обратно
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.back_button.clicked.connect(self.ClickedBack)
        self.back_button.setVisible(False)


        # кнопка сбора отчета xml
        self.generate_xml = QtWidgets.QPushButton(self.centralwidget)
        self.generate_xml.setGeometry(QtCore.QRect(25, 935, 80, 40))
        self.generate_xml.clicked.connect(self.ClickedXml)
        self.generate_xml.setVisible(False)

        # кнопка сбора отчета docx
        self.generate_docx = QtWidgets.QPushButton(self.centralwidget)
        self.generate_docx.setGeometry(QtCore.QRect(145, 935, 80, 40))
        self.generate_docx.clicked.connect(self.ClickedDocx)
        self.generate_docx.setVisible(False)
        # кнопка сбора отчета пдф
        self.generate_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.generate_pdf.setGeometry(QtCore.QRect(265, 935, 80, 40))
        self.generate_pdf.clicked.connect(self.ClickedPdf)
        self.generate_pdf.setVisible(False)
        # кнопка сбора отчета html
        self.generate_html = QtWidgets.QPushButton(self.centralwidget)
        self.generate_html.setGeometry(QtCore.QRect(385, 935, 80, 40))
        self.generate_html.clicked.connect(self.ClickedHtml)
        self.generate_html.setVisible(False)

        #Характеристики
        self.colected_description = QtWidgets.QLabel(self.centralwidget)
        self.colected_description.setGeometry(QtCore.QRect(25, 0, 400, 201))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.colected_description.setFont(font)
        self.colected_description.setObjectName("colected_description")
        self.colected_description.setVisible(False)





        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SysWatch"))
        self.start_button.setText(_translate("MainWindow", "Старт"))
        self.name.setText(_translate("MainWindow", "SysWatch"))
        self.ip_input.setText(_translate("MainWindow", "Введите диапазон ip-адрессов, порт"))
        self.accept.setText(_translate("MainWindow", "Подтвердить"))
        self.description.setText(_translate("MainWindow", "\n\n    Программа SysWatch - отечественная разработка, \nработающая на ОС Linux.\n    Благодаря возможности запуска по сети осуществляется\nполноценный сбор информации о программных и аппаратных\nхарактеристиках всех рабочих станций, подключенных к\nсерверу.\n    Собранная информация будет полезна для проведения\nинвентаризации и анализа защищенности ОИ.\n\n\n\tДля начала работы нажмите на кнопку \"Старт\" "))
        self.colected_description.setText(_translate("MainWindow", "Характеристики устройства:"))
        self.grep_text.setText(_translate("MainWindow", "Доступные хосты:"))
        #self.colecting_button.setText(_translate("MainWindow", "Сгенерировать отчет по \nвсем устройствам"))
        self.back_button.setText(_translate("MainWindow", "←"))
        self.generate_xml.setText(_translate("MainWindow", ".xml"))
        self.generate_docx.setText(_translate("MainWindow", ".docx"))
        self.generate_pdf.setText(_translate("MainWindow", ".pdf"))
        self.generate_html.setText(_translate("MainWindow", ".html"))
        self.colecting_description.setText(_translate("MainWindow", "Выберите формат отчета:"))

    def ClickedStart(self):
        self.description.setVisible(False)
        self.start_button.setVisible(False)
        self.input_field.setVisible(True)
        self.ip_input.setVisible(True)

        self.accept.setVisible(True)

    def ClickedAccept(self):

        ip_port = self.input_field.text()
        if re.match(ip_match, ip_port):
            address, port = ip_port.split(", ")


            result = find_clients(address, port)
            #self.grep_text.setVisible(True)
            while not result.empty():
                ip, port = result.get()
                print(ip, port)
                COMPUTERS.append(ip)
                get_report(ip, port)
            self.accept.setVisible(False)
            self.ip_input.setVisible(False)
            self.input_field.setVisible(False)

            _translate = QtCore.QCoreApplication.translate

            x = 35
            y = 175
            for computer in COMPUTERS:
                self.button = QtWidgets.QPushButton(self.centralwidget)
                self.button.setText(_translate("MainWindow", f"{computer}"))
                self.button.setVisible(True)
                self.button.setGeometry(QtCore.QRect(x, y, 100, 35))
                self.button.clicked.connect(
                    lambda checked,  button_name=computer: self.ClickedProperties(button_name))
                y = y + 50

            self.grep_text.setVisible(True)
            #self.colecting_button.setVisible(True)
        else:
            error_message = QtWidgets.QMessageBox()
            error_message.setIcon(QtWidgets.QMessageBox.Critical)
            error_message.setWindowTitle("Ошибка")
            error_message.setText("Произошла ошибка!\nВы ввели данные в неверном формате!")
            error_message.exec_()




    def ClickedProperties(self, button_name):
        self.name_comp =button_name
        with open(f'{button_name}.txt', 'r') as file:
            text = file.read()
            decoded_text = text.encode().decode('unicode_escape')
            self.text_edit.setPlainText(decoded_text)



        self.colected_description.setVisible(False)
        self.grep_text.setVisible(False)
        self.button.setVisible(False)
        #self.colecting_button.setVisible(False)

        MainWindow.showMaximized()

        self.name.setGeometry(QtCore.QRect(900, 15, 221, 90))

        self.colected_description.setVisible(True)
        self.text_edit.setVisible(True)
        self.text_edit.setGeometry(QtCore.QRect(25, 120, 1800, 750))
        self.text_edit.raise_()
        self.back_button.setVisible(True)
        self.generate_html.setVisible(True)
        self.generate_xml.setVisible(True)
        self.generate_docx.setVisible(True)
        self.generate_pdf.setVisible(True)
        Correcting_report(f"{button_name}.txt")
    def ClickedBack(self):
        MainWindow.resize(806, 609)
        self.name.setGeometry(QtCore.QRect(290, 25, 221, 91))
        self.back_button.setVisible(False)
        self.text_edit.setVisible(False)
        self.grep_text.setVisible(True)
        self.button.setVisible(True)
        #self.colecting_button.setVisible(True)

        self.colected_description.setVisible(False)
        self.grep_text.setVisible(True)
        self.button.setVisible(True)
        #self.colecting_button.setVisible(True)
    def ClickedXml(self):
        xml_report(f'correct-{self.name_comp}.txt', self.name_comp)
    def ClickedDocx(self):
        word_report(f'correct-{self.name_comp}.txt', self.name_comp)
    def ClickedPdf(self):
        pdf_report(f'correct-{self.name_comp}.txt', self.name_comp)
    def ClickedHtml(self):
        html_report(f'correct-{self.name_comp}.txt', self.name_comp)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())