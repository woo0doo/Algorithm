arr=input()
res=0
res+=arr.count('c=')
res+=arr.count('c-')
res+=arr.count('dz=')
res+=arr.count('d-')
res+=arr.count('lj')
res+=arr.count('nj')
res+=arr.count('s=')
res+=arr.count('z=')
print(len(arr) - res)
