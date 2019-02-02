def solved(n,arr):
    left = 0
    right = len(arr) - 1
    left_sum = arr[left]
    right_sum = arr[right]
    while left != right:
        if left_sum < right_sum:
            left += 1
            left_sum += arr[left]
        else:
            right -= 1
            right_sum += arr[right]
    return left_sum == right_sum

if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        if solved(n,arr):
            print('YES')
        else:
            print('NO')