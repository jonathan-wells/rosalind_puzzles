#!/usr/bin/env python3

def converttolists(base, exponent, parts):
    if len(parts) == 0:
        parts = [(base, exponent)]
        etrack = exponent
    while etrack > 990:
        for pair in list(parts):
            parts.append((base, etrack - 1))
            parts.append((base, etrack - 1))
            parts.remove(pair)
        etrack -= 1
    print(len(parts))
    print(parts[0])


converttolists(2, 1000, [])
