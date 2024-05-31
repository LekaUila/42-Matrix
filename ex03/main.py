# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 11:48:59 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector
from lerp import lerp




def __main__():
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))
    # 0.0
    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(u.dot(v))
    # 2.0
    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(u.dot(v))
    # 9.0

if __name__ == '__main__':
    __main__()