from matplotlib import pyplot as plt

def documentateHeader(fileText,minFitnessValue,maxFitnessValue,avgFitnessValue):
	fileText.write("# Menor fitness conseguido: " + str(minFitnessValue) + "\n")
	fileText.write("# Mayor fitness conseguido: " + str(maxFitnessValue) + "\n")
	fileText.write("# Promedio de fitness total conseguido: " + str(avgFitnessValue) + "\n")
	fileText.write("\n")

def documentateBody(fileText,listaDeDatos): # Teoricamente, la lista de datos deberia contener tuplas de min, max y avg fitness
    i=0
    for elem in listaDeDatos:
        lineValue = "Fitness de generacion n°"+ str(i) + ": [min fitness: "+str(elem[0])+", max fitness: "+str(elem[1])+", avg fitness "+str(elem[2])+"]\n"
        fileText.write(lineValue)
        i+=1

def documentatePlots(path, numberOfRun, x):
	plt.plot(x)
	plt.xlabel('Generations')
	plt.ylabel('Fitness value')
	plt.savefig(path + '/Run_'+ str(numberOfRun) +'_avgFitness.png', bbox_inches='tight')
	plt.close()

def documentateSetup(fileText,numberOfRuns,sizeOfInitialPopulation,numberOfGenerations,dimension, metodoInicial):
	fileText.write("Numero de corridas: " + str(numberOfRuns) + "\n")
	fileText.write("Numero de generacion por corrida: " + str(numberOfGenerations) + "\n")
	fileText.write("Tamaño de la poblacion inicial: " + str(sizeOfInitialPopulation) + "\n")
	fileText.write("Dimension: " + str(dimension) + "\n")
	fileText.write("\n")
	if (metodoInicial==1):
		fileText.write("La corrida se inicializo con valores optimos para acelerar la convergencia")
	else:
		fileText.write("La corrida fue inicializada con valores totalmente aleatorios")
