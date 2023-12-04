import sys
input = sys.stdin.readline

# 최댓값은 MK가 이어질 시 무조건 50 ~ 으로 바꾸는 것이고
# 최솟값은 M이 무조건 1로 변환되는 것 MM이 이어지면 10으로 바뀌는 것
word = list(map(str, input().rstrip()))

max_cnt = ""
min_cnt = ""

# Max 일 경우
m_cnt = 0
for i in range(len(word)):
    if word[i] == "M":
        max_cnt += "1"
        m_cnt += 1
    elif word[i] == "K":
        if m_cnt != 0:
            max_cnt = max_cnt[:-m_cnt] + "5" + "0" * m_cnt
            m_cnt = 0
        else:
            max_cnt += "5"

min_m_cnt = 0
for j in range(len(word)):
    if word[j] == "M":
        if min_m_cnt != 0:
            min_cnt = min_cnt[:-min_m_cnt] + "1" + "0" * min_m_cnt
            min_m_cnt += 1
        else:
            min_cnt += "1"
            min_m_cnt += 1
    elif word[j] == "K":
        min_cnt += "5"
        min_m_cnt = 0

print(max_cnt)
print(min_cnt)