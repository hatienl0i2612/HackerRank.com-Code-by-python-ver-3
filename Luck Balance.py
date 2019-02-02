n,k = map(int,input().split())
cs = [tuple(map(int,input().split())) for i in range(n)]
print(sum(map(lambda x: x[0], filter(lambda x: not x[1], cs))) + sum(map(lambda l, sgn: l*sgn, reversed(sorted(map(lambda x: x[0], filter(lambda x: x[1], cs)))),  [1]*k + [-1]*n)))