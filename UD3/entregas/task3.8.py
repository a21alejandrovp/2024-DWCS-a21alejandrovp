# TASK 3.8 - ALIEN CLASS
#-----------------------
#-----------------------
#-----------------------
#-----------------------

class Alien:
    numberOfAliens = 0

    def __init__(self, name):
        self.name = name
        Alien.numberOfAliens += 1
    
    def getNumberOfAliens():
        return(f'Number of aliens: {Alien.numberOfAliens}')

paco = Alien('Paco')
pepe = Alien('Pepe')
ramon = Alien('Ramón')

print(Alien.getNumberOfAliens())