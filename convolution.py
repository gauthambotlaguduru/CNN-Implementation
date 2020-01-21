import numpy as np

def sliceConv(image, filt, padding = 0, stride = 1):

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

def convForward(inputVolume, filtVolume):

    for i in range(0, noOfFilters):
        filt = filtVolume[i, :, :, :]
        for filterSlice, imageSlice in zip(filt, inputVolume):
            outputSlice += sliceConv(imageSlice, filterSlice)
        outputVolume[i, :, :] = outputSlice
    return outputVolume

def errorPropagation(errorVolume, kernel, forwardPadding, forwardStride, backwardStride = 1):

    [d, r, c] = errorVolume.shape
    [h, w] = kernel.shape
    expectedW = (c - 1)*forwardStride - 2*forwardPadding + w
    expectedH = (r - 1)*forwardStride - 2*forwardPadding + h
    backwardPadding = int(((expectedW - 1)*backwardStride + w - c)/2)
    paddedError = np.zeros((d, r+2*padding, c+2*padding))
    paddedError[:, padding:r+padding, padding:c+padding] = errorVolume
    out = np.zeros((d, expectedW, expectedH))
    for i in range(0, noOfFilters):
        filt = filtVolume[i, :, :, :]
        for filterSlice, errorSlice in zip(filt, errorVolume):
            outputSlice += errorSliceConv(errorSlice, np.flip(np.flip(filterSlice, 1), 0))
        out[i, :, :] = outputSlice
    return out
    

def errorSliceConv(errorSlice, flippedKernelSlice, backwardStride, expectedW, expectedH):

    out = np.zeros((expectedW, expectedH))
    [w, h] = flippedKernel.shape
    q = int(h/2)
    for i in range(0, expectedH):
        p = int(w/2)
        for j in range(0, expectedW):
            out[i, j] = np.sum(np.multiply(errorSlice[q-int(h/2):q+int(h/2)+1, p-int(w/2):p+int(w/2)+1], flippedKernelSlice))
            p += backwardStride
        q += backwardStride

    return out

def weightErrors(errorVolume, inputVolume, forwardPadding, forwardStride):

    [de, re, ce] = errorVolume.shape
    [di, ri, ci] = inputVolume.shape
    fw = (ce - ci + 2*forwardPadding)/forwardStride + 1
    fh = (re - ri + 2*forwardPadding)/forwardStride + 1
    paddedInput = np.zeros((di, ri+2*forwardPadding, ci+2*forwardPadding))
    paddedInput[:, forwardPadding:ri+forwardPadding, forwardPadding:ci+forwardPadding] = inputVolume
    out = np.zeros((de, di, fw, fh))

    for errorSlice in errorVolume:
        i = np.argwhere(errorVolume == errorSlice)
        for inputSlice in inputVolume:
            j = np.argwhere(inputVolume == inputSlice)
            out[i, j, :, :] =  errorWeightConv(paddedInput, errorSlice, fw, fh)
    return out

def errorWeightConv(paddedInput, errorSlice, fw, fh):

    out = np.zeros((fw, fh))
    [w, h] = errorSlice.shape
    q = int(h/2)
    for i in range(0, fh):
        p = int(w/2)
        for j in range(0, fw):
            out[i, j] = np.sum(np.multiply(errorSlice[q-int(h/2):q+int(h/2)+1, p-int(w/2):p+int(w/2)+1], flippedKernelSlice))
            p += forwardStride
        q += forwardStride

    return out

      
def main():

    
