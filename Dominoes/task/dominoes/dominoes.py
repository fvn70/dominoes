import random
import re


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


def draw_prompt(t):
    if t == 0:
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")


def end_game(comp, play, snake):
    result = False
    if len(comp) == 0:
        print("Status: The game is over. The computer won!")
        result = True
    elif len(play) == 0:
        print("Status: The game is over. You won!")
        result = True
    else:
        if snake[0][0] == snake[len(snake) - 1][1]:
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


def read_in(t, l):
    while True:
        cmd = input()
        if t == 0:
            return random.randint(-l, l)
        if re.match('-?[0-9]+', cmd) and int(cmd) in range(-l, l + 1):
            return int(cmd)
        print("Invalid input. Please try again.")


set_game = gen_set_game()
set_snake = []
status = ["computer", "player"]
turn = 0

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
    draw_snake(set_snake)
    draw_player(set_players[1])
    if end_game(set_players[0], set_players[1], set_snake):
        break
    draw_prompt(turn)

    i = read_in(turn, len(set_players[turn]))
    if i == 0:
        set_players[turn].append(set_stock.pop())
    elif i > 0:
        set_snake.append(set_players[turn].pop(i - 1))
    else:
        set_snake.insert(0, set_players[turn].pop(-i - 1))
    turn = (turn + 1) % 2
