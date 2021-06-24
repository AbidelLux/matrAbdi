class nodo_cabezeraY():
    def __init__(self,x,y,color):
        self.siguiente = None
        self.anterior = None
        self.arriba = None
        self.abajo = None
        self.fil_y = y
        self.fil_x = x
        self.cont = color