#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/14 12:25:37 by fanilran            #+#    #+#            #
#   Updated: 2026/06/02 14:46:09 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def parse(args: list[str]) -> dict[str, int]:
    all: dict[str, int] = {}
    for arg in args:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value_str = arg.split(":")
        if key in all:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            value = int(value_str)
        except ValueError:
            print(f"Quantity error for '{key}': invalid literal"
                  f" for int() with base 10: '{value_str}'")
        all[key] = value
    return all


def main() -> None:
    args = sys.argv[1:]
    tmp = parse(args)
    print(f"Got inventory: {tmp}")
    lst = list(tmp.keys())
    len_keys = len(lst)
    values = sum(tmp.values())
    print(f"Item list: {lst}")
    print(f"Total quantity of the {len_keys} items: {values}")
    for key in tmp:
        value = tmp[key]
        percentage = (value / values) * 100
        print(f"Item {key} represents {round(percentage, 1)}%")
    max_val = 0
    max_key = None
    for v in tmp:
        if tmp[v] > max_val:
            max_val = tmp[v]
            max_key = v
    min_key = lst[0]
    min_val = tmp[min_key]
    for val in tmp:
        if tmp[val] < min_val:
            min_val = tmp[val]
            min_key = val
    print(f"Item most abundant: {max_key} with quantity {max_val}")
    print(f"Item most abundant: {min_key} with quantity {min_val}")
    tmp.update({"magic_item": 1})
    print(f"Updated inventory: {tmp}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    len_argv = len(sys.argv)
    if len_argv == 1:
        print("Nothing article study")
    else:
        main()
