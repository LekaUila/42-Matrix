# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:04 by lflandri          #+#    #+#              #
#    Updated: 2024/05/31 14:42:59 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from class_d.Vector import Vector, acceptedType

class Matrix:
    
    def __init__(this, listP=[], lenth=0, weith=0):
        if type(listP) != list or type(lenth) != int or type(weith) != int :
            raise TypeError()
        this.__list = list()
        if len(listP):
            test = len(listP[0])
            for i in listP:
                if test != len(i):
                    raise ArithmeticError("Can't create Matrix with different size of ligne")
                if type(i) == list:
                    this.__list.append(Vector(listP=i))
                else :
                    raise TypeError()
        else :
            for i in range(lenth):
                this.__list.append(Vector(lenP=weith))
                
    def __getitem__(this, key):
        if type(key) != int:
            raise TypeError()
        if len(this.__list) <= key:
            raise IndexError()
        return this.__list[key]
        
    def __setitem__(this, key, value):
        if type(key) != int or type(value) != Vector:
            raise TypeError()
        this.__list[key] = value
        
    def size(this):
        if len(this.__list):
            return (this.__list[0].size(),len(this.__list))
        return None
    def __len__(this):
            return len(this.__list)
    
    def isSquare(this):
        if len(this.__list):
            return this.__list[0].size() == len(this.__list)
        return False
        
    def __add__(this, other):
        if type(other) != Matrix:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't add two Matrix of two different size.")
        cop = this.copy()
        for i in range(len(this.__list)):
            cop[i] = this.__list[i] + other.__list[i]
        return cop

    def __sub__(this, other):
        if type(other) != Matrix:
            raise TypeError()
        if this.size() != other.size():
            raise ArithmeticError("Can't sub two Matrix of two different size.")
        cop = this.copy()
        for i in range(len(this.__list)):
            cop[i] = this.__list[i] - other.__list[i]
        return cop
        
            
    def __mul__(this, other):
        cop = this.copy()
        if type(other) in acceptedType:
            for i in range(len(this.__list)):
                cop[i] = this.__list[i] * other
        else :
            raise TypeError()
        return cop
        
        
    def __str__(this):
        s = ""
        for i in this.__list:
            s += "|" + i.__str__() + "|\n"
        return s 
    
    def add(this, other):
        this.__list = this.__add__(other).__list


    def sub(this, other):
        this.__list = this.__sub__(other).__list
        
    def scl(this, other):
        this.__list = this.__mul__(other).__list
        
    def copy(this):
        newMatrix = Matrix(lenth=len(this.__list))
        for i in range(len(this.__list)):
            newMatrix[i] = this.__list[i].copy()
        return newMatrix
        