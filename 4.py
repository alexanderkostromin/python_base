"""
Задача 4. Крестики нолики

Напишите программу, которая реализует игру Крестики-нолики.

Ваши классы в этой задаче могут выглядеть так:

class Cell:
   #  Клетка, у которой есть значения
   #   - занята она или нет
   #   - номер клетки

class Board:
   #  Класс поля, который создаёт у себя экземпляры клетки

class Player:
   #  У игрока может быть
   #   - имя
   #   - на какую клетку ходит
"""

class Cell:
    def __init__(self, number):
        self.number = number
        self.empty = False
        self.player_symbol = None

    def occupy(self, symbol):
        self.empty = True
        self.player_symbol = symbol

    def __str__(self):
        return self.player_symbol if self.empty else str(self.number)


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print("Текущее поле:")
        for i in range(3):
            row = self.cells[i*3:(i+1)*3]
            print(" | ".join(str(cell) for cell in row))
            if i < 2:
                print("---------")

    def is_winner(self, symbol):
        winning_combinations = [
            [self.cells[0], self.cells[1], self.cells[2]],
            [self.cells[3], self.cells[4], self.cells[5]],
            [self.cells[6], self.cells[7], self.cells[8]],
            [self.cells[0], self.cells[3], self.cells[6]],
            [self.cells[1], self.cells[4], self.cells[7]],
            [self.cells[2], self.cells[5], self.cells[8]],
            [self.cells[0], self.cells[4], self.cells[8]],
            [self.cells[2], self.cells[4], self.cells[6]],
        ]

        return any(all(cell.player_symbol == symbol for cell in combination) for combination in winning_combinations)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board, cell_number):
        if 1 <= cell_number <= 9:
            cell = board.cells[cell_number - 1]
            if not cell.empty:
                cell.occupy(self.symbol)
                return True
            else:
                print(f"Клетка {cell_number} уже занята!")
        else:
            print("Неверный номер клетки. Введите номер от 1 до 9")
        return False


def play_game():
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "О")
    current_player = player1

    for turn in range(9):
        board.display()
        move_successful = False
        while not move_successful:
            try:
                cell_number = int(input(f"{current_player.name}, введите номер клетки (1-9): "))
                move_successful = current_player.make_move(board, cell_number)
            except ValueError:
                print("Введите правильный номер.")

        if board.is_winner(current_player.symbol):
            board.display()
            print(f"{current_player.name} выиграл!")
            return

        current_player = player2 if current_player == player1 else player1

    board.display()
    print("Ничья!")


if __name__ == "__main__":
    play_game()
