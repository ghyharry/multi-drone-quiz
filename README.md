# multi-drone-quiz
In main.py, we strictly implement the distance transformations of Euclidean distances in a 2d binary grid according to the algorithm proposed by Distance Transforms of Sampled Functions.

It is too time consuming to calculate the l2 norm for each grid respect to each obstacle using the conventional method, and opencv can't achieve the required accuracy. So we used the parabolic lower envelope method shown in the article. It has O(M*N) time complexity, which has been proved in the article. We can save further time if we use gpu parallel computing. (But I didn't use it in main.py because of my personal ability and time constraints)

esdf() first builds a 2d binary grid based on M,N and the positions of obstacles, and passes the 1-grid into the edt2D() method.

In edt2D(), two dimensional transform is computed by first performing one dimensional transforms (edt1d()) along each column of the grid, and then performing one dimensional transforms along each row of the result.

In edt1D(), we first compute the lower envelope of the n parabolas, then fill in the values of Df (p) by checking the height of the lower envelope at each grid location p.

References

Distance Transforms of Sampled Functions
Pedro F. Felzenszwalb Daniel P. Huttenlocher
http://people.cs.uchicago.edu/~pff/papers/dt.pdf

Parallel computing of signed distance function in level set based on dimension reduction
http://www.cjig.cn/html/jig/2018/2/20180203.htm#abstract_EN

Computer_Vision_Course Sheet02
Baraa Hassan
https://github.com/baraaHassan/Computer_Vision_Course/tree/9b80306370cb985d3b8e02fdf9c99adf9115340d/Sheet02