import numpy as np
import cv2

class cnn:

    def __init__(self):

    def sliceConv(self, image, filt, padding = 0, stride = 1):

        [r, c] = image.shape
        paddedImage = np.zeros((r+2*padding, c+2*padding))
        paddedImage[padding:r+padding, padding:c+padding] = a
        [win, hin] = filt.shape
        wout = int((c - win + 2*padding)/stride + 1)
        hout = int((r - hin + 2*padding)/stride + 1)
        out = np.zeros((wout, hout))
        q = int(hin/2)
        for i in range(0, hout):
            p = int(win/2)
            for j in range(0, wout):
                out[i, j] = np.sum(np.multiply(paddedImage[q-int(hin/2):q+int(hin/2)+1, p-int(win/2):p+int(win/2)+1], filt))
                p += stride
            q += stride
        return out

    def convForward(self, inputVolume, filters):

        for i in range(0, noOfFilters):
            filt = filtVolume[i, :, :, :]
            for filterSlice, imageSlice in zip(filt, inputVolume):
                outputSlice += sliceConv(imageSlice, filterSlice)
            outputVolume[i, :, :] = outputSlice
            
    def pooled(self, image, stride = 2):

        [r, c] = image.shape
        pooledSlice = np.zeros((int(r/2), int(c/2)))
        p = 0
        for i in range(0, r-1, stride):
            q = 0
            for j in range(0, c-1, stride):
                sub = image[i:i+2, j:j+2]
                pooledSlice[p, q] = np.max(sub)
                q += 1
            p += 1
        return pooledSlice
    
    def poolForward(self):

        [d, r, c] = inputVolume.shape
        outputVolume = np.zeros((d, int(r/2), int(c/2)))
        i = 0
        for slic in inputVolume:
            outputVolume[i, :, :] = pooled(slic)
            i += 1
        return outputVolume

    def relu(self, volume):
        return volume.clip(0)

    def fcForward(self):
        return (inputVolume.reshape(1, inputVolume.size)[0])*fcWeight
        
    def softMax(self):
        return np.exp(inputVolume)/np.sum(np.exp(inputVolume))

    def trainingPrediction(self):
        return trainPredict[np.where(inputVolume == np.max(inputVolume))[0][0]] = 1
        
    def convBackward(self):

    def poolBackward(self):
        
    def fcBackward(self):

    def loss(self):
        return measuredOutputs - trueOutputs
        
    def train(self):

    def predict(self):





