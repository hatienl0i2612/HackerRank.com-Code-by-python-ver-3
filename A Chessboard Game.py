if __name__ == "__main__":
    for _ in range(int(input())):
        x,y = map(int,input().split())
        x %= 4
        y %= 4
        if (x == 0 or x == 3) or (y == 0 or y == 3):
            print("First")
        else:
            print("Second")