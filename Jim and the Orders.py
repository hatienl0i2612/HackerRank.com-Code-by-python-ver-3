def oke(arr):
    arr = sorted(arr)
    for i in arr:
        print(i[1] + 1,end = ' ')
if __name__ == "__main__":
    arr = []
    for i in range(int(input())):
        arr.append([sum(list(map(int,input().split()))),i])
    oke(arr)