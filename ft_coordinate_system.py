#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:52:34 by fanilran            #+#    #+#            #
#   Updated: 2026/05/11 17:48:04 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def get_player_pos() -> tuple:
    print("Get a first set of coordinates")
    try:
        format = input("Enter new coordinates as floats in format 'x,y,z': ")
        split = format.split(",")
        if len(split) != 3:
            raise ValueError("Invalid syntax")
        i = 1
        for index in split:
            if i == 1:
                index1 = float(index)
            elif i == 2:
                index2 = float(index)
            elif i == 3:
                index3 = float(index)
            i += 1
        return index1, index2, index3
        
    except UnboundLocalError as e:
        print(e)
    except ValueError as e:
        print(f"{e}", end="")
        print("could not convert string to float:")
    

if __name__ == "__main__":
    res = get_player_pos()
    print(f"Got a first tuple: {res}")
