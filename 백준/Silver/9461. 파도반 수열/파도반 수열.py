t=int(input())

dp=[0]*100

def tri(x):
    if x==0 or x==1 or x==2:
        return 1
    if x==3 or x==4:
        return 2
    if dp[x] != 0:
        return dp[x]
    dp[x] = tri(x-1) + tri(x-5)
    return dp[x]
    
for _ in range(t):
    n=int(input())
    print(tri(n-1))