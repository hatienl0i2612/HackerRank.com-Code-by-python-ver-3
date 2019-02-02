if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        pile = list(map(int,input().split()))
        x = 0
        for i in pile:
            x ^= i
        if len(set(pile)) == 1 and 1 in pile:
            if x:
                print("Second")
            else:
                print("First")
        else:
            if x:
                print("First")
            else:
                print("Second")