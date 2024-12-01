# TASK 3.14 - PYTHON REVIEW - DICTIONARIES 1
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

products = {0: 'potatoes', 1: 'tomatoes', 3: 'onions', 4: 'garlic'}

def showDictionary(dictionary):
    print("Dictionary contents:")
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

def findValue(dictionary, key):
    if key in dictionary:
        print(f"The value for key {key} is '{dictionary[key]}'.")
    else:
        print(f"Key {key} not found in the dictionary.")

def mergeDictionaries(dictionary1, dictionary2):
    mergedDictionary = dictionary1.copy()
    offset = len(mergedDictionary)
    dictionary2Adjusted = {key + offset: value for key, value in dictionary2.items()}
    mergedDictionary.update(dictionary2Adjusted)
    return mergedDictionary

if __name__ == "__main__":
    print("Initial Dictionary:")
    showDictionary(products)

    products[5] = 'carrots'
    products[6] = 'peppers'
    print("\nDictionary after adding two products:")
    showDictionary(products)

    print("\nFinding value for key 3:")
    findValue(products, 3)

    newProducts = {0: 'lettuce', 1: 'cabbage', 2: 'spinach'}
    print("\nNew Dictionary to Merge:")
    showDictionary(newProducts)

    mergedProducts = mergeDictionaries(products, newProducts)
    print("\nMerged Dictionary:")
    showDictionary(mergedProducts)
