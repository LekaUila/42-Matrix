# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    angleCos.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/31 12:32:29 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 12:54:15 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Vector import Vector


def angleCos(u, v):
    if type(u) != Vector or type(v) != Vector:
        raise TypeError()
    if u.size() != v.size():
        raise ArithmeticError("Can't use angleCos on vector of different size.")
    if u.size() == 0:
        raise ArithmeticError("Can't use angleCos on vector of size NULL.")
    return (u.dot(v) / (u.norm() * v.norm()))