n = int(input())
while True:
    origin_number = n
    for i in range(len(str(n)),0,-1):
        str_n = str(n)
        if str_n[i-1] in ["5","6","7","8","9"]:
            if str_n[i-1] in "5":
                str_n = str_n.replace("5", "6")
            n = round(int(str_n), i-len(str_n)-1)
    if origin_number == n:
        break
print(n)