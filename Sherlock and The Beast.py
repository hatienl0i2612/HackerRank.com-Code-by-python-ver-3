def oke(n):
    if n < 3:
        print(-1)
        return
    elif n % 3 == 0:
        print('5'*n)
        return
    elif n == 5:
        print('3'*n)
    else:
        flag = False
        for j in range(int(n/3),-1,-1):
            if (n - (3*j))%5 ==0:
                flag = True
                print("{}{}".format('5'*(3*j),'3'*(n - (3*j))))
                break
        if not flag:
            print(-1)
            return

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        oke(n)