# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/06/04 16:40:07 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector




def __main__():
    u = Matrix([
    [1., 0., 0.],
    [0., 1., 0.],
    [0., 0., 1.],
    ])
    print(u.rank())
    # 3
    u = Matrix([
    [ 1., 2., 0., 0.],
    [ 2., 4., 0., 0.],
    [-1., 2., 1., 1.],
    ])
    print(u.rank())
    # 2
    u = Matrix([
    [ 8., 5., -2.],
    [ 4., 7., 20.],
    [ 7., 6., 1.],
    [21., 18., 7.],
    ])
    print(u.rank())
    # 
    return 0

if __name__ == '__main__':
    __main__()