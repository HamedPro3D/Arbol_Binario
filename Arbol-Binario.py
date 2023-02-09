
class Arbol:
    print("Arboles Binarios")
    #Iniciando el nodo de los arboles binarios
    def __init__(self,arbol,dato):
        self.derecha = None
        self.izquierda = None
        self.info = dato
    #Metodo para agregar los datos dentro de los nodos
    def agregar(self,arbol,dato):
        if arbol.info > dato:
            self.agregarIzquierda(arbol,dato)
        elif arbol.info < dato:
            self.agregarDerecha(arbol,dato)
    #Creacion de las ramas y nodo de la izquierda
    def agregarIzquierda(self,arbol,dato):
        if arbol.izquierda == None:
            arbol.izquierda = Arbol(arbol,dato)
        else:
            self.agregar(arbol.izquierda,dato)
    #Creacion de las ramas y nodo de la derecha
    def agregarDerecha(self,arbol,dato):
        if arbol.derecha == None:
            arbol.derecha = Arbol(arbol,dato)
        else:
            self.agregar(arbol.derecha,dato)
    def buscar(self,arbol,dato):
        if arbol.info != None:
            if arbol.info < dato:
                self.agregarIzquierda(arbol,dato)
            print(arbol.info)
            if arbol.info == dato:
                print("El dato: ",dato," se encontro")
            else:
                print("El dato: ",dato," No se encontro")
                print(arbol.info)
        else:
            print ("El arbol esta vacio")
    #Metodo de recorrer el arbol (PreOrden)
    def preOrden(self,arbol):
        print(arbol.info,end=" -> ")
        if arbol.izquierda != None:
            self.preoIzquierda(arbol)
        if arbol.derecha != None:
            self.preoDerecha(arbol)
    #Ver sí hay algo a la izquierda 
    def preoIzquierda(self,arbol):
        self.preOrden(arbol.izquierda)
    #Ver sí hay algo a la derecha 
    def preoDerecha(self,arbol):
        self.preOrden(arbol.derecha)
    #Metodo de recorrer el arbol (InOrden)
    def InOrden(self,arbol):
        if arbol.izquierda != None:
            self.inoIzquierda(arbol)
        print(arbol.info,end=" -> ")
        if arbol.derecha != None:
            self.inoDerecha(arbol)
    #Ver sí hay algo a la izquierda
    def inoIzquierda(self,arbol):
        self.InOrden(arbol.izquierda)
    #Ver sí hay algo a la derecha
    def inoDerecha(self,arbol):
        self.InOrden(arbol.derecha)
    #Metodo de recorrer el arbol (PostOrden)
    def PostOrden(self,arbol):
        if arbol.izquierda != None:
            self.posIzquierda(arbol)
        if arbol.derecha != None:
            self.posDerecha(arbol)
        print(arbol.info,end=" -> ")
    #Ver sí hay algo a la izquierda
    def posIzquierda(self,arbol):
        self.PostOrden(arbol.izquierda)
    #Ver sí hay algo a la derecha
    def posDerecha(self,arbol):
        self.PostOrden(arbol.derecha)
    

#Creacion del objeto arbol
#En este casó la palabra arbol es la referencia para buscar la formacion del arbol, desde que padre tomara el camino.
#Primer Nodo del arbol (Padre)
arbol = Arbol(None,10)
#Nodos seguidos (Hijos)
#Primer sub-arbol
arbol.agregar(arbol,8)
arbol.agregar(arbol,2)
arbol.agregar(arbol,9)
#segundo sub-arbol
arbol.agregar(arbol,12)
arbol.agregar(arbol,11)
arbol.agregar(arbol,15)
#Recorrido "PreOrden"
# Root <- ->
print("PreOrden")
arbol.preOrden(arbol)
print(" ")
#Recorrido "PostOrden"
# <- -> Root
print("PostOrden")
arbol.PostOrden(arbol)
print(" ")
#Recorrido "InOrden"
# <- Root ->
print("InOrden")
arbol.InOrden(arbol)
print(" ")
print("Buscar")
arbol.buscar(arbol,10)
