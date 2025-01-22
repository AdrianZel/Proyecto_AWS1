import xml.etree.ElementTree as ET

def convert_name(name_subelement) -> str:
    """
    Con esta función, unicamente nos aseguramos que no existan espacios en el nombre del subelemento.
    Si recibieramos id player, retornariamos id_player.
    Si fuera necesario podríamos utilizar expresiones regulares, para otros cambios.
    :param name_subelement el texto del subelemento
    :return retornamos el subelemento sin espacios y con _
    """
    return name_subelement.replace(" ", "_")

def generate_xml(datos,namenode, filename):
    filename = "reports/"+filename
    # print(filename)
    # print(datos)
    # print(len(datos))
    """
    Crear archivo XML por cada reporte demandado.

    :param nombre_archivo: Nombre del archivo XML a guardar. 
    :param datos: Lista de datos a recorrer
    :param namenode: Lista de nodos
    """
    # Crear el elemento raíz
    root = ET.Element("Resultados")

    for i in range(len(datos)):
        element = ET.SubElement(root, "Fila")
        for j in range(len(namenode)):
            #print("i {} - j {}- name {} - datos {} ".format(i, j,namenode[j], datos[i][j]))
            ET.SubElement(element,convert_name(namenode[j])).text = str(datos[i][j])

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    #print(f"XML guardado como {nombre_archivo}")
    # AÑADIR LOG INFO que se ha generado el archivo

