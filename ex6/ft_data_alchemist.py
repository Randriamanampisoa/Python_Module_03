#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 17:06:29 by fanilran            #+#    #+#            #
#   Updated: 2026/06/02 15:09:14 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    player = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {player}")
    len_p = len(player)
    all_lst_capitalized = [player[i].capitalize() for i in range(len_p)]
    already_lst_capitalize = [player[j] for j in range(len_p)
                              if player[j] == player[j].capitalize()]
    print(f"New list with all names capitalized: {all_lst_capitalized}")
    print(f"New list of capitalized names only: {already_lst_capitalize}")
    all_dict = {}
    for i in range(len_p):
        all_dict[all_lst_capitalized[i]] = random.randint(1, 1000)
    print(f"Score dict: {all_dict}")
    tot_s = 0
    i = 0
    value = list(all_dict)
    while i < len(value):
        tot_s += all_dict[value[i]]
        i += 1
    avg = tot_s / len_p
    print(f"Score average is {avg: .2f}")
    new_dict = {}
    for i in range(len(value)):
        key = value[i]
        val = all_dict[key]
        if val > 400:
            new_dict[key] = val
    print(f"High scores: {new_dict}")
