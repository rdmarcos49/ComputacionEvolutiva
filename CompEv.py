from Writer import *
from Ackley import *
from Filtro import *

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from datetime import datetime
import os

# Minimo valor para el valor de entrada de la variable
minVariableValue = -32768

# Maximo valor para el valor de entrada de la variable
maxVariableValue = 32767

# Valor alfa para la mutacion
alpha = 0.2

elitePercent = 0.1


class ListOfPairs():

    # Constructor de la clase
    # Inicializo las variables y desviaciones (aleatoriamente) de acuerdo a la dimension dada
    def __init__(self,dimension): # deberia ser variable global o constante, ya que la uso en otras funciones
        self.variables = []
        self.deviations = []
        self.fitnessValue = -1.0
        for i in range(dimension):
            self.variables.append(np.random.randint(low=minVariableValue, high=maxVariableValue))
            self.deviations.append('{0:.5g}'.format(np.random.uniform(low=1.0, high=2.0)))

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

def getAllAvgOfRun(listaDeTuplas): # por convencion el avg esta en listaDeTuplas[2]
    allAvgOfRun = []
    for tupla in listaDeTuplas:
        allAvgOfRun.append(tupla[2])
    return allAvgOfRun

# Inicializo la poblacion, pasando el tamaño de la misma, y la dimension para ackley
def initPopulation(sizeOfInitialPopulation,dimension):
    firstGeneration = []
    for step in range(sizeOfInitialPopulation):
        listOfPair = ListOfPairs(dimension)
        firstGeneration.append(listOfPair)
    return firstGeneration

def initOptimazedPopulation(sizeOfInitialPopulation,dimension):
    initPopulation = []
    for j in range(sizeOfInitialPopulation):
        variables = []
        temp = ListOfPairs(dimension)
        for i in range(dimension):
            variables.append(np.random.randint(low=-45, high=45))
        temp.variables = variables
        initPopulation.append(temp)
    return initPopulation

# Funcion que le paso una lista de variables y desviaciones, devolviendome una lista de 
# igual longitud con los elementos mutados
def getMutatedElements(listOfPairs):
    mutatedVariables = []
    mutatedDeviations = []
    for k in range(len(listOfPairs.variables)):
        tempMutatedDeviation = (float(listOfPairs.deviations[k])*(1+alpha*(np.random.normal(0,1))))
        tempMutatedVariable = (listOfPairs.variables[k]+tempMutatedDeviation*(np.random.normal(0,1)))
        if((tempMutatedVariable > maxVariableValue) or (tempMutatedVariable < minVariableValue)):
            tempMutatedVariable = np.random.randint(low=minVariableValue, high=maxVariableValue)
        mutatedVariables.append(tempMutatedVariable)
        mutatedDeviations.append(tempMutatedDeviation)
    instanceOfListOfPairs = ListOfPairs(dimension)
    instanceOfListOfPairs.variables = mutatedVariables
    instanceOfListOfPairs.deviations = mutatedDeviations
    return instanceOfListOfPairs

# Me devuelve los hijos de mi generacion actual (pero no es la generacion siguiente)
def getChilds(listOfParents):
    listOfChilds = []
    for parent in listOfParents:
        listOfChilds.append(getMutatedElements(parent))
    return listOfChilds



# Esta funcion devuelve la siguiente generacion
def getNextGeneration(oldGeneration):
    listOfChilds = getChilds(oldGeneration)

    # Le asigno un valor de fitness a cada hijo
    for element in listOfChilds: 
        element.fitnessValue = getAckleyResult(element.variables)

    listOfSupervivientes = []
    if (filtroSeleccionado==1):
        listOfSupervivientes = getSupervivientesTorneo(oldGeneration, listOfChilds)
    else:
        listOfSupervivientes = getSupervivientesElitismo(oldGeneration, listOfChilds)
    return listOfSupervivientes

# Metodo que lleva a cabo el proceso evolutivo
def initRun(path, numberOfRun,numberOfGenerations, sizeOfInitialPopulation, dimension):
    targetGeneration = []    

    if(metodoInicial == 1):
        targetGeneration = initOptimazedPopulation(sizeOfInitialPopulation,dimension)
    else:
        targetGeneration = initPopulation(sizeOfInitialPopulation, dimension)

    fileRunName = "Run" + str(numberOfRun)

    # crear archivo
    file = open(path + "/"+ fileRunName +".txt", "w") 


    # Le inicializo el fitness a la primera generacion
    for elem in targetGeneration:
        elem.fitnessValue = getAckleyResult(elem.variables)


    listaDeDatos = []
    listaDeDatos.append(getTupleValues(targetGeneration))

    hardcodedFlag = 0

    minFitnessOfRun = 0
    maxFitnessOfRun = 0
    avgFitnessOfRun = 0

    for tuples in listaDeDatos:
        minFitnessOfRun = tuples[0]
        maxFitnessOfRun = tuples[1]
        avgFitnessOfRun = tuples[2]
        if(hardcodedFlag > 0):
            break
        hardcodedFlag+=1

        minVariablesRun = targetGeneration[0].variables
        maxVariablesRun = targetGeneration[0].variables

    count = 0
    # Corro el algoritmo tantas veces como generaciones me hayan asignado
    for xi in range(numberOfGenerations):
        targetGeneration = getNextGeneration(targetGeneration)
        tempTuple = getTupleValues(targetGeneration)
        listaDeDatos.append(tempTuple)
        if(tempTuple[0] < minFitnessOfRun):
            minFitnessOfRun = tempTuple[0]
            minVariablesRun = tempTuple[3]
        if(tempTuple[1] > maxFitnessOfRun):
            maxFitnessOfRun = tempTuple[1]
            maxVariablesRun = tempTuple[4]
        avgFitnessOfRun+=tempTuple[2]
    avgFitnessOfRun = avgFitnessOfRun / numberOfGenerations
    count+=1
    if (count % 500 == 0):
        collect()

    listaDeAvg = getAllAvgOfRun(listaDeDatos)

    documentateHeader(file, minFitnessOfRun, maxFitnessOfRun, avgFitnessOfRun, minVariablesRun, maxVariablesRun)
    documentateBody(file, listaDeDatos)
    documentatePlots(path,numberOfRun,listaDeAvg)
    
    file.close()

    return targetGeneration

def getTupleValues(actualGeneration):
    minValue = actualGeneration[0].fitnessValue
    maxValue = actualGeneration[0].fitnessValue
    avgValue = 0
    minVariables = []
    maxVariables = []

    for elem in actualGeneration:
        if(elem.fitnessValue <= minValue):
            minValue=elem.fitnessValue
            minVariables = elem.variables
        if(elem.fitnessValue >= maxValue):
            maxValue=elem.fitnessValue
            maxVariables=elem.variables
        avgValue += elem.fitnessValue
    avgValue = avgValue / (len(actualGeneration))
    temp = (minValue, maxValue, avgValue,minVariables,maxVariables)
    return temp


    

def main(numberOfRuns):
    tempDate = datetime.now()
    path = tempDate.strftime("%d/%m/%Y %H:%M:%S")
    path = path.replace("/","-")
    path = path.replace(":",".")
    os.mkdir(path)
    fileRunName = "Especificaciones de las corridas"
    fileSetup = open(path + "/"+ fileRunName +".txt", "w") 
    documentateSetup(fileSetup, numberOfRuns, sizeOfInitialPopulation, numberOfGenerations, dimension, metodoInicial, filtroSeleccionado)
    fileSetup.close()
    count = 1
    for i in range(numberOfRuns):
        initRun(path, count, numberOfGenerations, sizeOfInitialPopulation, dimension)
        count+=1


#################################################################

raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroRuns = Entry(miFrame)
cuadroRuns.focus_set()
cuadroRuns.grid(row=0, column=1, pady=4)

cuadroGeneration = Entry(miFrame)
cuadroGeneration.focus_set()
cuadroGeneration.grid(row=1, column=1, pady=4)

cuadroPoblacion = Entry(miFrame)
cuadroPoblacion.focus_set()
cuadroPoblacion.grid(row=2, column=1, pady=4)

cuadroDimension = Entry(miFrame)
cuadroDimension.focus_set()
cuadroDimension.grid(row=3, column=1, pady=4)

runsLabel = Label(miFrame, text="Number of runs:")
runsLabel.grid(row=0, column=0, sticky="ne", pady=4)

generationLabel = Label(miFrame, text="Number of generations:")
generationLabel.grid(row=1, column=0, sticky="ne", pady=4)

poblacionLabel = Label(miFrame, text="Population size:")
poblacionLabel.grid(row=2, column=0, sticky="ne", pady=4)

dimensionLabel = Label(miFrame, text="Dimention")
dimensionLabel.grid(row=3, column=0, sticky="ne", pady=4)


varOpcionMetodoInicial = IntVar()
Radiobutton(raiz,text='Utilizar valores optimizados',variable=varOpcionMetodoInicial,value=1).pack()
Radiobutton(raiz,text='Utilizar valores optimizados',variable=varOpcionMetodoInicial,value=1).select()
Radiobutton(raiz,text='Utilizar valores totalmente estocasticos',variable=varOpcionMetodoInicial,value=2).pack()

varOpcionfiltroSeleccionado = IntVar()
Radiobutton(raiz,text='Utilizar torneo - presion selectiva',variable=varOpcionfiltroSeleccionado,value=1).pack()
Radiobutton(raiz,text='Utilizar torneo - presion selectiva',variable=varOpcionfiltroSeleccionado,value=1).select()
Radiobutton(raiz,text='Utilizar metodo de seleccion elitista',variable=varOpcionfiltroSeleccionado,value=2).pack()

inicialLabel = Label(miFrame, text = 'Valores iniciales:')
inicialLabel.grid(row=4,column=0,sticky='w',pady=4)

filtroLabel = Label(miFrame, text = 'Metodo de seleccion de supervivientes:')
filtroLabel.grid(row=5,column=0,sticky='w',pady=4)


def codeButtonRun():
    global numberOfRuns
    global numberOfGenerations
    global sizeOfInitialPopulation
    global dimension
    global metodoInicial
    global filtroSeleccionado
    numberOfRunsx = cuadroRuns.get()
    sizeOfInitialPopulationx = cuadroPoblacion.get()
    numberOfGenerationsx = cuadroGeneration.get()
    dimensionx = cuadroDimension.get()

    metodoInicial=int(varOpcionMetodoInicial.get())
    filtroSeleccionado = int(varOpcionfiltroSeleccionado.get())
    numberOfRuns = int(numberOfRunsx)
    sizeOfInitialPopulation = int(sizeOfInitialPopulationx)
    numberOfGenerations = int(numberOfGenerationsx)
    dimension = int(dimensionx)
    close_window()
    main(numberOfRuns)
    

botonRun = Button(raiz, text="Run!", pady=2, padx=2, command=codeButtonRun)

botonRun.pack()

numberOfRuns = 0
numberOfGenerations = 0
sizeOfInitialPopulation = 0
dimension = 0
metodoInicial = 1
filtroSeleccionado = 1

def close_window(): 
    raiz.destroy()

raiz.mainloop()


'''
numberOfRuns = 1
numberOfGenerations = 100
sizeOfInitialPopulation = 120
dimension = 5
'''

#main(numberOfRuns)
