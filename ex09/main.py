# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/06/04 12:49:44 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector




def __main__():
    u = Matrix([
    [1., 0.],
    [0., 1.],
    ])
    print( u)
    print( u.transpose())
    print( u.transpose().transpose())
    print("----------")
    u = Matrix([
    [2., -5., 0.],
    [4., 3., 7.],
    [-2., 3., 4.],
    ])
    print( u)
    print( u.transpose())
    print( u.transpose().transpose())
    print("----------")
    u = Matrix([
    [-2., -8., 4.],
    [1., -23., 4.],
    [0., 6., 4.],
    ])
    print( u)
    print( u.transpose())
    print( u.transpose().transpose())
    print("----------")
    u = Matrix([
    [-2., -8., 4.],
    [1., -23., 4.],
    ])
    print( u)
    print( u.transpose())
    print( u.transpose().transpose())
    print("----------")
    u = Matrix([
    [-2., -8.],
    [1., -23.],
    [0., 6.],
    ])
    print( u)
    print( u.transpose())
    print( u.transpose().transpose())
    print("----------")
    
    return 0

if __name__ == '__main__':
    __main__()