import os


class matriz_cont():
    def __init__(self)-> None:
        self.head = None
    def filaNoExiste_ColNoExites(self,posx,posy,listaCabeza,nuevoNodo):
        listax = listaCabeza.cabX
        while listax is not None:
            if(listax.fil_x == posx):
                break
            listax=listax.siguiente
        listay = listaCabeza.cabY
        while listay is not None:
            if(listay.fil_y == posy):
                break
            listay = listay.abajo
        self.insertar_en_columna_final(listax, nuevoNodo)
        self.insertar_en_fila_final(listay, nuevoNodo)
    def Insertar(self, posx, posy, listaCabeza, nuevoNodo):
        listax = listaCabeza.cabX
        while listax is not None:
            if (listax.fil_x == posx):
                break
            listax = listax.siguiente
        listay = listaCabeza.cabY
        while listay is not None:
            if (listay.fil_y == posy):
                break
            listay = listay.abajo
        self.validar_insertar_columna(listax,nuevoNodo,posy)
        self.validar_insertar_fila(listay, nuevoNodo, posx)
#validar inserciones y dejar fila en 0,0 1,0 2,0 3,0 4,0
    def validar_insertar_fila(self, node, nuevoNodo, nuevoX):
        aux = node
        while node is not None:
            sig = node.siguiente
            ant = node.anterior
            if sig is None:
                if ant is None:
                    self.insertar_en_fila_final(aux, nuevoNodo)
                    break
            if ant is None:
                if sig is not None:
                    auxMin = min(node.fil_x, nuevoX, sig.fil_x)
                    auxMax = max(node.fil_x, nuevoX, sig.fil_x)
                    if auxMax == sig.fil_x and auxMin == node.fil_x:
                        self.insertar_en_fila_antes(aux, sig.fil_x, nuevoNodo)
                        break

            if sig is None:
                if ant is not None:
                    auxMin = min(node.fil_x, nuevoX, ant.fil_x)
                    auxMax = max(node.fil_x, nuevoX, ant.fil_x)
                    if auxMax == nuevoX and auxMin == ant.fil_x:
                        self.insertar_en_fila_final(aux, nuevoNodo)
                        break

            if sig is not None:
                if ant is not None:
                    auxMin = min(node.fil_x, nuevoX, sig.fil_x)
                    auxMax = max(node.fil_x, nuevoX, sig.fil_x)
                    if auxMax == sig.fil_x and auxMin == node.fil_x:
                        self.insertar_en_fila_antes(aux, sig.fil_x, nuevoNodo)
                        break
            node = node.siguiente
#validar inserciones por columna y dejar en (0,0) (0,1) (0,2) (0,3) (0,4)
    def validar_insertar_columna(self, node, nuevoNodo, nuevoy):
        aux = node
        while node is not None:
            sig = node.abajo
            ant = node.arriba
            if sig is None:
                if ant is None:
                    self.insertar_en_columna_final(aux, nuevoNodo)
                    break
            if ant is None:
                if sig is not None:
                    auxMin = min(node.fil_y, nuevoy, sig.fil_y)
                    auxMax = max(node.fil_y, nuevoy, sig.fil_y)
                    if auxMax == sig.fil_y and auxMin == node.fil_y:
                        self.insertar_en_columna_antes(aux, sig.fil_y, nuevoNodo)
                        break

            if sig is None:
                if ant is not None:
                    auxMin = min(node.fil_y, nuevoy, ant.fil_y)
                    auxMax = max(node.fil_y, nuevoy, ant.fil_y)
                    if auxMax == nuevoy and auxMin == ant.fil_y:
                        self.insertar_en_columna_final(aux, nuevoNodo)
                        break

            if sig is not None:
                if ant is not None:
                    auxMin = min(node.fil_y, nuevoy, sig.fil_y)
                    auxMax = max(node.fil_y, nuevoy, sig.fil_y)
                    if auxMax == sig.fil_y and auxMin == node.fil_y:
                        self.insertar_en_columna_antes(aux, sig.fil_y, nuevoNodo)
                        break
            node = node.abajo
#************************************************************************************
#mostrar pos filas y columnas
    def mostrar_columna(self, posx, listaCabeza):
        listax = listaCabeza.cabX
        while listax is not None:
            #if (listax.fil_x == posx):
                #break
            aux = listax
            while aux is not None:
                print(aux.fil_x, aux.fil_y, aux.cont, "->", end="")
                aux = aux.abajo
            print("")
            listax = listax.siguiente

    def mostrar_fila(self, posy, listaCabeza):
        listay = listaCabeza.cabY
        while listay is not None:
            #if (listay.fil_y == posy):
                #break
            aux=listay
            while aux is not None:
                print(aux.fil_x, aux.fil_y, aux.cont, "->", end="")
                aux = aux.siguiente
            print("")
            listay = listay.abajo
        #while listay is not None:
        #    print(listay.fil_x,listay.fil_y,listay.cont,"->",end="")
        #    listay =listay.siguiente
        #print("")
#********************Inserciones******************************
    def insertar_en_fila_final(self, node, nuevo_nodo_cont):
        while node.siguiente is not None:
            node = node.siguiente
        node.siguiente = nuevo_nodo_cont
        nuevo_nodo_cont.anterior = node
        print("anterior<-[]->Null")

    def insertar_en_fila_antes(self, node, x, nuevo_nodo_cont):
        while node is not None:
            if node.fil_x == x:
                break
            node = node.siguiente
        nuevo_nodo_cont.siguiente = node
        nuevo_nodo_cont.anterior = node.anterior
        if node.anterior is not None:
            node.anterior.siguiente = nuevo_nodo_cont
        node.anterior = nuevo_nodo_cont
        print('caby<->[]<->[]<->[]->Null')
    def insertar_en_columna_final(self, node, nuevo_nodo_cont):

        while node.abajo is not None:
            node = node.abajo
        node.abajo = nuevo_nodo_cont
        nuevo_nodo_cont.arriba = node
        print("cabx")
        print("  |  ")
        print(" [] ")
        print("  |  ")
        print("Null")
    def insertar_en_columna_antes(self, node, y, nuevo_nodo_cont):
        while node is not None:
            if node.fil_y == y:
                break
            node = node.abajo
        nuevo_nodo_cont.abajo = node
        nuevo_nodo_cont.arriba = node.arriba
        if node.arriba is not None:
            node.arriba.abajo = nuevo_nodo_cont
        node.arriba = nuevo_nodo_cont
        print("cabx")
        print("  |  ")
        print(" [] ")
        print("  |  ")
        print(" [] ")
        print("  |  ")
        print(" Null")
    def report_graphiz(self,listaCabeza):
        Graph = "digraph L {" + "\n"
        Graph = Graph +"node [shape=box, color=cornflowerblue ];"+"\n"

        listax = listaCabeza.cabX
        listay = listaCabeza.cabY

        while listay  is not None:
            if listay.abajo is None:
                break
            Graph = Graph + '\"' + "(" + str(listay.fil_x) + "," + str(listay.fil_y) + ")" + "=" + listay.cont + '\"' + ";\n"
            Graph = Graph + '\"' + "(" + str(listay.fil_x) + "," + str(listay.fil_y) + ")" + "=" + listay.cont + '\"' + "->" + '\"' + "(" + str(listay.abajo.fil_x) + "," + str(listay.abajo.fil_y) + ")" + "=" + listay.abajo.cont + '\"' + ";\n"
            listay = listay.abajo

        while listax is not None:
            aux = listax
            while aux is not None:
                if aux.abajo is not None:
                    Graph = Graph +'\"'+"("+str(aux.fil_x)+","+str(aux.fil_y)+")"+"="+aux.cont+'\"'+";\n"
                    Graph = Graph + '\"'+"(" +str(aux.fil_x)+ "," +str(aux.fil_y)+ ")" + "=" + aux.cont + '\"' + "->" +'\"' + "(" +str(aux.abajo.fil_x)+","+str(aux.abajo.fil_y)+ ")" + "=" + aux.abajo.cont + '\"'+ ";\n"
                aux = aux.abajo

            listax = listax.siguiente


        listarankSameCaby = listaCabeza.cabY
        while listarankSameCaby is not None:

            if listarankSameCaby.siguiente is not None:
                Graph = Graph + "rank=same{\n"
                Graph = Graph + '\"' + "(" + str(listarankSameCaby.fil_x) + "," + str(listarankSameCaby.fil_y) + ")" + "=" + listarankSameCaby.cont + '\"' + "->" + '\"' + "(" + str(listarankSameCaby.siguiente.fil_x) + "," + str(listarankSameCaby.siguiente.fil_y) + ")" + "=" + listarankSameCaby.siguiente.cont + '\"' + ";\n"
                Graph = Graph + "} \n"
            #Graph = Graph + '\"' + "(" + str(listaCabeza.cabY.fil_x) + "," + str(listaCabeza.cabY.fil_y) + ")" + "=" + listaCabeza.cabY.cont + '\"' + "->" + '\"' + "(" + str(listaCabeza.cabY.siguiente.fil_x) + "," + str(listaCabeza.cabY.siguiente.fil_y) + ")" + "=" + listaCabeza.cabY.siguiente.cont + '\"' + ";\n"

            listarankSameCaby= listarankSameCaby.abajo

        listarankSameCab0 = listaCabeza.cabX
        while listarankSameCab0 is not None:
            auxRankSame = listarankSameCab0
            while auxRankSame is not None:

                if auxRankSame.siguiente is not None:
                    if auxRankSame.anterior is not None:
                        Graph = Graph + "rank=same{\n"
                        Graph = Graph + '\"'+"("+ str(auxRankSame.fil_x)+","+str(auxRankSame.fil_y)+")" + "=" +auxRankSame.cont+'\"'+"->"+'\"'+"("+str(auxRankSame.siguiente.fil_x)+","+str(auxRankSame.siguiente.fil_y)+")"+"="+auxRankSame.siguiente.cont + '\"' + ";\n"
                        Graph = Graph + '\"' + "(" + str(auxRankSame.fil_x) + "," + str(auxRankSame.fil_y) + ")" + "=" + auxRankSame.cont + '\"' + "->" + '\"' + "(" + str(auxRankSame.anterior.fil_x) + "," + str(auxRankSame.anterior.fil_y) + ")" + "=" + auxRankSame.anterior.cont + '\"' + ";\n"
                        Graph = Graph + "} \n"
                if auxRankSame.anterior is not None:
                    if auxRankSame.siguiente is None:
                        Graph = Graph + "rank=same{\n"
                        Graph = Graph + '\"' + "(" + str(auxRankSame.fil_x) + "," + str(auxRankSame.fil_y) + ")" + "=" + auxRankSame.cont + '\"' + "->" + '\"' + "(" + str(auxRankSame.anterior.fil_x) + "," + str(auxRankSame.anterior.fil_y) + ")" + "=" + auxRankSame.anterior.cont + '\"' + ";\n"
                        Graph = Graph + "} \n"

                auxRankSame = auxRankSame.abajo
            listarankSameCab0 = listarankSameCab0.siguiente


        Graph = Graph + "\n " + "}"
        print(Graph)
        nuevo_arch = open('Matriz.dot', 'w')
        nuevo_arch.write(Graph)
        nuevo_arch.seek(0)
        comando = "dot -Tpng Matriz.dot -o Matriz.png"
        os.system(comando)
        os.system("Matriz.png")