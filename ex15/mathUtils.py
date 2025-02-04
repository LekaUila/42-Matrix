# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mathUtils.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <lflandri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/31 12:06:19 by lflandri          #+#    #+#              #
#    Updated: 2025/02/04 21:50:18 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sqrt(n):
    i = 0
    result = 1
    if n == 0.0:
        return 0.0
    while i < 50:
        result = (result + (n / result)) / 2
        i+=1
    return result

def abs(nb):
    try :
        return nb.abs()
    except :
        try :
            return nb *-1 if nb < 0 else nb
        except :
            raise ArithmeticError(f"Can't do abs of {nb}, make sur {type(nb)} has method 'abs'")
