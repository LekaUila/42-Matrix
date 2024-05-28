# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/28 16:33:07 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector



def __main__():
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.add(v)
    print(u)
    # [7.0]
    # [10.0]
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.sub(v)
    print(u)
    # [-3.0]
    # [-4.0]
    u = Vector([2., 3.])
    u.scl(2.)
    print(u)
    # [4.0]
    # [6.0]
    print("")
    u = Matrix([[1., 2.],[3., 4.]])
    v = Matrix([[7., 4.],[-2., 2.]])
    print(u + v, "\n")
    u.add(v)
    print(u)
    
    # [8.0, 6.0]
    # [1.0, 6.0]
    u = Matrix([[1., 2.],[3., 4.]])
    v = Matrix([[7., 4.],[-2., 2.]])
    print(u - v, "\n")
    u.sub(v)
    print(u)
    # [-6.0, -2.0]
    # [5.0, 2.0]
    u = Matrix([[1., 2.],[3., 4.]])
    print(u * 2., "\n")
    u.scl(2.)
    print(u)
    # [2.0, 4.0]
    # [6.0, 8.0]
    return 0

if __name__ == '__main__':
    __main__()