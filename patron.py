class Patron(): 
    
    def __init__(self, codigo, patron, C):
        self.codigo = codigo
        self.patron = str(patron)
        self.C = C

    def __str__(self):
        String = "\n\n| Patrón código: "+ str(self.codigo) + '| \n\n' +  self.patron
        return String

    def __iter__(self):
        return self

    def graficar(self):
        grafica = ''
        
        
        r = 0
        for i in self.patron:
            r+=1
            if (r==self.C+1):
                grafica += '\n\t\t'
                r=1
            
            if(i =='B'):
                grafica +='⬛'
            elif(i == 'W'):
                grafica +='⬜'
            else: 
                pass

        Tabla="""\
        |     Patrón código: {0:<1}  
        |
        |       {1}
        |
        +---------------------------------------------------------------------+\
        """

        Tabla = (Tabla.format(str(self.codigo), str(grafica))) 
        print(Tabla)


