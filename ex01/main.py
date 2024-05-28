# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/28 17:37:51 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector
from linearCombination import linearCombination




def __main__():
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    print( linearCombination([e1, e2, e3], [10., -2., 0.5]))
    m = Matrix(lenth=3)
    m[0] = e1
    m[1] = e2
    m[2] = e3
    v = Vector([10., -2., 0.5])
    print( linearCombination(m, v))
    # [10.]
    # [-2.]
    # [0.5]
    print( linearCombination([v1, v2], [10., -2.]))
    m = Matrix(lenth=2)
    m[0] = v1
    m[1] = v2
    v = Vector( [10., -2.])
    print( linearCombination(m, v))
    # [10.]
    # [0.]
    # [230.]
    return 0

if __name__ == '__main__':
    __main__()