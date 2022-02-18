import cargar

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
        for piso in cargar.ListaPisos:
            piso.grafica()
            
            for patron in piso.patrones:
                patron.graficar()
                    
    elif opcion == 3:
        
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")

print ("Fin")

entrada()