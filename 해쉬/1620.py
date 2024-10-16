import sys

n,m = map(int, sys.stdin.readline().split())
pokemon = dict()
pokemon_idx = dict()
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = i
    pokemon_idx[i] = name
for j in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit():
        print(pokemon_idx[int(tmp)])
    else:
        print(pokemon[tmp])
    
    