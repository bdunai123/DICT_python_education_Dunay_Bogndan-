def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def is_winner(cells, player):
    # Перевірка горизонталей, вертикалей та діагоналей
    for i in range(0, 9, 3):
        if all(cells[j] == player for j in range(i, i + 3)):
            return True  # Перевірка горизонталей
        if all(cells[j] == player for j in range(i, 9, 3)):
            return True  # Перевірка вертикалей
    if all(cells[i] == player for i in range(0, 9, 4)):
        return True  # Перевірка головної діагоналі
    if all(cells[i] == player for i in range(2, 7, 2)):
        return True  # Перевірка додаткової діагоналі
    return False


def is_draw(cells):
    return " " not in cells


def is_impossible(cells):
    count_x = cells.count("X")
    count_o = cells.count("O")
    return abs(count_x - count_o) >= 2


def make_move(cells, player, row, col):
    index = (row - 1) * 3 + (col - 1)
    if cells[index] == " ":
        cells[index] = player
        return True
    return False


def main():
    cells = [" "] * 9
    player = "X"

    while True:
        print_board(cells)
        coordinates = input(f"Enter the coordinates for player {player} (row col): ").split()

        if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print("You should enter two numbers!")
            continue

        row, col = map(int, coordinates)
        if not (1 <= row <= 3) or not (1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        if not make_move(cells, player, row, col):
            print("This cell is occupied! Choose another one!")
            continue

        if is_winner(cells, player):
            print_board(cells)
            print(f"{player} wins")
            break

        if is_draw(cells):
            print_board(cells)
            print("Draw")
            break

        if is_impossible(cells):
            print_board(cells)
            print("Impossible")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
