# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linearCombination.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 16:58:19 by lflandri          #+#    #+#              #
#    Updated: 2024/05/28 17:36:29 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Matrix import Matrix, Vector, acceptedType


def linearCombination(u, coefs):
    if type(u) != list and type(u) != Matrix:
        raise TypeError()
    if len(u) != len(coefs):
        raise ArithmeticError(f"The number of vector doesn't match the number of coefficient. {len(u)} != {len(coefs)}")
    if len(u) == 0:
        raise Exception("Empty list.")
    retVector = Vector(lenP=u[0].size())
    for i in range(len(coefs)):
        for j in range(u[i].size()):
            if type(coefs[i]) not in acceptedType:
                raise TypeError
            retVector[j] = retVector[j] +  u[i][j] *  coefs[i]
    return retVector
    