#!/usr/bin/env python3
# coding=utf-8


s = []
with open('a.txt', 'r') as file:
    for line in file.readlines():
        s.append(line)
        print(line)

print(s)
