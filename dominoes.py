import random


def gen_set_all():
    s = []
    for i in range(0, 7):
        for j in range(i, 7):
            p = []
            p.append(i)
            p.append(j)
            s.append(p)
    return s


def get_max(list):
    vmax = 0
    imax = -1
    for i in range(len(list)):
        if list[i][0] == list[i][1] and list[i][0] > vmax:
            imax = i
            vmax = list[i][0]
    return imax


set_all = gen_set_all()
set_snake = []
status = ""

while True:
    set_stock = []
    set_stock.extend(set_all)
    random.shuffle(set_stock)

    set_comp = []
    for i in range(7):
        set_comp.append(set_stock.pop())

    set_player = []
    for i in range(7):
        set_player.append(set_stock.pop())

    imax_comp = get_max(set_comp)
    imax_player = get_max(set_player)
    if imax_comp == -1 and imax_player == -1:
        continue

    if set_comp[imax_comp][0] > set_player[imax_player][0]:
        p = set_comp.pop(imax_comp)
        status = "player"
    else:
        p = set_player.pop(imax_player)
        status = "computer"
    set_snake.append(p)
    break

print(f"Stock pieces: {set_stock}")
print(f"Computer pieces: {set_comp}")
print(f"Player pieces: {set_player}")
print(f"Domino snake: {set_snake}")
print(f"Status: {status}")
