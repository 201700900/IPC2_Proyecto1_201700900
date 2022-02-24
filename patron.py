import lista

class Patron(): 
    
    def __init__(self, codigo, patron, C):
        self.codigo = codigo
        self.patron = str(patron)
        self.C = C
        self.rows = lista.LinkedList()

       
    def __str__(self):
        String = "| Patrón código: "+ str(self.codigo) + '| ' +  self.patron
        return String

    def __iter__(self):
        return self

    def graficar(self, n):
        grafica = ''
        r = 0
        self.rows = lista.LinkedList()
        fila = lista.LinkedList()
        for i in self.patron:
            r+=1
            if (r==self.C+1):
                grafica += '\n\t\t' 
                self.rows.Append(fila)
                fila = lista.LinkedList()
                r=1
            
            if(i =='B'):
                grafica +='⬛'
                fila.Append('B')
            elif(i == 'W'):
                grafica +='⬜'
                fila.Append('W')
            else: 
                pass

        self.rows.Append(fila)
        Tabla="""\
        |     Patrón {2}, código: {0}  
        |
        |       {1}
        |
        +---------------------------------------------------------------------+\
        """

        Tabla = (Tabla.format(str(self.codigo), str(grafica), n)) 
        print(Tabla)

    
    def gRows(self, n):
        grafica = ''

        for fila in self.rows:
            
            for columna in fila:
                          
                if(columna =='B'):
                    grafica +='⬛'
                   
                elif(columna == 'W'):
                    grafica +='⬜'
                   
                else: 
                    pass
            
            grafica += '\n\t\t'    
        
        Tabla="""\
        |     Patrón {2}, código: {0}  
        |
        |       {1}
        |
        +---------------------------------------------------------------------+\
        """

        Tabla = (Tabla.format(str(self.codigo), str(grafica), n)) 
        print(Tabla)

