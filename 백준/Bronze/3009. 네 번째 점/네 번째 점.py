import sys
x1,y1=map(int,sys.stdin.readline().split())
x2,y2=map(int,sys.stdin.readline().split())
x3,y3=map(int,sys.stdin.readline().split())

if x1==x2:
    result_x=x3
elif x2==x3:
    result_x=x1
elif x3==x1:
    result_x=x2

if y1==y2:
    result_y=y3
elif y2==y3:
    result_y=y1
elif y3==y1:
    result_y=y2
print(result_x,result_y)