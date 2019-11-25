import matplotlib.pyplot as plt
import numpy as np

# Minimo valor para el valor de entrada de la variable
minVariableValue = -32768

# Maximo valor para el valor de entrada de la variable
maxVariableValue = 32767

# Valor alfa para la mutacion
alpha = 0.2


class ListOfPairs():

    # Constructor de la clase
    # Inicializo las variables y desviaciones (aleatoriamente) de acuerdo a la dimension dada
    def __init__(self,dimension): # deberia ser variable global o constante, ya que la uso en otras funciones
        self.variables = []
        self.deviations = []
        for i in range(dimension):
            self.variables.append(np.random.randint(low=minVariableValue, high=maxVariableValue))
            self.deviations.append('{0:.5g}'.format(np.random.uniform(low=0.0, high=2.0)))

    # Muestra todas las variables
    def showVariables(self):
        for v in self.variables:
            print(v)

    # Muestra todas las desviaciones
    def showDeviations(self):
        for d in self.deviations:
            print(d)

    # Muestra todo el contenido en formato <X1,...,Xn> <D1,...,Dn>
    def showContent(self):
        string = "<"
        for v in self.variables:
            string+=str(v) + ", "
        string = string[:-2]
        string += "> <"

        for d in self.deviations:
            string+= str(d) +", "
        string = string[:-2]
        string += ">"
        print(string)

# Inicializo la poblacion, pasando el tamaño de la misma, y la dimension para ackley
def initPopulation(sizeOfInitialPopulation,dimension):
    firstGeneration = []
    for step in range(sizeOfInitialPopulation):
        listOfPair = ListOfPairs(dimension)
        firstGeneration.append(listOfPair)
    return firstGeneration

# Dado un valor x (o conjunto de valores xi) de entrada, obtengo el valor de la funcion evaluada
def getAckleyResult(xi):
    resultOfAckleyFunction = "aca se retornaria el resultado de la funcion de ackley"
    return resultOfAckleyFunction

# Prueba de los metodos
firstGeneration = initPopulation(10,5)
for fg in firstGeneration:
    fg.showContent()