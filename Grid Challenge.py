
def solved(lst):
    return True if list(lst) == sorted(lst) else False
    
for i in range(int(input())):
    lst = []
    for _ in range(int(input())):
        lst.append(sorted(input()))
    zipp = (solved(z) for z in zip(*lst))
    print("YES" if all(zipp) else "NO")
    