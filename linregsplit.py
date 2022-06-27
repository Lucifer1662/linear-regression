import numpy as np
import matplotlib.pyplot as plt
import math


def combination(c,phi,x):
    sum = 0
    for i in range(0, len(c)):
        sum += c[i]*phi[i](x)
    return sum

def main():
    x2 = [1,3,4]
    y2 = [5,5,5] 
    

    x1 = [1,3,2]
    y1 = [9,9,6]

    

    phi = [
        lambda x : 1,
        lambda x : x
    ]
    c = []
    for i in range(0,len(phi)):
        c.append(0)

    f = lambda x : combination(c,phi,x)
    
    X1 = []
    for xi in x1:
        xs = []
        for p in phi:
            xs.append(p(xi))

        X1.append(xs)

    X2 = []
    for xi in x2:
        xs = []
        for p in phi:
            xs.append(p(xi))

        X2.append(xs)
    
    Y1 = []
    for yi in y1:
        Y1.append([yi])

    Y2 = []
    for yi in y2:
        Y2.append([yi])


    X1 = np.matrix(X1)
    X2 = np.matrix(X2)
    Y1 = np.matrix(Y1)
    Y2 = np.matrix(Y2)
    
    X2T = np.transpose(X2)
    Y2T = np.transpose(Y2)
    inv = np.linalg.inv(2*X2T.dot(X1))

    
    cMat = inv.dot( X2T.dot(Y1) + np.transpose(Y2T.dot(X1)) )

    index = 0

    for i in range(0, cMat.shape[0]):
        c[i] = cMat.item((i,0))



    xc = []
    yc = []
    for i in range(1,6):
        xc.append(i)
        yc.append(f(i))


    plt.plot(x1, y1, 'ro')
    plt.plot(x2, y2, 'bo')
    plt.plot(xc, yc)
    plt.ylabel('some numbers')
    plt.show()



# y > mx + c
# Xc < Y
# c < X^-1Y



main()