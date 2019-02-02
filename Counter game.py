def solved(v):
    count = 0
    while v:
        v &= (v-1)
        count += 1
    return count
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        if solved(n-1) & 1:
            print("Louise")
        else:
            print("Richard")