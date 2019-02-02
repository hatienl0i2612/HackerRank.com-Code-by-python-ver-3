def commonChild(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    lcs = [[0]*(len(s1)+1) for _ in range(2)]
    for i in range(l1):
        li1 = (i+1)%2
        li = i%2
        for j in range(l2):
            if s1[i] == s2[j]:
                lcs[li1][j+1] = (lcs[li][j] + 1) 
            elif lcs[li1][j] > lcs[li][j+1]:
                lcs[li1][j+1] = lcs[li1][j] 
            else:
                lcs[li1][j+1] = lcs[li][j+1] 
    return lcs[(i+1)%2][j+1]
# def commonChild(s1, s2):
#     lcs = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 lcs[i + 1][j + 1] = lcs[i][j] + 1
#             else:
#                 lcs[i + 1][j + 1] = max(lcs[i][j + 1],lcs[i + 1][j])
#     return lcs[len(s1)][len(s2)]
if __name__ == "__main__":
    print(commonChild(input(),input()))