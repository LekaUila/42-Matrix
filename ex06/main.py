# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 13:17:20 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Vector import Vector
from crossProduct import crossProduct




def __main__():
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print( crossProduct(u, v))
    # [0.]
    # [1.]
    # [0.]
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print( crossProduct(u, v))
    # [-3.]
    # [6.]
    # [-3.]
    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print( crossProduct(u, v))
    # [17.]
    # [-58.]
    # [-16.]

if __name__ == '__main__':
    __main__()