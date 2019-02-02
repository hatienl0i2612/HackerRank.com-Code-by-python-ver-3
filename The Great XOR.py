def solved(x):
    b = 2**(x.bit_length()) -1 - x
    print(b)
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        solved(n)