# TASK 3.15 - PYTHON REVIEW - DICTIONARIES 2
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

import json

archivo = open('catalog.json', 'r')
catalog = json.load(archivo)

def mostrarCatalogo(catalog):
    try:
        print(json.dumps(catalog, indent=4))
    except:
        print("Ha habido un error al leer el archivo")

def mostrarTitulos(catalog):
    try:
        archivo = open('catalog.json', 'r')
        catalog = json.load(archivo)
        
        for book in catalog["catalog"]["book"]:
            print(book["title"])
    except:
        print("Ha habido un error al mostrar los títulos")

def findValue(catalog, id):
    error = 1

    try:
        for book in catalog["catalog"]["book"]:
            if book["id"] == id:
                print(book)
                error = 0
            
        if error != 0:
            raise ValueError(f"Ha habido un error al tratar de encontrar el libro con id {id}")
    except ValueError as e:
        print(e)

# mostrarCatalogo(catalog)
# mostrarTitulos(catalog)
# findValue(catalog, 2)