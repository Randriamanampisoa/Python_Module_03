#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/13 12:39:03 by fanilran            #+#    #+#            #
#   Updated: 2026/05/26 15:46:12 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

all_achievements = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder'
    ]


def gen_player_achievements() -> set[str]:
    number = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, number))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    achievements = [
        gen_player_achievements(), gen_player_achievements(),
        gen_player_achievements(), gen_player_achievements()
        ]
    i = 0
    while i < len(players):
        print(f"Player {players[i]}: {achievements[i]}")
        i += 1
    union = set.union(achievements[0], achievements[1], achievements[2],
                      achievements[3])
    print(f"\nAll distinct achievements: {union}")

    intersect = set.intersection(achievements[0], achievements[1],
                                 achievements[2], achievements[3])
    print(f"\nCommon achievements: {intersect}\n")
    alice_only = set.difference(achievements[0], achievements[1],
                                achievements[2], achievements[3])
    bob_only = set.difference(achievements[1], achievements[0],
                              achievements[2], achievements[3])
    charlie_only = set.difference(achievements[2], achievements[0],
                                  achievements[1], achievements[3])
    dylan_only = set.difference(achievements[3], achievements[0],
                                achievements[1], achievements[2])
    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}")
    alice_missing = union - achievements[0]
    bob_missing = union - achievements[1]
    charlie_missing = union - achievements[2]
    dylan_missing = union - achievements[3]
    print(f"\nAlice is missing: {alice_missing}")
    print(f"\nBob is missing: {bob_missing}")
    print(f"\nCharlie is missing: {charlie_missing}")
    print(f"\nDylan is missing: {dylan_missing}")
