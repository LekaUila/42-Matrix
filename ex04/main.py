# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 12:18:41 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector
from lerp import lerp




def __main__():
    u = Vector([0., 0., 0.])
    print(u.norm1(), u.norm(), u.normInf())
    # 0.0, 0.0, 0.0
    u = Vector([1., 2., 3.])
    print(u.norm1(), u.norm(), u.normInf())
    # 6.0, 3.74165738, 3.0
    u = Vector([-1., -2.])
    print(u.norm1(), u.norm(), u.normInf())
    # 3.0, 2.236067977, 2.0

if __name__ == '__main__':
    __main__()