import matplotlib.pyplot as plt
import numpy as np
import sys

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
        self.fitnessValue = -1.0
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

# Funcion que le paso una lista de variables y desviaciones, devolviendome una lista de 
# igual longitud con los elementos mutados
def getMutatedElements(ListOfPairs):
    mutatedVariables = []
    mutatedDeviations = []
    for k in range(len(ListOfPairs.variables)):
        tempMutatedDeviation = "formula de mutacion de la desviacion"
        tempMutatedVariable = "formula de mutacion de la variable (usando la desviacion mutada)"
        mutatedVariables.append(tempMutatedVariable)
        mutatedDeviations.append(tempMutatedDeviation)
    result = ListOfPairs() # //todo chequear si puedo construirlo sin pasarle los parametros del constructor
    result.variables = mutatedVariables
    result.deviations = mutatedDeviations
    return result

# Me devuelve los hijos de mi generacion actual (pero no es la generacion siguiente)
def getChilds(listOfParents):
    listOfChilds = []
    for parent in listOfParents:
        listOfChilds.append(getMutatedElements(parent))
    return listOfChilds


# Funcion que me devuelve el fitness
def getAckleyResult(listOfVariables):

    # Valores recomendados, a = 20, b = 0.2, c = 2*pi

    a = 20
    b = 0.2
    c = 2 * np.pi

    # Primer sumatoria
    firstSum = 0
    for xi in listOfVariables: 
        firstSum += np.power(xi,2)

    firstSum = -b * np.sqrt((1/len(listOfVariables))*firstSum)

    # Segunda sumatoria
    secondSum = 0
    for xi in listOfVariables:
        secondSum += (np.cos(c*xi))

    secondSum = (1/len(listOfVariables)) * secondSum 

    resultOfAckleyFunction = - a * np.exp(firstSum) - np.exp(secondSum) + a + np.exp(1)

    return resultOfAckleyFunction

# Dado los padres y sus hijos, devuelve a los que sobrevivieron a la seleccion
def getSupervivientes(listOfParents, listOfChilds):
    listOfParentsAndChilds = listOfParents + listOfChilds

    for element in listOfParentsAndChilds: 
        element.fitnessValue = getAckleyResult(element.variables)

    # //todo filtrar supervivientes
    supervivientes = ["el 1° mejor","el 2° mejor", "...", "el 10° mejor", "resto elegido al azar"]
    return supervivientes

# Esta funcion devuelve la siguiente generacion
def getNextGeneration(oldGeneration):
    listOfChilds = getChilds(oldGeneration)
    listOfSupervivientes = getSupervivientes(oldGeneration, listOfChilds)
    return listOfSupervivientes

# Metodo que lleva a cabo el proceso evolutivo
def initRun(numberOfGenerations, sizeOfInitialPopulation, dimension):
    targetGeneration = initPopulation(sizeOfInitialPopulation, dimension) # Primera generacion
    for xi in range(numberOfGenerations):
        targetGeneration = getNextGeneration(targetGeneration)
    return targetGeneration



#################################

# Tomo los parametros y los paso de str a int

numberOfGenerations = int(sys.argv[1])
sizeOfInitialPopilation = int(sys.argv[2])
dimension = int(sys.argv[3])

print("num de generaciones: " + str(numberOfGenerations))
print("tamaño de poblacion inicial: " + str(sizeOfInitialPopilation))
print("numero de dimensiones: " + str(dimension))


firstGeneration = initPopulation(sizeOfInitialPopilation,dimension)
for i in firstGeneration:
    i.showContent()
