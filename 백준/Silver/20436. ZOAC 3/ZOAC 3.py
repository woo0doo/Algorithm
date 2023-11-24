l, r = input().split()
word = input()

l_list=[["q","w","e","r","t"], ["a","s","d","f","g"],["z","x","c","v","No"]]
r_list = [["No","y","u","i","o","p"], ["No", "h","j","k","l","No"],["b","n","m","No","No","No"]]

distance = 0

def findLeftIndex(word):
    for i in range(3):
        for j in range(5):
            if word == l_list[i][j]:
                y_index = i+1
                x_index = j+1
                return [y_index, x_index]
    return [-1, -1]

def findRightIndex(word):
    for i in range(3):
        for j in range(6):
            if word == r_list[i][j]:
                y_index = i+1
                x_index = j+1
                return [y_index, x_index]
    return [-1, -1]

left_index = findLeftIndex(l)
l_y_index = left_index[0]
l_x_index = left_index[1]
right_index = findRightIndex(r)
r_y_index = right_index[0]
r_x_index = right_index[1]

for i in range(len(word)):
    find_left_index = findLeftIndex(word[i])
    if find_left_index[0] != -1:
        y_sub = abs(l_y_index - find_left_index[0])
        x_sub = abs(l_x_index - find_left_index[1])
        distance += y_sub+x_sub+1
        l_y_index = find_left_index[0]
        l_x_index = find_left_index[1]

    find_right_index = findRightIndex(word[i])
    if find_right_index[0] != -1:
        y_sub = abs(r_y_index - find_right_index[0])
        x_sub = abs(r_x_index - find_right_index[1])
        distance += y_sub+x_sub+1
        r_y_index = find_right_index[0]
        r_x_index = find_right_index[1]
print(distance)