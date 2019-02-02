if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        r = 0
        for i in range(n):
            if arr[i] % 2 == 1:
                r ^= i
        if r == 0:
            print("Second")
        else:
            print("First")
