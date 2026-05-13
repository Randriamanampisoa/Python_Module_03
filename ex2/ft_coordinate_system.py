#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 17:52:34 by fanilran            #+#    #+#            #
#   Updated: 2026/05/13 17:30:23 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        format = input("Enter new coordinates as floats in format 'x,y,z': ")
        split = format.split(",")
        try:
            if len(split) != 3:
                raise UnboundLocalError("Invalid syntax")
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
        except ValueError as e:
            print(f"Error on parameter '{index}': {e}")
        except UnboundLocalError as e:
            print(e)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    x = first[0]
    y = first[1]
    z = first[2]
    sqrt = math.sqrt((x)**2 + (y)**2 + (z)**2)
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {sqrt: .4f}")

    print("\nGet a second set of coordinates")
    second = get_player_pos()
    x1 = second[0]
    y1 = second[1]
    z1 = second[2]
    sqrt = math.sqrt((x1-x)**2 + (y1-y)**2 + (z1-z)**2)
    # print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance between the 2 sets of coordinates: {sqrt: .4f}")
