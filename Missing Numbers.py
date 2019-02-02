# itt = int(input())
# A = map(int,input().split())
# itt_b = int(input())
# B = map(int,input().split())
# mini = min(B)
# answer = []
# lis = [0 for x in range(102)]
# for k in A:
#     lis[k-mini] -= 1
# for d in B:
#     lis[d-mini] += 1
# for ind, ele in enumerate(lis):
#     if ele != 0:
#         answer.append(ind+mini)
# print(' '.join(map(str,answer)))
from collections import Counter
int_a = int(input())
a = sorted(list(map(int,input().split())))
int_b = int(input())
b = sorted(list(map(int,input().split())))
a_c = Counter(a)
b_c = Counter(b)
for k,v in a_c.items():
    if b_c[k]   
