#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))

    if len(a) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    res = 1
    count = 0
    for item in a:
        if item > 0 and item % 3 == 0:
            res *= item
            count += 1

    if count > 0:
        print(f"Произведение: {res}")
        print(f"Количество: {count}")
    else:
        print(0)