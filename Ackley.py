import numpy as np

def getAckleyResult(x):
    
    # Valores recomendados, a = 20, b = 0.2, c = 2*pi

    a = 20
    b = 0.2
    c = 2 * np.pi

    # Primer sumatoria
    firstSum = 0
    for xi in x: 
        firstSum += np.power(xi,2)

    firstSum = -b * np.sqrt((1/len(x))*firstSum)

    # Segunda sumatoria
    secondSum = 0
    for xi in x:
        secondSum += (np.cos(c*xi))

    secondSum = (1/len(x)) * secondSum 

    resultOfAckleyFunction = - a * np.exp(firstSum) - np.exp(secondSum) + a + np.exp(1)

    return resultOfAckleyFunction