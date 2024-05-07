T = 10

for _ in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        max_idx, min_idx, max_num, min_num = 0, 0, 0, 1000
        for idx, box in enumerate(boxes):
            if box > max_num:
                max_idx = idx
                max_num = box
            if box < min_num:
                min_idx = idx
                min_num = box
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    print(f"#{_}", max(boxes) - min(boxes))


