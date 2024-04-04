N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

index_a = 0
index_b = 0
result = []
for i in range(N+M):
    if index_a != N and (index_b == M or A[index_a] <= B[index_b]):
        result.append(A[index_a])
        index_a += 1
    elif index_b != M and (index_a == N or B[index_b] <= A[index_a]):
        result.append(B[index_b])
        index_b += 1

for i in result:
    print(i, end=' ')