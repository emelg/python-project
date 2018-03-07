from numpy import random
from numpy import array
import numpy as np
from math import sqrt
x = 18
y = 18
z = 18
DCUT = 1.5

def gen(x, y, z, dcut = DCUT):
    dataset = []
    cutoff_distance = dcut 
    print "cutoff distance", cutoff_distance
    for i in xrange(10000):
        r1 = random.random() * x
        r2 = random.random() * y
        r3 = random.random() * z
        di = array([r1, r2, r3])
        passed = True
        
        for data in dataset:
            if np.linalg.norm(di - data) < cutoff_distance:
                passed = False
            else:
                pass

        if passed == True:
            dataset.append(di)
        else:
            pass

        if len(dataset) == 432:
            break
    return dataset

dataset =  gen(x,y,z)

with open("POSCAR_DATA", 'w') as f:
    f.write("FeZr\n")
    f.write("1.0\n")
    f.write("%d 0 0\n"%x)
    f.write("0 %d 0\n"%y)
    f.write("0 0 %d\n"%z)
    f.write("Fe Zr\n")
    f.write(" 368 64\n")
    f.write("Direct\n")

    for data in dataset:
        f.write("%f %f %f\n"%(data[0]/float(x), data[1]/float(y), data[2]/float(z)))
