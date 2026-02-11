#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = tuple(map(float, input().split()))

    if len(a) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    is_sorted = True
    err_idx = -1

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            is_sorted = False
            err_idx = i + 1
            break

    if is_sorted:
        print("Упорядочен")
    else:
        print(err_idx + 1)