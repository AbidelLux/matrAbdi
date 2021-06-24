from nodo_cabezeraX import nodo_cabezeraX
from nodo_cabezeraY import nodo_cabezeraY

class matriz():
    def __init__(self):
        self.cabX = nodo_cabezeraX(0,0,"cabx")
        self.cabY= nodo_cabezeraY(0,0,"caby")
    def buscar_x(self, X):
        print('recorrer x')
        node = self.cabX
        while node is not None:
            print(node.fil_x)
            node = node.siguiente
    def buscar_y(self,y):
        print('recorrer y')
        node = self.cabY
        while node is not None:
            print(node.fil_y)

            node = node.abajo


#*************************************************
#funcion ordenar en X
    def ordenar_cab_columna(self, nuevoX):
        node = self.cabX
        while node is not None:
            sig = node.siguiente
            ant = node.anterior
            if sig is None:
                if ant is None:
                    print('Solo hay uno en la lista')
                    self.insertar_x_final(nuevoX)
                    break
            if ant is None:
                if sig is not None:

                    auxMin = min(node.fil_x,nuevoX,sig.fil_x)
                    auxMax = max(node.fil_x,nuevoX,sig.fil_x)
                    if auxMax == sig.fil_x and  auxMin == node.fil_x:
                        print(node.fil_x,'nodo primero')
                        self.insertar_x_antes(nuevoX,sig.fil_x)
                        break

            if sig is None:
                if ant is not None:
                    print(node.fil_x,'nodo ultimo')
                    auxMin = min(node.fil_x, nuevoX, ant.fil_x)
                    auxMax = max(node.fil_x, nuevoX, ant.fil_x)
                    if auxMax == nuevoX and auxMin == ant.fil_x:
                        self.insertar_x_final(nuevoX)
                        break

            if sig is not None:
                if ant is not None:
                    auxMin = min(node.fil_x, nuevoX, sig.fil_x)
                    auxMax = max(node.fil_x, nuevoX, sig.fil_x)
                    if auxMax == sig.fil_x and auxMin == node.fil_x:
                        print(node.fil_x,'Es un nodo en medio')
                        self.insertar_x_antes(nuevoX,sig.fil_x)
                        break
            node = node.siguiente
#*************************************************
#funcion ordenar en Y
    def ordenar_cab_fila(self, nuevoy):
        node = self.cabY
        while node is not None:
            sig = node.abajo
            ant = node.arriba
            if sig is None:
                if ant is None:
                    print('Solo hay uno en la lista')
                    self.insertar_y_final(nuevoy)
                    break
            if ant is None:
                if sig is not None:
                    auxMin = min(node.fil_y, nuevoy, sig.fil_y)
                    auxMax = max(node.fil_y, nuevoy, sig.fil_y)
                    if auxMax == sig.fil_y and auxMin == node.fil_y:
                        print(node.fil_y, 'nodo primero')
                        self.insertar_y_antes(nuevoy, sig.fil_y)
                        break

            if sig is None:
                if ant is not None:
                    print(node.fil_y, 'nodo ultimo')
                    auxMin = min(node.fil_y, nuevoy, ant.fil_y)
                    auxMax = max(node.fil_y, nuevoy, ant.fil_y)
                    if auxMax == nuevoy and auxMin == ant.fil_y:
                        self.insertar_y_final(nuevoy)
                        break
            if sig is not None:
                if ant is not None:
                    auxMin = min(node.fil_y, nuevoy, sig.fil_y)
                    auxMax = max(node.fil_y, nuevoy, sig.fil_y)
                    if auxMax == sig.fil_y and auxMin == node.fil_y:
                        print(node.fil_y, 'Es un nodo en medio')
                        self.insertar_y_antes(nuevoy, sig.fil_y)
                        break
            node = node.abajo
#*****************************************************************************************************
#Funciones para inserta en Y
    def insertar_y_final(self,nuevoy):
        if self.cabY is None:
            nuevo_nodo = nodo_cabezeraY(0,nuevoy,"caby")
            self.cabY = nuevo_nodo
            return
        node = self.cabY
        while node.abajo is not None:
            node = node.abajo
        nuevo_nodo = nodo_cabezeraY(0,nuevoy,"caby")
        node.abajo = nuevo_nodo
        nuevo_nodo.arriba = node
        print(nuevoy,'fila se agrego con exito')
    def insertar_y_antes(self,nuevoy,y):
        if self.cabY is None:
            print('Lista esta vacia')
            return
        else:
            node = self.cabY
            while node is not None:
                if node.fil_y == y:
                    break
                node = node.abajo
            if node is None:
                print('')
            else:
                nuevo_nodo = nodo_cabezeraY(0,nuevoy,"caby")
                nuevo_nodo.abajo = node
                nuevo_nodo.arriba = node.arriba
                if node.arriba is not None:
                    node.arriba.abajo = nuevo_nodo
                node.arriba = nuevo_nodo
                print(nuevoy,'fila se agrego con exito')
#*****************************************************************************
#funciones insertar en x

    def insertar_x_final(self,nuevox):
        if self.cabX is None:
            nuevo_nodo = nodo_cabezeraX(nuevox,0,"cabx")
            self.cabX = nuevo_nodo
            return
        node = self.cabX
        while node.siguiente is not None:
            node = node.siguiente
        nuevo_nodo = nodo_cabezeraX(nuevox,0,"cabx")
        node.siguiente = nuevo_nodo
        nuevo_nodo.anterior = node
        print(nuevox,'columna se agrego con exito')
    def insertar_x_antes(self,nuevox,x):
        if self.cabX is None:
            print('Lista esta vacia')
            return
        else:
            node = self.cabX
            while node is not None:
                if node.fil_x == x:
                    break
                node = node.siguiente
            if node is None:
                print('')
            else:
                nuevo_nodo = nodo_cabezeraX(nuevox,0,"cabx")
                nuevo_nodo.siguiente = node
                nuevo_nodo.anterior = node.anterior
                if node.anterior is not None:
                    node.anterior.siguiente = nuevo_nodo
                node.anterior = nuevo_nodo
                print(nuevox,'columna se agrego con exito')
