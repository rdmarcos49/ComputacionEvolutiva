import numpy as np

# Dado los padres y sus hijos, devuelve a los que sobrevivieron a la seleccion
def getSupervivientesTorneo(listOfParents, listOfChilds):

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

    
    limitOfElite = len(listOfParents)*0.1
    limitOfElite = int(np.round(limitOfElite))

    posibbleSurvivors.sort(key=lambda x: x[1])
    survivors = posibbleSurvivors[0:limitOfElite]
    theWorstElements = np.random.randint(low=limitOfElite, high=len(posibbleSurvivors), size=(len(listOfParents)-limitOfElite))
    for k in theWorstElements:
    	survivors.append(posibbleSurvivors[k])
    posibbleSurvivors.clear()
    for j in survivors:
    	posibbleSurvivors.append(listOfParentsAndChilds[j[0]])

    return posibbleSurvivors

def getSupervivientesElitismo(listOfParents, listOfChilds):
	listOfParentsAndChilds = listOfParents + listOfChilds

	listOfParentsAndChilds.sort(key=lambda x: x.fitnessValue)
	
	limitOfElite = len(listOfParents)*0.1
	limitOfElite = int(np.round(limitOfElite))

	survivors = listOfParentsAndChilds[0:limitOfElite]

	randomIndex = np.random.randint(low=limitOfElite+1, high=len(listOfParentsAndChilds), size=(len(listOfParents))-limitOfElite)
	for ri in randomIndex:
		survivors.append(listOfParentsAndChilds[ri])

	return survivors