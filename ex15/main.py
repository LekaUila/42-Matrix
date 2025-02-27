# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <lflandri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2025/02/04 22:04:13 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector, Complex
from mathUtils import sqrt



def __main__():

    u = Matrix([
    [1., 0.],
    [0., 1.],
    ])
    v = Vector([Complex(4., 2.), 2.])
    print(u * v)
    print(u.mulVec(v))
    # [4.]
    # [2.]
    u = Matrix([
    [2., 0.],
    [0., 2.],
    ])
    v = Vector([4., 2.])
    print(u * v)
    print(u.mulVec(v))
    # [8.]
    # [4.]
    u = Matrix([
    [2., -2.],
    [-2., 2.],
    ])
    v = Vector([4., 2.])
    print(u * v)
    print(u.mulVec(v))
    # [4.]
    # [-4.]
    v = Vector([Complex(2, -5), Complex(-48, -5)])
    print(v.normInf())
    #48.25971404805462
    v = Vector([-1.56, 0.6])
    print(v.normInf())
    #1.56
    u = Matrix([
    [1., 0.],
    [0., 1.],
    ])
    v = Matrix([
    [1., 0.],
    [0., 1.],
    ])
    print(u * v)
    print(u.mulMat(v))
    # [1., 0.]
    # [0., 1.]
    u = Matrix([
    [1., 0.],
    [0., 1.],
    ])
    v = Matrix([
    [2., 1.],
    [4., 2.],
    ])
    print(u * v)
    print(u.mulMat(v))
    # [2., 1.]
    # [4., 2.]
    u = Matrix([
    [3., -5.],
    [6., 8.],
    ])
    v = Matrix([
    [2., 1.],
    [4., 2.],
    ])
    print(u * v)
    print(u.mulMat(v))
    # [-14., -7.]
    # [44., 22.]
    
    u = Matrix([
    [2., 1.],
    [Complex(5.65, -8), -1.],
    [-3., Complex(9.9, 5.3)],
    ])
    v = Matrix([
    [-1., 0., 4.],
    [2., 1., 2.],
    ])
    print(u * v)
    print(u.mulMat(v))
    # [0., 1., 10.]
    # [-7., -1., 18.]
    # [9., 3., -36.]
    print(sqrt(Complex(3, 8)))
    
    print(Complex(3, 8) ** 0)
    print(Complex(3, 8) ** 1)
    print(Complex(3, 8) ** 2)
    print(Complex(3, 8) ** 3)
    
    
    return 0

if __name__ == '__main__':
    __main__()
    
    
#command to set format for proj file :  py main.py | sed s/'|'/''/g | sed s/'\['/''/g | sed s/'\]'/''/g  > /proj