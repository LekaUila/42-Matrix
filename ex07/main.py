# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 14:58:26 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector




def __main__():
    u = Matrix([
    [1., 0.],
    [0., 1.],
    ])
    v = Vector([4., 2.])
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
    [5., -1.],
    [-3., 3.],
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
    
    return 0

if __name__ == '__main__':
    __main__()