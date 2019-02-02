if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    print(lst[(n-1)//2])