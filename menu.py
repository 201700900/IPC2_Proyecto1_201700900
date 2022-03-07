import cargar
import piso
import patron


PisoActual = piso.Piso('', 0, 0, 0, 0)
global PatronDestino
sPiso=0


def setNuevo():
    global PisoActual
    global sPiso
    try:
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
    except:
        print("Piso "+sPiso, " no encontrado")

    try:
        sPatron = input("Introduzca el número o el código de patrón inicial:\n")
        if sPatron.isdigit():
            PisoActual.Origen = PisoActual.patrones[int(sPatron)-1].rows
            PisoActual.cOrigen = PisoActual.patrones[int(sPatron)-1].codigo
            PisoActual.patrones[int(sPatron)-1].graficar(sPatron)
        else:
            for patron in PisoActual.patrones:
                if patron.codigo == sPatron:
                    PisoActual.Origen = patron.rows
                    patron.graficar(sPatron)
    except:
        print("Patrón "+sPatron, " no encontrado")

def ordenarPatrones():
    for piso in cargar.ListaPisos:
        for n in range(len(piso.patrones) - 1, 0, -1):
            for i in range(n):
                if piso.patrones[i].codigo > piso.patrones[i + 1].codigo:
                    temp = piso.patrones[i]
                    piso.patrones[i] = piso.patrones[i + 1]
                    piso.patrones[i + 1] = temp

def ordenarPisos():
    for n in range(len(cargar.ListaPisos) - 1, 0, -1):
        for i in range(n):
            if cargar.ListaPisos[i].nombre > cargar.ListaPisos[i + 1].nombre:
                temp = cargar.ListaPisos[i]
                cargar.ListaPisos[i] = cargar.ListaPisos[i + 1]
                cargar.ListaPisos[i + 1] = temp

def entrada():
    global PisoActual
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
    print ("4. Ordenar pisos cargados")
    print ("5. Salir")
    print("~~~~~~")
    print ("Elige una opcion")
    opcion = entrada()

    if opcion == 1:
        cargar.leer()
    elif opcion == 2:
        if cargar.ListaPisos.Size > 0 and PisoActual.nombre != "": 
            PisoActual.grafica(sPiso)
            p = 0
            PisoActual.gRows(PisoActual.Origen, "Patrón actual código: {}".format(PisoActual.cOrigen))

            op = input("Para seleccionar un nuevo Piso y Patrón Origen presione S\n")
            if op == 'S' or op == 's':
                setNuevo()
            
        elif cargar.ListaPisos.Size > 0 and PisoActual.nombre == "":
            n = 0
            for piso in cargar.ListaPisos:
                n += 1
                piso.grafica(n)
                p = 0
                for patron in piso.patrones:
                    p += 1
                    patron.graficar(p)
            setNuevo()
        else:
            pass
        
                    
    elif opcion == 3:
        PisoActual.grafica(sPiso)
        p=0
        for patron in PisoActual.patrones:
                p += 1
                patron.graficar(p)
        try:
            pNuevo = input("Seleciona el número o el código del patrón destino:\n")
            if pNuevo.isdigit():
                PatronDestino = PisoActual.patrones[int(pNuevo)-1].rows
                PisoActual.Destino = PisoActual.patrones[int(pNuevo)-1].rows
                PisoActual.cDestino = PisoActual.patrones[int(pNuevo)-1].codigo
            else:
                for patron in PisoActual.patrones:
                    if patron.codigo == pNuevo:
                        PatronDestino = patron.rows 
                        PisoActual.Destino = patron.rows 
            PisoActual.costo(PatronDestino)

            
        except:
            print("Patrón "+ pNuevo, " no encontrado")
    elif opcion == 4:
 
        ordenarPisos()
        ordenarPatrones()
        n=0
        for piso in cargar.ListaPisos:
                n += 1
                piso.grafica(n)
                p = 0
                for patron in piso.patrones:
                    p += 1
                    patron.graficar(p)
        
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")

print ("Fin")

entrada()