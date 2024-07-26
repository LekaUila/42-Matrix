# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    projection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/17 14:59:46 by lflandri          #+#    #+#              #
#    Updated: 2024/07/17 15:05:59 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Matrix import Matrix, acceptedType
from math import tan

def projection(fov, ratio, near, far):
    if type(fov) not in acceptedType or type(ratio) not in acceptedType or type(near) not in acceptedType or type(far) not in acceptedType :
        raise TypeError()
    return Matrix([[ 1 / (ratio * tan(fov / 2)), 0, 0, 0],
		           [ 0, 1 / tan(fov / 2), 0, 0],
                   [ 0, 0, (near + far) / (near - far), (2 * near * far) / (near - far)],
                   [ 0, 0, -1, 0]
	               ])