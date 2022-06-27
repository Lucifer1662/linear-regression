import numpy as np
import matplotlib.pyplot as plt
import math


def combination(c,phi,x):
    sum = 0
    for i in range(0, len(c)):
        sum += c[i]*phi[i](x)
    return sum

def main():
    x = [1,3,4,-1]
    y = [2,4,3,-2] 

    

    phi = [
        lambda x : 1,
        lambda x : x,
        lambda x : x*x,
        lambda x : x*x*x
    ]
    c = []
    for i in range(0,len(phi)):
        c.append(0)

    f = lambda x : combination(c,phi,x)
    
    X = []
    for xi in x:
        xs = []
        for p in phi:
            xs.append(p(xi))

        X.append(xs)
    
    Y = []
    for yi in y:
        Y.append([yi])


    X = np.matrix(X)
    Y = np.matrix(Y)
    XT = np.transpose(X)
    inv = np.linalg.inv(XT.dot(X))
    
    cMat = inv.dot(XT).dot(y)
    index = 0

    for i in range(0, cMat.shape[1]):
        c[i] = cMat.item((0,i))


    x1 = []
    y1 = []
    for i in range(-1,6):
        x1.append(i)
        y1.append(f(i))

    plt.plot(x, y, 'ro')
    plt.plot(x1, y1)
    plt.ylabel('some numbers')
    plt.show()



# y > mx + c
# Xc < Y
# c < X^-1Y



main()