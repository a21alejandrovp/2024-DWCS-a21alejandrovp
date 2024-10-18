# DECLARACIÓN DE VARIABLES
# ------------------------
age = 22
name = 'Alejandro'
pet = True
print(f'Hello my name is {name} and I am {age} years old.')
# print('Hello my name is {} and I am {} years old.'.format(name, age))

info = """I live in Santiago.
In my free time I play volleyball.
"""
print(info)


# CONDICIONAL IF
# --------------
# if age < 18:
#     print('You are younger than 18.')
# elif age == 18:
#     print('You are 18.')
# else:
#     print('You are older than 18.')


# FUNCIONES
# ---------
def petOwner(pet=False):
    if(pet == True):
        print('Alejandro, you have got a pet.')
    else:
        print('Alejandro, you haven´t got a pet.')

petOwner(pet)