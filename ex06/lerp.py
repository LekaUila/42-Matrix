# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lerp.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 16:58:19 by lflandri          #+#    #+#              #
#    Updated: 2024/05/28 17:55:37 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Vector import acceptedType


def lerp(u, v, t):
    if type(t) not in acceptedType:
        raise TypeError()
    try:
        x = u.__add__
        x = u.__sub__
        x = u.__mul__
        x = v.__add__
        x = v.__sub__
        x = v.__mul__
    except AttributeError :
        raise TypeError("Can't use a type who haven't an overloading operateur for '+' ('__add__'), '-' ('__sub__') and '*' ('__mul__')")
    return (((v - u) * t) + u)
    
        

    