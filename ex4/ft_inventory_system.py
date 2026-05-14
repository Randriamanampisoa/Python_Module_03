#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/14 12:25:37 by fanilran            #+#    #+#            #
#   Updated: 2026/05/14 16:16:28 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

def parse(args: list):
    all = {}
    for arg in args:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = arg.split(":", 1)
        if key in all:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            value = int(value)
        except ValueError:
            print(f"Quantity error for '{key}': invalid literal for int() with base 10: '{value}'")
            continue
        all[key] = value
    return all


def main():
    args = sys.argv[1:]
    tmp = parse(args)

    print(f"Got inventory: {tmp}")
    lst = list(tmp.keys())
    len_lst_keys = len(lst)
    values = sum(tmp.values())
    print(f"Item list: {lst}")
    print(f"Total quantity of the {len_lst_keys} items: {values}")

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    len_argv = len(sys.argv)
    if len_argv == 1:
        print("Nothing article study")
    else:
        main()