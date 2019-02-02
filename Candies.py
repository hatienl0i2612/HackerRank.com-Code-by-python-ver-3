if __name__ == "__main__":
    arr = [int(input()) for _ in range(int(input()))]
    out = []
    new_arr = [-1] * len(arr)
    new_arr[0] = 1
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            new_arr[i] = new_arr[i-1] + 1
        else:
            new_arr[i] = 1
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > arr[i + 1] and new_arr[i + 1] + 1 >= new_arr[i]:
            new_arr[i] = new_arr[i + 1] + 1
    print(sum(new_arr))