# Minimo valor para el valor de entra de la variable
minVariableValue = -32768

# Maximo valor para el valor de entra de la variable
maxVariableValue = 32767

# Valor alfa para la mutacion
alpha = 0.2

# Clase tupla para almacenar posteriormente en un arreglo
class Pair():

    # Constructor de la clase
    def Pair(self, variable, desviacion):
        self.variable = variable
        self.deviation = desviacion

    # Getter de la variable
    def getVariable(self):
        return variable

    # Getter de la desviacion asociada a la variable
    def getDesviacion(self):
        return deviation

# Metodo que devuelve una lista con el tamaño definido por parametro,
# con valores inicializados al azar
def initPoblation(sizeOfInitialPoblation):
    initialPoblation = [sizeOfInitialPoblation]
    for x in initialPoblation:
        newPair = Pair() # Falta pasar como parametros valores al azar
        initialPoblation.append(newPair)
    return initialPoblation

# Esta funcion devuleve una lista de los hijos de los padres de la generacion
# anterior, en una lista de la misma longitud que la pasada por parametro
def getMutatePoblation(myListOfParents):
    childs = []
    for actualParent in myListOfParents:
        print("mutar los valores del padre actual, y asignarlos al hijo")
        childs.append("par mutado del padre")
    return childs

print("hola mundo")