# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:04 by lflandri          #+#    #+#              #
#    Updated: 2024/06/04 12:46:27 by lflandri         ###   ########.fr        #
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
        cop = 0
        if type(other) in acceptedType:
            cop = this.copy()
            for i in range(len(this.__list)):
                cop[i] = this.__list[i] * other
                
        elif type(other) == Vector:
            cop = Vector(lenP=this.size()[1])
            if this.size()[0] != other.size():
                raise ArithmeticError("Can't multiply Matrix with Vector : Size don't match.")
            for j in range(this.size()[1]):
                nb = 0
                for i in range(other.size()):
                    nb += this[j][i] * other[i]
                cop[j] = nb
        elif type(other) == Matrix:
            if this.size()[0] != other.size()[1]:
                raise ArithmeticError(f"Can't multiply matrix : size error")
            #max = this.size()[1] if this.size()[1] > this.size()[0] else this.size()[0]
            cop = Matrix(lenth=this.size()[1], weith=other.size()[0])
            for iMult in range(other.size()[0]):
                for jMult in range(this.size()[1]):
                    nb = 0
                    for i in range(this.size()[0]):
                        nb += this[jMult][i] * other[i][iMult]
                    cop[jMult][iMult] = nb
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
    
    def mulVec(this, vec):
        if type(vec) != Vector:
            raise TypeError()
        return this * vec
    
    def mulMat(this, mat):
        if type(mat) != Matrix:
            raise TypeError()
        return this * mat
    
    def trace(this):
        if this.__list[0].size() != len(this.__list):
            raise ArithmeticError("Can't calcul trace of non square matrix.")
        retValue = 0
        for i in range(len(this.__list)):
            retValue += this[i][i]
        return retValue
    
    def transpose(this):
        newMatrix = Matrix(lenth=this.__list[0].size(), weith=len(this.__list))
        for i in range(len(this.__list)):
            for j in range(this.__list[0].size()):
                newMatrix[j][i] = this[i][j]
        return newMatrix