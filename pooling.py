import numpy as np

maxLocations = []

def pooled(image, stride = 2):

    [r, c] = image.shape
    pooledSlice = np.zeros((int(r/2), int(c/2)))
    p = 0
    for i in range(0, r-1, stride):
        q = 0
        for j in range(0, c-1, stride):
            sub = image[i:i+2, j:j+2]
            m = int(np.max(sub))
            pooledSlice[p, q] = m
            Id = np.argwhere(sub == m)[0] + np.array([i, j])
            maxLocations.append(list(Id))
            q += 1
        p += 1
    return pooledSlice
    
def poolForward(inputVolume):

    [d, r, c] = inputVolume.shape
    outputVolume = np.zeros((d, int(r/2), int(c/2)))
    i = 0
    for slic in inputVolume:
        outputVolume[i, :, :] = pooled(slic)
        i += 1
    return outputVolume

def poolBackward(e):

    [d, r, c] = e.shape
    s = int((e.size)/d)
    out = np.zeros((d*2*r*2*c))
    e = list(e.flatten())
    slic = -1
    for i, j in zip(maxLocations, e):
        if (maxLocations.index(i)%s) == 0:
            slic += 1
        out[2*c*(i[0]) + i[1] + 2*d*s*slic] = j
    out = np.reshape(out, (d, 2*r, 2*c))
    return out

def main():
    a = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [25, 26, 27, 28]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24], [-1, -2, -3, -4]]])
    r = poolForward(a)
    r2 = poolBackward(r)
    
if __name__ == '__main__':
    main()
