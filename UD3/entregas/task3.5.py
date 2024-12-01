# TASK 3.5 - WORKING WITH LISTS - TRIPLE CHECK FUNCTION
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

def tripleCheck(array):
    if type(array) != list:
        raise Exception("Tha parameter must be an array!")
    else:
        contador = 0
        i = 0
        array0 = array[0]
        for i in range(i, len(array)):
            if(array[i] == array0):
                contador += 1
                i += 1

                if(contador == 3):
                    return True
            else:
                array0 = array[i]
                contador = 0
                i += 1
        return False

try:
    print(tripleCheck([1, 1, 2, 2, 1 ]))
    print(tripleCheck([1, 1, 2, 1, 2, 3]))
    print(tripleCheck([1, 1, 1, 2, 2, 2, 1]))
except Exception as error:
    print(error)



# TASK 3.5 - WORKING WITH LISTS - COUNTRIES FUNCTION
# --------------------------------------------------
def countries(array):
    if type(array) != dict:
        raise Exception("The parameter must be an array!")
    else:
        for i in array:
            print(f'The capital of {i} is {array[i]}')
        
ceu = {
    "Italy": "Rome",
    "Luxembourg": "Luxembourg",
    "Belgium": "Brussels",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "France": "Paris",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Netherlands": "Amsterdam",
    "Portugal": "Lisbon",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "United Kingdom": "London",
    "Cyprus": "Nicosia",
    "Lithuania": "Vilnius",
    "Czech Republic": "Prague",
    "Estonia": "Tallinn",
    "Hungary": "Budapest",
    "Latvia": "Riga",
    "Malta": "Valetta",
    "Austria": "Vienna",
    "Poland": "Warsaw"
}

try:
    countries(ceu)
except Exception as error:
    print(error)