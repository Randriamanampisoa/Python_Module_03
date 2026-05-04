#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/28 20:19:14 by fanilran            #+#    #+#            #
#   Updated: 2026/04/29 17:43:35 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No score provided. Usage: python3 ft_score_analytics <score1> <score2> ...")
    else:
        valid_args = []
        invalid_args = []

        for arg in sys.argv[1:]:
            try:
                int(arg)
                valid_args += [arg]
            except ValueError:
                invalid_args += [arg]

        for i in invalid_args:
            print(f"Invalid parameter: '{i}'")

        scores = [int(x) for x in valid_args]

        if not scores:
            print("No valid scores provided.")
        else:
            tot_p = len(scores)
            tot_s = sum(scores)
            avg = tot_s / tot_p
            high = max(scores)
            low = min(scores)
            score_range = high - low

            print(f"Score processed: {scores}")
            print(f"Total players: {tot_p}")
            print(f"Total score: {tot_s}")
            print(f"Average score: {avg:.1f}")
            print(f"High score: {high}")
            print(f"Low score: {low}")
            print(f"Score range:: {score_range}")