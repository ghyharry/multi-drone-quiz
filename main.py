import time
from result import *
import numpy as np


"""References
    ----------
    [1] "Distance Transforms of Sampled Functions"
        Pedro F. Felzenszwalb & Daniel P. Huttenlocher
        Theory of Computing (2012)
        https://www.theoryofcomputing.org/articles/v008a019/v008a019.pdf
    [2] Computer Vision Course
        Baraa Hassan
        https://github.com/baraaHassan/Computer_Vision_Course/tree/9b80306370cb985d3b8e02fdf9c99adf9115340d/Sheet02
"""




def edt1D(f):

    d = np.zeros(len(f)) 					
    k = 0                                   # Index of rightmost parabola in lower envelope
    v = np.zeros_like(f).astype(np.int32)   # Locations of parabolas in lower envelope
    z = np.zeros(len(f)+1)					# Locations of intersection of two parabolas

    z[0] = -1000000
    z[1] = 1000000


    for q in range(1, len(f)):
        s = ((f[q] + q * q) - (f[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k])

        while s <= z[k]:
            k -= 1
            s = ((f[q] + q * q) - (f[v[k]] + v[k] * v[k])) / (2 * q - 2 * v[k])

        k += 1
        v[k] = q
        z[k] = s
        z[k+1] = 1000000

    k = 0
    for q in range(len(f)):
        while z[k+1] < q:
            k+=1
        d[q] = (q - v[k])**2 + f[v[k]]
    return d

def edt2D(f):
    f *= 1000000

    d = np.zeros_like(f)
    for i in range(f.shape[1]):

        d[:, i] = edt1D(f[:, i])

    f = d

    d = np.zeros_like(f)
    for i in range(f.shape[0]):
        d[i, :] = edt1D(f[i, :])

    d = np.sqrt(d)

    return d

def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    grids = np.zeros((M, N))
    for i, j in obstacle_list:
        grids[i, j] = 1
    grids = 1-grids
    d = edt2D(grids)

    return d
    """res=[]
    for i in range(M):
        row=[]
        for j in range(N):
            min=100000
            for each in obstacle_list:
                d=np.linalg.norm(np.array([i,j])-each)
                if min>d:
                    min=d
            row.append(min)
        res.append(row)
    
    return res"""

if __name__ == '__main__':
    st = time.time()
    #assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)
