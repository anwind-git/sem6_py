import random


def generate_board():
    board = []
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append(0)
        board.append(row)

    queens = []
    for i in range(8):
        row = random.randint(0, 7)
        queens.append((i, row))
        board[i][row] = 1

    return queens


def check_attack(queens):
    for i in range(7):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


successful_boards = []
count = 0
while count < 4:
    board = generate_board()
    if check_attack(board):
        successful_boards.append(board)
        count += 1


def combination():
    for i, board in enumerate(successful_boards):
        print(f"Успешная комбинация {i + 1}:")
        for row in range(8):
            for col in range(8):
                if (row, col) in board:
                    print(' Q ', end=' ')
                else:
                    print(' - ', end=' ')
            print()
        print()