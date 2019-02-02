from collections import Counter
_ = int(input())
dic = Counter(list(map(int,input().split())))
for k,v in dic.items():
    if v == 1:
        print(k)
        break