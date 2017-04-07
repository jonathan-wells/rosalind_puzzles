#!/usr/bin/env python3

import re

class WrittenNumbers(object):
    def __init__(self):
        self._numbers = {0: '',
                         1: 'one',
                         2: 'two',
                         3: 'three',
                         4: 'four',
                         5: 'five',
                         6: 'six',
                         7: 'seven',
                         8: 'eight',
                         9: 'nine',
                         10: 'ten',
                         11: 'eleven',
                         12: 'twelve',
                         13: 'thirteen',
                         14: 'fourteen',
                         15: 'fifteen',
                         16: 'sixteen',
                         17: 'seventeen',
                         18: 'eighteen',
                         19: 'nineteen',
                         20: 'twenty',
                         30: 'thirty',
                         40: 'forty',
                         50: 'fifty',
                         60: 'sixty',
                         70: 'seventy',
                         80: 'eighty',
                         90: 'ninety',
                         100: 'hundred',
                         1000: 'thousand',
                         1000000: 'million'}

    def _split_parts(self, n):
        parts = [int(i) for i in str(n)]
        multiplier = 1
        for i in range(len(parts)):
            parts[-(i + 1)] *= multiplier
            multiplier *= 10
        n = len(parts)
        if n > 4:
            top = [int(str(parts[0])[:-3]), int('1'+str(parts[0])[-3:])]
            parts = top + parts[1:]

        return parts

    def _flatten(self, nested):
        for i in nested:
            if hasattr(i, '__iter__') and not isinstance(i, str):
                for sub in self._flatten(i):
                    yield sub
            else:
                yield i

    def _parse_tens(self, parts):
        if len(parts) == 1:
            return [self._numbers[parts[0]]]
        else:
            if parts[-2] < 20:
                parts[-2] += parts[-1]
                parts.pop()
        top = ['-'.join([self._numbers[i] for i in parts[-2:]])]
        top = [re.sub(r'\s+|-$', '', i) for i in top]
        return top

    def _parse_num(self, parts):
        n = len(parts)
        if n <= 2:
            return self._parse_tens(parts)
        elif n >= 3:
            if parts[0] == 0:
                top = ''
            else:
                top = [self._numbers[parts[-n]/10**(n-1)],
                       self._numbers[10**(n-1)]]
                top = ' '.join(top)
            below = self._parse_num(parts[-(n-1):])
            return [top, below]

    def getnum(self, n):
        parts = self._split_parts(n)
        written = list(self._flatten(self._parse_num(parts)))
        for word in list(written):
            if word == '':
                written.remove(word)
        if len(written) == 0:
            return 'zero'
        elif len(written) == 1:
            return written[0]
        else:
            written.insert(-1, 'and')
            written = ' '.join(written)
        return written


def count_letters(start, stop, step=1):
    numbers = WrittenNumbers()
    totletters = 0
    for i in range(start, stop, step):
        num = numbers.getnum(i)
        num = re.sub(r'-|\s+', '', num)
        totletters += len(num)
    print(totletters)



if __name__ == '__main__':
    count_letters(1, 1001)
    test = WrittenNumbers()
    print(test.getnum(2331))
    # print(test._split_parts(100000))
