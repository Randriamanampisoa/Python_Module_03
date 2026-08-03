#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 17:06:29 by fanilran            #+#    #+#            #
#   Updated: 2026/06/05 17:10:55 by fanilran           ###   ########.fr      #
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
    all_lst_capitalized = [i.capitalize() for i in player]
    already_lst_capitalize = [j for j in player if j == j.capitalize()]
    all_dict = {i: random.randint(1, 1000) for i in player}
    tot_s = sum(all_dict[key] for key in all_dict)
    avg = tot_s / len_p
    new_dict = {key: all_dict[key] for key in all_dict if all_dict[key] > avg}
    print(f"New list with all names capitalized: {all_lst_capitalized}")
    print(f"New list of capitalized names only: {already_lst_capitalize}")
    print(f"Score dict: {all_dict}")
    print(f"Score average is {avg: .2f}")
    print(f"High scores: {new_dict}")
