products = {
    0:'potatoes',
    1:'tomatoes',
    2:'onions',
    3:'garlic'
}

def showDictionary(dictionary):
    for product in dictionary:
        print(f"{product} are {dictionary[product]}")
 
# showDictionary(products)
 
def findValue(dictionary, key):
    for product in dictionary:
        if key == product:
            print(f"{key} are {dictionary[product]}")

# findValue(products, 0)

def mergeDictionaries(dictionary1, dictionary2):
    dictionary3 = dictionary1.copy()
    dictionary3.update(dictionary2)
    print(dictionary3)

mergeDictionaries(products, products)
