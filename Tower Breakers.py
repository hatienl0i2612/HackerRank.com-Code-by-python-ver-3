def solved(n,m):
    if m == 1 or n % 2 == 0:
        print(2)
    else:
        print(1)
if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        n,m = map(int,input().split())
        solved(n,m)