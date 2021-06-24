# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matriz import matriz
from matriz_cont import matriz_cont
from nodo_matriz import nodo_matriz
from ventana_ui import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        #self.btn_fin_turno.clicked.connect(self.insertar_pieza(2,2))
        self.btn_estado.setText("Presionar")

if __name__ == '__main__':
    print("""""""""""")
    funciones_matriz = matriz()
    func_matriz_cont = matriz_cont()
    x = int(input('Ingresar posicion x :'))
    y = int(input('Ingresar posicion y :'))
    cont = input('Ingresar color: ')
    funciones_matriz.ordenar_cab_fila(y)
    funciones_matriz.ordenar_cab_columna(x)
    print('***************************')

    funciones_matriz.insertar_x_final(4)
    funciones_matriz.insertar_y_final(4)
    print('*****************************')
    funciones_matriz.insertar_x_final(8)
    funciones_matriz.insertar_x_antes(3,4)
    funciones_matriz.insertar_x_antes(6,8)
    funciones_matriz.insertar_x_final(10)
    print('*******************************')

    funciones_matriz.insertar_y_final(8)
    funciones_matriz.insertar_y_antes(3,4)
    funciones_matriz.insertar_y_antes(6,8)
    funciones_matriz.insertar_y_final(10)
   # funciones_matriz.ordenar_cab_fila(int(5))
    #funciones_matriz.ordenar_cab_fila(int(8))
    print('*******************************')
    #func_matriz_cont.insertarx(x,y,funciones_matriz,nodo_matriz(cont,x,y))
    #func_matriz_cont.insertary(x,y,funciones_matriz,nodo_matriz(cont,x,y))
    #func_matriz_cont.mostrar_columna(x,funciones_matriz)

    #func_matriz_cont.mostrar_fila(y,funciones_matriz)
    funciones_matriz.buscar_y(2)
    funciones_matriz.buscar_x(2)
    #funciones_matriz.buscar_x(x)
    print("********************************")
    print("probar insertar antes de 2 un 1 en columnas")
    funciones_matriz.ordenar_cab_fila(1)
    print("probar inserta despues de 10 un 11 en columnas")
    funciones_matriz.ordenar_cab_fila(11)
    print("inserta antes de 6")
    funciones_matriz.ordenar_cab_fila(5)
    print("inserar antes de 10")
    funciones_matriz.ordenar_cab_fila(9)
    print("*******************************")
    funciones_matriz.buscar_y(1)

    print("*******************************")
    func_matriz_cont.Insertar(10,11,funciones_matriz,nodo_matriz("color1",10,11))
    func_matriz_cont.Insertar(4, 11, funciones_matriz, nodo_matriz("color2", 4, 11))
    func_matriz_cont.Insertar(2, 11, funciones_matriz, nodo_matriz("color2", 2, 11))
    func_matriz_cont.Insertar(3, 11, funciones_matriz, nodo_matriz("color2", 3, 11))
    func_matriz_cont.Insertar(10, 8, funciones_matriz, nodo_matriz("color1", 10, 8))
    func_matriz_cont.Insertar(10, 2, funciones_matriz, nodo_matriz("color1", 10, 2))
    func_matriz_cont.Insertar(10, 4, funciones_matriz, nodo_matriz("color1", 10, 4))
    func_matriz_cont.Insertar(8, 2, funciones_matriz, nodo_matriz("color1", 8, 2))
    func_matriz_cont.Insertar(2, 2, funciones_matriz, nodo_matriz("color1",2, 2))

    func_matriz_cont.Insertar(3, 4, funciones_matriz, nodo_matriz("color1",3, 4))
    func_matriz_cont.Insertar(4, 3, funciones_matriz, nodo_matriz("color1", 4, 3))
    func_matriz_cont.Insertar(3, 5, funciones_matriz, nodo_matriz("color1", 3, 5))
    func_matriz_cont.Insertar(3, 6, funciones_matriz, nodo_matriz("color1", 3, 6))

    func_matriz_cont.Insertar(8, 11, funciones_matriz, nodo_matriz("color1", 8, 11))
    func_matriz_cont.Insertar(4, 9, funciones_matriz, nodo_matriz("color1", 4, 9))
    func_matriz_cont.Insertar(4, 10, funciones_matriz, nodo_matriz("color1", 4, 10))
    func_matriz_cont.Insertar(2, 1, funciones_matriz, nodo_matriz("color1", 2, 1))
    func_matriz_cont.Insertar(6, 1, funciones_matriz, nodo_matriz("color1", 6, 1))
    print("***********************************************")
    print("columnas")

    func_matriz_cont.mostrar_columna(10,funciones_matriz)
    print("****************************************")
    print("filas")
    func_matriz_cont.mostrar_fila(4,funciones_matriz)
    func_matriz_cont.report_graphiz(funciones_matriz)
    #Interfaz
    #app = QtWidgets.QApplication([])
    #window = MainWindow()
    #window.show()
    #app.exec_()