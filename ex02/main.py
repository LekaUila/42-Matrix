# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/05/28 18:02:11 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector
from lerp import lerp




def __main__():
    print(lerp(0., 1., 0.))
    # 0.0
    print(lerp(0., 1., 1.))
    # 1.0
    print(lerp(0., 1., 0.5))
    # 0.5
    print(lerp(21., 42., 0.3))
    # 27.3
    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
    # [2.6]
    # [1.3]
    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5))
    # [[11., 5.5]
    # [16.5, 22.]
    return 0

if __name__ == '__main__':
    __main__()