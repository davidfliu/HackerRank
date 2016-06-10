import hashlib

n = int(raw_input())
T = tuple(map(int, raw_input().strip().split(" ")))
print hash(T)
