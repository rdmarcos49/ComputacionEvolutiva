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