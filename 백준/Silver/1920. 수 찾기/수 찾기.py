N = int(input())
a = list(map(int, input().split()))
a.sort()

def binarySearch(target):
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if a[mid] == target:
            print(1)
            return
        elif a[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    print(0)
    return

m = int(input())
b = list(map(int, input().split()))
for i in range(m):
    binarySearch(b[i])