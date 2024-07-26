# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mathUtils.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/31 12:06:19 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 12:21:01 by lflandri         ###   ########.fr        #
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

def abs(flt):
    return flt *-1 if flt < 0 else flt
