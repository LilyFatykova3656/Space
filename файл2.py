for N in range(1,1000):
    n=bin(N)[2:]
    if n.count('1')%2==0:
        n = '10'+n[2:]+'0'
    else:
        n='11'+n[2:]+'1'
    r = int(n,2)
    if r>40:
        print(N)
        break
