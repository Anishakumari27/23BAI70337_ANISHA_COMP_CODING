import sys
sys.setrecursionlimit(10**7)

data = sys.stdin.read().split()
n = int(data[0])
tokens = data[1:]

i = 0
t = 0
b = []

def F():
    global i, t
    if i < len(tokens):
        s = tokens[i]
        i += 1
        b.append(s)
        if s == "pair":
            b.append('<')
            F()
            b.append(',')
            F()
            b.append('>')
    else:
        t = 1

F()

if t or i != len(tokens):
    print("Error occurred")
else:
    print("".join(b))