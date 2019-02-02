def solved(n):
    if n > 5:
        out = [1] * (n + 1)
        out[1] = 2
        out[2] = 1
        out[3] = 1
        out[4] = 1
        out[5] = 1
        for i in range(n + 1):
            if out[i - 2] == 2 or out[i - 3] == 2 or out[i - 5] == 2:
                out[i] = 1
            else:
                out[i] = 2
        if out[n] == 1:
            print("First")
        else:
            print("Second")
    else:
        if n == 1:
            print("Second")
        else:
            print("First")

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        solved(n)