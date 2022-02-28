import xml.etree.ElementTree as ET
import lista
import piso
import patron



ListaPisos = lista.LinkedList()


def leer():
    global ListaPisos
    ListaPisos = lista.LinkedList()
    path = input("Introduzca la dirreción del XML:\n")
    try:
        tree = ET.parse('ejemplo.xml')
        root = tree.getroot()

        for y in range(0, len(root)):
            nombrePiso = root[y].attrib
            #print(nombrePiso['nombre'])
            R = int(root[y][0].text)
            C = int(root[y][1].text)
            F = int(root[y][2].text)
            S = int(root[y][3].text)
            #print(R, C, F, S)

            listaPatrones = lista.LinkedList()

            for patronXML in root[y].iter('patron'):

                codigoPatron = patronXML.attrib['codigo']
                #print(codigoPatron)
                BWPAtron = str(patronXML.text).strip()
                #print(BWPAtron)
                listaPatrones.Append(patron.Patron(str(codigoPatron), BWPAtron, C))

            ListaPisos.Append(piso.Piso(str(nombrePiso['nombre']), R, C, F, S, listaPatrones))

    except:
        print(path, " no encontrado")





