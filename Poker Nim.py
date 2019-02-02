if __name__ == '__main__':
    for _ in range(int(input())):
        n,k=map(int,input().split())
        arr = list(map(int,input().split()))
        b = 0
        for i in arr:
            b ^= i
        if b == 0:
            print("Second")
        else:
            print("First")