import random
import re

def read_in(t, l):
    while True:
        cmd = input()
        if t == 0:
            return random.randint(-l, l)
        if re.match('-?[0-9]+', cmd) and int(cmd) in range(-l, l + 1):
            return int(cmd)
        print("Invalid input. Please try again.")

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

set_snake = []
turn = 0

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

    if set_comp[imax_comp][0] > set_player[imax_player][0]:
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
    draw_snake(set_snake)
    draw_player(set_player)
    if end_game(set_comp, set_player, set_snake):
        break
    draw_prompt(turn)

    l = len(set_player) if turn == 1 else len(set_comp)
    i = read_in(turn, l)

    # do turn
    if turn == 0:
        if i == 0:
            set_comp.append(set_stock.pop())
        elif i > 0:
            set_snake.append(set_comp.pop(i - 1))
        else:
            set_snake.insert(0, set_comp.pop(-i - 1))
    else:
        if i == 0:
            set_player.append(set_stock.pop())
        elif i > 0:
            set_snake.append(set_player.pop(i - 1))
        else:
            set_snake.insert(0, set_player.pop(-i - 1))
    turn = (turn + 1) % 2

