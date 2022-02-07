import random


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

print("=" * 70)
print(f"Stock size: {len(set_stock)}")
print(f"Computer pieces: {len(set_players[0])}\n")
print(set_snake[0])
print("\nYour pieces:")
for i in range(1, len(set_players[1]) + 1):
    print(f"{i}:{set_players[1][i - 1]}")
print()
if status[turn] == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
else:
    print("Status: It's your turn to make a move. Enter your command.")