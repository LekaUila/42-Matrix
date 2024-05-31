# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    crossProduct.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/31 13:10:41 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 13:20:32 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Vector import Vector

def crossProduct(u, v):
    if type(u) != Vector or type(v) != Vector:
        raise TypeError()
    if u.size() == v.size() == 3:
        return Vector([u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]])
    raise ArithmeticError(f"Need two vector of Size 3 to do crossProduct {u.size()} {v.size()}")
    