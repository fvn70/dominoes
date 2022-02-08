import random
import re


def calc_score():
    update_count()
    score = {}
    i = 0
    for p in set_players[0]:
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
    for p in set_players[0]:
        count[p[0]] += 1
        count[p[1]] += 1


def gen_set_game():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def get_max(list):
    vmax = 0
    imax = -1
    for i in range(len(list)):
        if list[i][0] == list[i][1] and list[i][0] > vmax:
            imax = i
            vmax = list[i][0]
    return imax


def draw_title(stock_size, comp_size):
    print("=" * 70)
    print(f"Stock size: {stock_size}")
    print(f"Computer pieces: {comp_size}")


def draw_player():
    print("Your pieces:")
    for i in range(len(set_players[1])):
        print(f"{i + 1}:{set_players[1][i]}")
    print()


def draw_snake():
    imax = len(set_snake)
    s = ""
    for i in range(imax):
        if i < 3 or i > imax - 4:
            s += str(set_snake[i])
        if i == 2 and imax > 6:
            s += "..."
    print(f"\n{s}\n")


def draw_prompt(t):
    if t == 0:
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")


def end_game():
    result = False
    if not set_players[0]:
        print("Status: The game is over. The computer won!")
        result = True
    elif not set_players[1]:
        print("Status: The game is over. You won!")
        result = True
    else:
        if set_snake[0][0] == set_snake[len(set_snake) - 1][1]:
            cnt = 0
            for s in set_snake:
                if s[0] == set_snake[0][0]:
                    cnt += 1
                if s[1] == set_snake[0][0]:
                    cnt += 1
            if cnt == 8:
                print("Status: The game is over. It's a draw!")
                result = True
    return result


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


def read_in(t, l):
    left = False
    if t == 0:
        # computer turn
        cmd = input()
        k = []
        score = calc_score()
        while True:
            j = score.pop() if score else -1
            if j == -1 or len(k) == 2 * l + 1:
                return 0
            if j in k:
                continue
            k.append(j)
            p = set_players[0][j]
            chk = check_snake(p, left, True)
            if chk == -1:
                left = True
                chk = check_snake(p, left, True)
            if chk != -1:
                break
    else:
        # player turn
        while True:
            cmd = input()
            if re.match('-?[0-9]+', cmd) and int(cmd) in range(-l, l + 1):
                i = int(cmd)
                if i == 0:
                    return i
                j = abs(i) - 1
                p = set_players[1][j]
                left = i < 0
                chk = check_snake(p, left, False)
                if chk != -1:
                    break
                else:
                    continue
            print("Invalid input. Please try again.")

    p = set_players[t].pop(j)
    to_snake(p, left, chk == 1)
    return 1


def to_snake(p, left, reverse):
    if reverse:
        p[0], p[1] = p[1], p[0]
    if left:
        set_snake.insert(0, p)
    else:
        set_snake.append(p)


set_snake = []
turn = 0
count = {}


while True:
    set_stock = gen_set_game()
    random.shuffle(set_stock)
    set_players = [[], []]

    for i in range(7):
        set_players[0].append(set_stock.pop())
    for i in range(7):
        set_players[1].append(set_stock.pop())

    imax = get_max(set_players[0] + set_players[1])
    if imax == -1:
        continue

    turn = imax // 7  # 0 - "computer", 1 - "player"
    set_snake.append(set_players[turn].pop(imax % 7))
    turn = (turn + 1) % 2
    break

while True:
    draw_title(len(set_stock), len(set_players[0]))
    draw_snake()
    draw_player()
    if end_game():
        break
    draw_prompt(turn)

    i = read_in(turn, len(set_players[turn]))
    if i == 0 and set_stock:
        set_players[turn].append(set_stock.pop())
    turn = (turn + 1) % 2
