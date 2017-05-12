#!/usr/bin/env python3

import decimal
import re

def decfrac_to_string(num, denom):
    decimal.getcontext().prec = 3000
    value = decimal.Decimal(num)/decimal.Decimal(denom)
    return str(value).split('.')[1]


def repeatsearch(string):
    pattern = re.compile(r'([0-9]+?)\1+')
    matchobj = pattern.findall(string)
    if matchobj:
        return sorted(matchobj)[::-1][0]

class SuffixTree(object):
    def __init__(self, string):
        assert type(string) == str
        self.s = string + '$'
        self.n = len(string)
        self.nodes = {}
        self.edges = {}
        self._constructtree()

    def _constructtree(self):
        for i in range(self.n + 1):
            suf = self.s[i:]


    def __repr__(self):
        return self.s

if __name__ == '__main__':
    currmax = 0
    idx = 0
    topcycle = ''
    for i in range(2, 1001):
        dfstring = decfrac_to_string(1, i)
        cycle = repeatsearch(dfstring)
        if cycle and len(cycle) >= currmax:
            currmax = len(cycle)
            idx = i
            topcycle = cycle
    print(idx, topcycle)
