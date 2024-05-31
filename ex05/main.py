# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 12:54:57 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Vector import Vector
from angleCos import angleCos




def __main__():
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print( angleCos(u, v))
    # 1.0
    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print( angleCos(u, v))
    # 0.0
    u = Vector([-1., 1.])
    v = Vector([ 1., -1.])
    print( angleCos(u, v))
    # -1.0
    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print( angleCos(u, v))
    # 1.0
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print( angleCos(u, v))
    # 0.974631846

if __name__ == '__main__':
    __main__()