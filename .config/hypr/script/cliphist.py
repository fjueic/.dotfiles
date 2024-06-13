#!/usr/bin/env python3
data = ""
try:
    while True:
        data += input()
except EOFError:
    pass

if data == "":
    quit()

if len(data) > 23:
    data = data[:20] + "..."
print(data)

