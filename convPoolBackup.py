'''
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 12, 13, 14, 15]])
b = np.ones((3, 3))
[r, c] = a.shape
padding = 1
stride = 2
A = np.zeros((r+2*padding, c+2*padding))
A[padding:r+padding, padding:c+padding] = a
[win, hin] = b.shape
wout = int((c - win + 2*padding)/stride + 1)
hout = int((r - hin + 2*padding)/stride + 1)
out = np.zeros((wout, hout))
q = int(hin/2)
for i in range(0, hout):
    p = int(win/2)
    for j in range(0, wout):
        out[i, j] = np.sum(np.multiply(A[q-int(hin/2):q+int(hin/2)+1, p-int(win/2):p+int(win/2)+1], b))
        p += stride
    q += stride
print(out)
'''
'''
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 12, 13, 14, 15]])
[r, c] = a.shape
stride = 2
pooled = np.zeros((int(r/2), int(c/2)))
p = 0
for i in range(0, r-1, stride):
    q = 0
    for j in range(0, c-1, stride):
        sub = a[i:i+2, j:j+2]
        pooled[p, q] = np.max(sub)
        q += 1
    p += 1
print(pooled)
'''                
