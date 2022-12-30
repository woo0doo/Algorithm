import sys
from collections import Counter

n=input().upper()

num=Counter(n).most_common()
if len(num) > 1:
    if num[0][1] == num[1][1]:
        print("?")
    else:
        print(num[0][0])
else:
    print(num[0][0])

