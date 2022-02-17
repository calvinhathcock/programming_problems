# https://open.kattis.com/problems/2048
# 0, 1, 2, 3
# left, up, right, down

#input
board = [list(map(int, input().split())) for _ in range(4)]
direction = int(input())
new_board = []

#board transformation for direction
if direction == 0:
    for i in board:
        i = i.reverse()
if direction == 1:
    board = list(map(list, zip(*board)))
    for i in board:
        i = i.reverse()
if direction == 3:
    board = list(map(list, zip(*board)))

#main loop
for r in board:
    t = [x for x in r if x > 0]
    checked = []
    for i in reversed(range(len(t))):
        if i in checked:
            continue
        if i > 0:
            if t[i] == t[i-1]:
                t[i] = t[i]*2
                t.pop(i-1)
                checked.append(i-1)
    if len(t) < 4:
        for i in range(4-len(t)):
            t.insert(0, 0)
    new_board.append(t)

#revert board direction
if direction == 0:
    for i in new_board:
        i = i.reverse()
if direction == 1:
    for i in new_board:
        i = i.reverse()
    new_board = list(map(list, zip(*new_board)))
if direction == 3:
    new_board = list(map(list, zip(*new_board)))

#output
for row in new_board:
    for c in row:
        print(str(c),  end = ' ')
    print()
