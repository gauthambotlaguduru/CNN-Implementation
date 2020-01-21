import numpy as np

def fcForward(weights, inputVolume):

    inputVector = np.reshape(inputVolume, (1, inputVolume.size))
    outputVector = inputVector.dot(weights)
    return outputVector

def fcWeightCorrection(errorVector, inputVector, weights):

    errorVector = np.array([errorVector])
    errorJacobian = np,=.matmul(errorVector, inputVector)
    weights = weights - learningRate*errorJacobian
    return weights

def fcErrorPropagation:

    errorVector = np.array([errorVector])
    return np.matmul(errorVector.T, weights.T)

def main():

    

    

    


