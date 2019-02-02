if __name__ == "__main__":
    n = int(input())
    binn = bin(n)[2:]
    count = 0
    for i in binn:
        if i == '0':
            count += 1
    print(2**count if n > 0 else 1)