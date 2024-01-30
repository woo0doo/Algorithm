def solution(friends, gifts):
    idx_friends = dict()
    for idx, name in enumerate(friends):
        idx_friends[name] = idx
    
    arr = [[0] * len(friends) for _ in range(len(friends))]
    for i in gifts:
        sender,receiver = map(str, i.split())
        sender_idx = idx_friends.get(sender)
        receiver_idx = idx_friends.get(receiver)
        arr[sender_idx][receiver_idx] += 1
    
    gift_numbers = []
    for j in range(len(friends)):
        sum_cnt = 0
        for a in range(len(friends)):
            sum_cnt += arr[j][a]
            sum_cnt -= arr[a][j]
        gift_numbers.append(sum_cnt)
        
        
    receive_numbers = []
    max_cnt = 0
    for send in range(len(friends)):
        cnt = 0
        for receive in range(len(friends)):
            if send == receive:
                continue
            elif arr[send][receive] > arr[receive][send]:
                cnt += 1
            elif arr[send][receive] == arr[receive][send]:
                if gift_numbers[send] > gift_numbers[receive]:
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
        receive_numbers.append(cnt)
    
    return max_cnt
        