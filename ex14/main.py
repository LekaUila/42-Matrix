# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/28 14:19:07 by lflandri          #+#    #+#              #
#    Updated: 2024/07/17 15:52:47 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from class_d.Matrix import Matrix, Vector
from projection import projection



def __main__():

    print(projection(70, 2, 1, 50))
    return 0

if __name__ == '__main__':
    __main__()
    
    
#command to set format for proj file :  py main.py | sed s/'|'/''/g | sed s/'\['/''/g | sed s/'\]'/''/g  > /proj