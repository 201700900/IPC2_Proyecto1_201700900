import list
import patron

class Piso(): 
  
    def __init__(self, nombre, R, C, F, S, patrones = list.LinkedList()):
        self.nombre = nombre
        self.R = R 
        self.C = C 
        self.F = F 
        self.S = S 
        self.patrones = patrones
        
    def __str__(self):
        String = "[ "+ self.nombre + ' ,'+ str(self.R) + ' ,' +  str(self.C) + ' ,'+  str(self.F) + ' ,'+  str(self.S) + ' ,'+  str(self.patrones) + ' ]'

        return String

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def grafica(self):
        Tabla = """\
        +---------------------------------------------------------------------+
        |                         Piso: {0:^2}                                                                                   
        |---------------------------------------------------------------------|
        |    Dimensión: {1:<1}X{2:<1}                                                                                                                        
        |    Costo voltear: ${3:<1}.00                                                             
        |    Costo intercambiar: ${4:<1}.00                                                
        +---------------------------------------------------------------------+\
        """
        Tabla = (Tabla.format(str(self.nombre), str(self.R), str(self.C), str(self.F), str(self.S)))

        print(Tabla)
       