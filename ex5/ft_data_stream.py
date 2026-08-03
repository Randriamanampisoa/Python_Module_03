#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: fanilran <fanilran@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 13:48:14 by fanilran            #+#    #+#            #
#   Updated: 2026/06/06 21:14:57 by fanilran           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
import typing


def get_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
                "run", "eat", "sleep", "grab", "move", "climb",
                "swim", "release", "use"
    ]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield player, action


def lst_event() -> list[tuple[str, str]]:
    generateur = get_event()
    event = []
    for _ in range(10):
        event += [next(generateur)]
    return event


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[
                                                tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        events[:] = events[:index] + events[index + 1:]
        yield event


if __name__ == "__main__":
    a = get_event()
    for i in range(1000):
        player, action = next(a)
        print(f"Event {i}: Player {player} did action {action}")
    events = lst_event()
    print(f"Built list of {len(events)} events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
