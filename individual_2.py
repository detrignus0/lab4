#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))
    if not a:
        print('Заданный список пуст', file=sys.stderr)
        exit(1)

    i_min = 0
    for i, item in enumerate(a):
        if abs(item) < abs(a[i_min]):
            i_min = i
    print(i_min)

    s = 0
    idx_neg = -1
    for i, item in enumerate(a):
        if item < 0:
            idx_neg = i
            break

    if idx_neg != -1:
        for item in a[idx_neg + 1:]:
            s += abs(item)
        print(s)

    val_a = float(input())
    val_b = float(input())

    res = [x for x in a if not (val_a <= x <= val_b)]
    res += [0.0] * (len(a) - len(res))
    print(res)