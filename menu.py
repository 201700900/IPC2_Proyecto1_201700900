import cargar
import piso
import patron

global PisoActual
global PatronDestino

def entrada():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:      
            print('Error, introduce un numero entero')

    return num

salir = False
opcion = 0

while not salir:

    print("------------------------------------------------------------------------------------------")
    print("Elija una opción.")
    print ("1. Cargar XML")
    print ("2. Mostrar Patron")
    print ("3. Seleccionar nuevo patron")
    print ("4. Mostrar pisos cargados")
    print ("5. Salir")
    print("~~~~~~")
    print ("Elige una opcion")
    opcion = entrada()

    if opcion == 1:
        cargar.leer()
    elif opcion == 2:
        n = 0
        for piso in cargar.ListaPisos:
            n += 1
            piso.grafica(n)
            p = 0
            for patron in piso.patrones:
                p += 1
                patron.graficar(p)
        
        sPiso = input("Seleciona el número o el nombre de piso especifico:\n")
        

        if sPiso.isdigit():
            PisoActual = cargar.ListaPisos[int(sPiso)-1]
        else:
            for piso in cargar.ListaPisos:
                if piso.nombre == sPiso:
                    PisoActual = piso
                else:
                    pass
        PisoActual.grafica(sPiso)
        p=0
        for patron in PisoActual.patrones:
                p += 1
                patron.graficar(p)
        sPatron = input("Introduzca el número o el código de patrón inicial:\n")
        if sPatron.isdigit():
            PisoActual.Origen = PisoActual.patrones[int(sPatron)-1].rows
            PisoActual.patrones[int(sPatron)-1].graficar(sPatron)
        else:
            for patron in PisoActual.patrones:
                if patron.codigo == sPatron:
                    PisoActual.Origen = patron.rows
                    patron.graficar(sPatron)

                    
    elif opcion == 3:
        PisoActual.grafica(sPiso)
        p=0
        for patron in PisoActual.patrones:
                p += 1
                patron.graficar(p)
        pNuevo = input("Seleciona el número o el código del patrón destino:\n")
        if pNuevo.isdigit():
            PatronDestino = PisoActual.patrones[int(pNuevo)-1].rows
            print(PatronDestino)
        else:
            for patron in PisoActual.patrones:
                if patron.codigo == pNuevo:
                    PatronDestino = patron.rows 
        PisoActual.costo(PatronDestino)
    elif opcion == 4:
        pass
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")

print ("Fin")

entrada()