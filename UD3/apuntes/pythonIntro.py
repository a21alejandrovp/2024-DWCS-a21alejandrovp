# DECLARACIÓN DE VARIABLES
# ------------------------
# age = 22
# name = 'Alejandro'
# pet = True
# print(f'Hello my name is {name} and I am {age} years old.')
# print('Hello my name is {} and I am {} years old.'.format(name, age))

# info = """I live in Santiago.
# In my free time I play volleyball.
# """
# print(info)



# ARRAYS
# ------
# posiciones = ["Central", "Líbero", "Receptor", "Opuesto", "Lateral Izquierdo"]
# posiciones.insert(0, "Colocador")
# del(posiciones[5])
# print(posiciones)



# DICCIONARIOS
# ------------
# numerosDePosiciones = {"Colocador": 1, "Opuesto": 2, "Central": 3, "Receptor1": 4, "Líbero": 5}
# numerosDePosiciones["Receptor2"] = 6
# print(numerosDePosiciones)



# CONDICIONAL IF
# --------------
# if age < 18:
#     print('You are younger than 18.')
# elif age == 18:
#     print('You are 18.')
# else:
#     print('You are older than 18.')



# BUCLE FOR
# ---------
# for posicion in posiciones:
#     print(posicion)

# for x in range(1, 10):
#     print(x)



# FUNCIONES
# ---------
# def petOwner(pet=False):
#     if(pet == True):
#         print('Alejandro, you have got a pet.')
#     else:
#         print('Alejandro, you haven´t got a pet.')

# petOwner(pet)



# CLASSES
# -------
# class Jugador:
#     nombre = 'Alejandro'
#     edad = 22
#     equipo = "CV Noia"
#     posicion = 'Central'
#     def presentacion(self):
#         print(f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años y juego de {self.posicion} en el {self.equipo}')

# yo = Jugador()
# print(yo.presentacion())