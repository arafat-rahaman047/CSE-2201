n = int(input())
li = []
# li = list(map(int, input().split()))
for i in range(n):
    li.append(int(input()))

for i in range(1, n):
    key = li[i]
    j = i - 1
    while j >= 0 and li[j] > key:
        li[j+1] = li[j]
        j = j-1
    li[j+1] = key

for i in range(n):
    print(li[i], end=" ")
