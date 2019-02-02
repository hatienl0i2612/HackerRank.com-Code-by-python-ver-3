if __name__ == '__main__':
    t = int(input())
    elem = set(input().strip())
    for _ in range(t-1):
        elem &= set(input())
    print(len(elem))