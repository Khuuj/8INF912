""" hp: 0
        1-5
        6-10   
        11-15
        16-20
        21-25
        26-30
        30+
        """

""" armor:  1-5
            6-10
            10+
            """

""" num creatures friendly: 0,1,2,3,4,5,6,7 """

""" num creatures opponent: 0,1,2,3,4,5,6,7 """

import numpy as np

MATRIX_SIZE = 8*8*8

R = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
R *= -1

R[:,0] = 100
R[]

print(R)
