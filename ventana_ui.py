# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_estado = QtWidgets.QPushButton(self.centralwidget)
        self.btn_estado.setGeometry(QtCore.QRect(20, 70, 91, 23))
        self.btn_estado.setObjectName("btn_estado")
        self.btn_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrir.setGeometry(QtCore.QRect(20, 120, 91, 23))
        self.btn_abrir.setObjectName("btn_abrir")
        self.btn_reporte = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reporte.setGeometry(QtCore.QRect(20, 20, 91, 23))
        self.btn_reporte.setObjectName("btn_reporte")
        self.btn_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guardar.setGeometry(QtCore.QRect(20, 170, 91, 23))
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_ayuda = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ayuda.setGeometry(QtCore.QRect(20, 220, 91, 23))
        self.btn_ayuda.setObjectName("btn_ayuda")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.btn_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_iniciar.setGeometry(QtCore.QRect(410, 20, 75, 23))
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.btn_fin_turno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fin_turno.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.btn_fin_turno.setObjectName("btn_fin_turno")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 170, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 210, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 140, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lbPuntos = QtWidgets.QLabel(self.centralwidget)
        self.lbPuntos.setGeometry(QtCore.QRect(480, 140, 47, 13))
        self.lbPuntos.setObjectName("lbPuntos")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 170, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(400, 210, 47, 13))
        self.label_9.setObjectName("label_9")
        self.lb_tiempo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_tiempo_2.setGeometry(QtCore.QRect(400, 230, 71, 31))
        self.lb_tiempo_2.setObjectName("lb_tiempo_2")
        self.Tablero = QtWidgets.QFrame(self.centralwidget)
        self.Tablero.setEnabled(False)
        self.Tablero.setGeometry(QtCore.QRect(90, 290, 211, 141))
        self.Tablero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Tablero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Tablero.setObjectName("Tablero")
        self.txt_fila = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_fila.setGeometry(QtCore.QRect(200, 160, 81, 31))
        self.txt_fila.setObjectName("txt_fila")
        self.txt_col = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_col.setGeometry(QtCore.QRect(200, 210, 81, 31))
        self.txt_col.setObjectName("txt_col")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(460, 170, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.txt_fila_tablero = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_fila_tablero.setGeometry(QtCore.QRect(190, 20, 51, 31))
        self.txt_fila_tablero.setObjectName("txt_fila_tablero")
        self.txt_col_tablero = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_col_tablero.setGeometry(QtCore.QRect(320, 20, 61, 31))
        self.txt_col_tablero.setObjectName("txt_col_tablero")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.btn_estado.setText(_translate("MainWindow", "Estado Tablero"))
        self.btn_abrir.setText(_translate("MainWindow", "Abrir Partida"))
        self.btn_reporte.setText(_translate("MainWindow", "Reporte"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar Partida"))
        self.btn_ayuda.setText(_translate("MainWindow", "Ayuda"))
        self.label.setText(_translate("MainWindow", "Filas"))
        self.label_2.setText(_translate("MainWindow", "Columnas"))
        self.btn_iniciar.setText(_translate("MainWindow", "Iniciar Juego"))
        self.btn_fin_turno.setText(_translate("MainWindow", "Fin Turno"))
        self.label_3.setText(_translate("MainWindow", "Fila"))
        self.label_4.setText(_translate("MainWindow", "Columna"))
        self.label_5.setText(_translate("MainWindow", "Puntos:"))
        self.lbPuntos.setText(_translate("MainWindow", "0000"))
        self.label_7.setText(_translate("MainWindow", "Tiempo(s):"))
        self.label_9.setText(_translate("MainWindow", "Turno:"))
        self.lb_tiempo_2.setText(_translate("MainWindow", "Jugador No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

