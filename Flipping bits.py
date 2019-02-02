if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(n^(pow(2,32) - 1))