#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/28 15:17:55 by fanilran            #+#    #+#            #
#   Updated: 2026/06/06 21:26:33 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print("Arguments received: ", len(sys.argv) - 1)
        i = 1
        for x in sys.argv[1:]:
            print(f"Argument {i}: {x}")
            i += 1
    print("Total arguments:", len(sys.argv))
