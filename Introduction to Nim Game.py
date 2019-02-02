from functools import reduce
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        pile = list(map(int,input().split()))
        print("Second" if reduce(lambda a,b:a^b,pile) == 0 else "First")