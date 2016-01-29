#!/usr/bin/env python3

"""One-line code to transcribe DNA to RNA"""

print('{0}\n{1}'.format(open('input/puzzle2.txt').readline().strip(), ''.join(['U' if n == 'T' else n for n in open('input/puzzle2.txt').readline()])))
