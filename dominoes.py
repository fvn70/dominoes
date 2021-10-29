import random
import re

set_snake = []
turn = 0
count = {}

def calc_score():
    update_count()
    score = {}
    i = 0
    for p in set_comp:
        k = count[p[0]] + count[p[1]]
        score[i] = k
        i += 1
    s = [k for k in sorted(score, key=score.get)]
    return s

def update_count():
    for i in range(7):
        count[i] = 0
    for p in set_snake:
        count[p[0]] += 1
        count[p[1]] += 1
    for p in set_comp:
        count[p[0]] += 1
        count[p[1]] += 1

def read_in(t, l):
    left = False
    if t == 0:
        cmd = input()
        k = []
        score = calc_score()
        while True:
            j = -1 if len(score) == 0 else score.pop()
            if j == -1 or len(k) == 2 * l + 1:
                return 0
            if j in k:
                continue
            k.append(j)
            p = set_comp[j]
            chk = check_snake(p, left, True)
            if chk == -1:
                left = True
                chk = check_snake(p, left, True)
            if chk != -1:
                break
    else:
        while True:
            cmd = input()
            if re.match('-?[0-9]+', cmd) and int(cmd) in range(-l, l + 1):
                i = int(cmd)
                if i == 0:
                    return 0
                j = abs(i) - 1
                p = set_player[j]
                left = i < 0
                chk = check_snake(p, left, False)
                if chk != -1:
                    break
                else:
                    continue
            print("Invalid input. Please try again.")

    p = set_player.pop(j) if t == 1 else set_comp.pop(j)
    to_snake(p, left, chk == 1)
    return 1

# 0 - p match value v
# 1 - p need turn
# -1 - do not match
def check_snake(p, to_left, comp):
    v = set_snake[0][0] if to_left else set_snake[len(set_snake) - 1][1]
    if p[0] != v and p[1] != v:
        result = -1
    elif to_left:
        result = 0 if p[1] == v else 1
    else:
        result = 0 if p[0] == v else 1
    if not comp and result == -1:
        print("Illegal move. Please try again.")
    return result

def to_snake(p, left, reverse):
    if reverse:
        v = p[0]
        p[0] = p[1]
        p[1] = v
    if left:
        set_snake.insert(0, p)
    else:
        set_snake.append(p)


def end_game(comp, play, snake):
    result = False
    if len(comp) == 0:
        print("Status: The game is over. The computer won!")
        result = True
    elif len(play) == 0:
        print("Status: The game is over. You won!")
        result = True
    else:
        l = len(snake)
        if snake[0][0] == snake[l-1][1]:
            cnt = 0
            for s in snake:
                if s[0] == snake[0][0]:
                    cnt += 1
                if s[1] == snake[0][0]:
                    cnt += 1
            if cnt == 8:
                print("Status: The game is over. It's a draw!")
                result = True
    return result

def draw_prompt(t):
    if t == 0:
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")

def draw_title(stock_size, comp_size):
    print("=" * 70)
    print(f"Stock size: {stock_size}")
    print(f"Computer pieces: {comp_size}")

def draw_comp(list):
    print("Comp pieces:")
    print(list)

def draw_player(list):
    print("Your pieces:")
    for i in range(len(list)):
        print(f"{i + 1}:{list[i]}")
    print()

def draw_snake(list):
    imax = len(list)
    s = ""
    for i in range(imax):
        if i < 3 or i > imax - 4:
            s += str(list[i])
        if i == 2 and imax > 6:
            s += "..."
    print(f"\n{s}\n")

def gen_set_all():
    return [[i, j] for i in range(7) for j in range(i, 7)]

def get_max(list):
    vmax = 0
    imax = -1
    for i in range(len(list)):
        if list[i][0] == list[i][1] and list[i][0] > vmax:
            imax = i
            vmax = list[i][0]
    return imax

# Start game
while True:
    set_stock = gen_set_all()
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
    p_comp = set_comp[imax_comp] if imax_comp >= 0 else [-1, -1]
    p_pl = set_player[imax_player] if imax_player >= 0 else [-1, -1]

    if p_comp[0] > p_pl[0]:
        p = set_comp.pop(imax_comp)
        turn = 1
    else:
        p = set_player.pop(imax_player)
        turn = 0
    set_snake.append(p)

    break

# Game loop
while True:
    # draw()
    draw_title(len(set_stock), len(set_comp))
    # draw_comp(set_comp)
    draw_snake(set_snake)
    draw_player(set_player)
    if end_game(set_comp, set_player, set_snake):
        break
    draw_prompt(turn)
    l = len(set_player) if turn == 1 else len(set_comp)
    i = read_in(turn, l)
    if i == 0 and len(set_stock) > 0:
        if turn == 0:
            set_comp.append(set_stock.pop())
        else:
            set_player.append(set_stock.pop())
    turn = (turn + 1) % 2

