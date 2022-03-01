import lista
import graph


class Piso(): 
    
   
    def __init__(self, nombre, R, C, F, S, patrones = lista.LinkedList()):
        self.nombre = nombre
        self.R = R 
        self.C = C 
        self.F = F 
        self.S = S 
        self.patrones = patrones
        self.Origen = lista.LinkedList()
        self.cOrigen = ""
        self.Destino = lista.LinkedList()
        self.cDestino = ""
        self.precio = 0
        self.iter = 0 
        
    def __str__(self):
        String = "["+ self.nombre + ' ,'+ str(self.R) + ' ,' +  str(self.C) + ' ,'+  str(self.F) + ' ,'+  str(self.S) + ' ,'+  str(self.patrones) + str(self.Origen) + ']'
        return String

    def __iter__(self):
        return self

    def grafica(self, n):
        Tabla = """\
        +---------------------------------------------------------------------+
        |                         Piso {5}: {0:^2}                                                                                   
        |---------------------------------------------------------------------|
        |    Dimensión: {1:<1}X{2:<1}                                                                                                                        
        |    Costo voltear: ${3:<1}.00                                                             
        |    Costo intercambiar: ${4:<1}.00                                                
        +---------------------------------------------------------------------+\
        """
        Tabla = (Tabla.format(str(self.nombre), str(self.R), str(self.C), str(self.F), str(self.S), n))

        print(Tabla)

    def gRows(self,rows, texto):
        grafica = ''

        for fila in rows:
            
            for columna in fila:
                          
                if(columna =='B'):
                    grafica +='⬛'
                   
                elif(columna == 'W'):
                    grafica +='⬜'
                   
                else: 
                    pass
            
            grafica += '\n\t\t'    
        
        Tabla="""\
        |     {0}  
        |
        |       {1}
        +---------------------------------------------------------------------+\
        """

        Tabla = (Tabla.format(str(texto), str(grafica))) 
        print(Tabla)

    def igual(self, nuevo):
        for y in range(0, len(self.Origen)):
            for x in range(0, len(self.Origen[y])):
                if self.Origen[y][x] != nuevo[y][x]:
                    return False
        return True


    def costo(self, nuevo):
        self.iter = 0
        self.precio = 0
        graph.graph(self.Origen, 'patron-Origen')
        self.gRows(self.Origen, "Patrón inicial: ")
        self.gRows(nuevo, "Patrón destino: ")
        while (not self.igual(nuevo)):
            if self.F > self.S:
                self.cambiar(nuevo)
                self.cambiar(nuevo)
                self.voltear(nuevo)
                
            elif self.F == self.S:
                self.cambiar(nuevo)
                self.cambiar(nuevo)
                self.voltear(nuevo)
                
            elif self.F < self.S: 
                self.voltear(nuevo)
                self.voltear(nuevo)
                self.cambiar(nuevo)

        self.gRows(nuevo, "Por lo tanto, se necesitan ${0}.00 como mínimo para transformar el patrón inicial al patrón final.".format(self.precio))
        graph.graph(self.Destino, 'patron-Destino')
        self.cOrigen = self.cDestino
            
        
       
    def voltear(self, nuevo):
        for y in range(0, len(self.Origen)):
            for x in range(0, len(self.Origen[y])):
                if self.Origen[y][x] != nuevo[y][x]:
                    self.Origen[y][x] = nuevo[y][x]
                    self.iter+=1
                    self.gRows(self.Origen, "{3}. Se ha volteado ({0}, {1}), y costó: ${2}.00".format(y+1, x+1, self.F, self.iter))
                    self.precio+=self.F
                
        

    def cambiar(self, nuevo):
        for y in range(0, len(self.Origen)):
            
            for x in range(0, len(self.Origen[y])):

                if self.Origen[y][x+1] is not False and self.Origen[y][x] == nuevo[y][x+1] and self.Origen[y][x+1] != nuevo[y][x+1] and self.Origen[y][x] != nuevo[y][x]:
                    self.Origen[y][x] = nuevo[y][x]
                    self.iter+=1
                    self.Origen[y][x+1] = nuevo[y][x+1]
                    self.gRows(self.Origen, "{5}. Se ha intercambiado piso ({0}, {1}) por ({2}, {3}), y costó: ${4}.00".format(y+1, x+1, y+1, x+2, self.S, self.iter))
                    self.precio+=self.S 
            
                elif self.Origen[y+1] is not False and self.Origen[y][x] == nuevo[y+1][x] and self.Origen[y+1][x] != nuevo[y+1][x] and self.Origen[y][x] != nuevo[y][x]:
                    self.Origen[y][x] = nuevo[y][x]
                    self.iter+=1
                    self.Origen[y+1][x] = nuevo[y+1][x]
                    self.gRows(self.Origen, "{5}. Se ha intercambiado piso ({0}, {1}) por ({2}, {3}), y costó: ${4}.00".format(y+1, x+1, y+2, x+1, self.S, self.iter))
                    self.precio+=self.S

                elif self.Origen[y][x-1] is not False and self.Origen[y][x] == nuevo[y][x-1] and self.Origen[y][x-1] != nuevo[y][x-1] and self.Origen[y][x] != nuevo[y][x]:
                    self.Origen[y][x] = nuevo[y][x]
                    self.iter+=1
                    self.Origen[y][x-1] = nuevo[y][x-1]
                    self.gRows(self.Origen, "{5}. Se ha intercambiado piso ({0}, {1}) por ({2}, {3}), y costó: ${4}.00".format(y+1, x+1, y+1, x, self.S, self.iter))
                    self.precio+=self.S 

                elif self.Origen[y-1] is not False and self.Origen[y][x] == nuevo[y-1][x] and self.Origen[y-1][x] != nuevo[y-1][x] and self.Origen[y][x] != nuevo[y][x]:
                    self.Origen[y][x] = nuevo[y][x]
                    self.iter+=1
                    self.Origen[y-1][x] = nuevo[y-1][x]
                    self.gRows(self.Origen, "{5}. Se ha intercambiado piso ({0}, {1}) por ({2}, {3}), y costó: ${4}.00".format(y+1, x+1, y, x+1, self.S, self.iter))
                    self.precio+=self.S

                else:
                    if self.Origen[y][x] != nuevo[y][x]:
                        self.Origen[y][x] = nuevo[y][x]
                        self.iter+=1
                        self.gRows(self.Origen, "{3}. Se ha volteado ({0}, {1}), y costó: ${2}.00".format(y+1, x+1, self.F, self.iter))
                        self.precio+=self.F 
                    
                 
        
                    

        

