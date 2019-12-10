import numpy as np

# Dado los padres y sus hijos, devuelve a los que sobrevivieron a la seleccion
def getSupervivientes(listOfParents, listOfChilds):

    listOfParentsAndChilds = listOfParents + listOfChilds # Los padres ya tenian fitness asignado, y los hijos lo asigne recien
    
    competitors = np.random.randint(low=0, high=(len(listOfParentsAndChilds)), size=(5)) # tomo 5 elementos al azar

    posibbleSurvivors = []

    identifier = 0 # referencia al elemento actual
    for elem in listOfParentsAndChilds:
    	acumulatePoints = 0
    	for competitor in competitors:
    		if (elem.fitnessValue > listOfParentsAndChilds[competitor].fitnessValue):
    			acumulatePoints+=1
    	posibbleSurvivors.append((identifier,acumulatePoints))
    	acumulatePoints = 0 # reinicio el contador de puntos a 0
    	identifier+=1 # referencia al proximo elemento
    	competitors = np.random.randint(low=0, high=(len(listOfParentsAndChilds)), size=(5)) # elijo otros 5 sujetos al azar

    sortedPossibleSurvivors = sorted(posibbleSurvivors, key=lambda x: x[1])

    limitOfElite = len(listOfParents)*0.1
    limitOfElite = int(np.round(limitOfElite))

    survivors = sortedPossibleSurvivors[0:limitOfElite] # dejo en sobrevivientes a la elite que gano el torneo
    posibbleSurvivors = posibbleSurvivors[limitOfElite+1:] # mis nuevos posibles sobrevivientes son el resto

    theWorstGeneration = np.random.randint(low=0, high=len(posibbleSurvivors), size=(len(listOfParents)-limitOfElite)) # tomo un subconjunto al azar restante

    realSurvivors = []
    for s in survivors:
    	realSurvivors.append(listOfParentsAndChilds[s[0]])

    # estos son LISTOFPAIRS
    for i in theWorstGeneration: # asigno elementos random a la lista de sobrevivientes
    	realSurvivors.append(listOfParentsAndChilds[i])


    return realSurvivors

