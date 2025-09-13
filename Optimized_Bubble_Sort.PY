n = int(input())
li = []
# li = list(map(int, input().split()))
for i in range(n):
    li.append(int(input()))

for i in range(n-1):
    flag = 0
    for j in range(n-1-i):
        if li[j]>li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
            flag = 1
        if flag == 0: break

for i in range(n):
    print(li[i], end=" ")
    