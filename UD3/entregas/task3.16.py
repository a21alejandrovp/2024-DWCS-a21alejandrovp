# TASK 3.16 - PYTHON REVIEW - CLASSES
# -----------------------------------
# -----------------------------------
# -----------------------------------
# -----------------------------------

class Person:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"Name: {self.name} --- Email: {self.email} --- Telephone: {self.telephone}"

class Product:
    def __init__(self, name, description, price, image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
    
    def __str__(self):
        return f"Name: {self.name} --- Description: {self.description} --- Price: {self.price} --- Image: {self.image}"
    
class Order:
    def __init__(self, date, productsList:Product, client:Person):
        self.date = date
        self.productsList = productsList
        self.client = client
    
    def getProducts(self):
        return "\n".join(str(product) for product in self.productsList)

    def getTotal(self):
        contador = 0
        for product in self.productsList:
            contador += float(product.price)
        return contador

    def __str__(self):
        return f"Date: {self.date}\n\nProducts List:\n{self.getProducts()}\n\nClient Info: {self.client}\n\nTotal: {self.getTotal()}"

apple = Product("Apple", "Reineta Granel Apple", "2.79", "Image")   
pear = Product("Pear", "Conferncia Pear", "2.29", "Image")
orange = Product("Orange", "Mesa Orange", "1.29", "Image")

client1 = Person("Alejandro", "a21alejandrovp@iessanclemente.net", 603425772)

productsList = []
productsList.append(apple)
productsList.append(pear)
productsList.append(orange)

order1 = Order("29-11-2024", productsList, client1)

print(order1)   
