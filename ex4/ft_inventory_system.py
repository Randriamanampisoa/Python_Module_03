#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/14 12:25:37 by fanilran            #+#    #+#            #
#   Updated: 2026/06/06 21:15:55 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


class Error(Exception):
    pass


def parse(args: list[str]) -> dict[str, int] | None:
    all_dict: dict[str, int] = {}
    for arg in args:
        try:
            key_value = arg.split(':')
            if len(key_value) != 2:
                raise Error(f"Error - invalid parameter '{arg}'! "
                            "Usage: Python <item_name>:<quantity> ...")
            if key_value[0] in all_dict.keys():
                print(f"Redundant item '{key_value[0]}' - discarding")
                continue
            all_dict[key_value[0]] = int(key_value[1])
        except Error as e:
            print(f"{e}")
        except Exception as e:
            print(f"Quantity error for '{key_value[0]}': {e}")
    return all_dict


def main() -> None:
    args = sys.argv[1:]
    tmp = parse(args)
    if not tmp:
        return
    print(f"Got inventory: {tmp}")
    lst = list(tmp.keys())
    len_keys = len(lst)
    values = sum(tmp.values())
    print(f"Item list: {lst}")
    print(f"Total quantity of the {len_keys} items: {values}")
    for key in tmp:
        value = tmp[key]
        if values != 0:
            percentage = (value / values) * 100
        else:
            percentage = 0
        print(f"Item {key} represents {round(percentage, 1)}%")
    max_key = lst[0]
    max_val = tmp[max_key]
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
    print(f"Item least abundant: {min_key} with quantity {min_val}")
    tmp.update({"magic_item": 1})
    print(f"Updated inventory: {tmp}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    len_argv = len(sys.argv)
    if len_argv == 1:
        print("No arguments provided! "
              "Usage: Python <item_name>:<quantity>")
    else:
        try:
            main()
        except Exception:
            pass
