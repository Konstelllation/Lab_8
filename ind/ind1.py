#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    c = [(10, 12), (8, 6), (9, 12), (9, 9), (13, 13)]
    all_x = []
    all_y = []
    for i in c:
        all_x.append(i[0])
        all_y.append(i[1])

    fp = (min(all_x), min(all_y))
    sp = (max(all_x), max(all_y))
    print(fp)
    print(sp)
