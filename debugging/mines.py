#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_non_mine_cells = width * height - mines
        self.revealed_non_mine_cells = 0

    def print_board(self, reveal=False):
        # Print column indices
        print(' '.join(str(i) for i in range(self.width)))
        # Print row indices only
        for y in range(self.height):
            print(y)

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True  # Cell already revealed, move on
        if (y * self.width + x) in self.mines:
            return False  # Hit a mine

        self.revealed[y][x] = True
        self.revealed_non_mine_cells += 1

        # Reveal adjacent cells if there are no nearby mines
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def check_win(self):
        return self.revealed_non_mine_cells == self.total_non_mine_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print(f"Invalid coordinates! Please enter values between 0 and {self.width-1} for x, and 0 and {self.height-1} for y.")
                    continue
                if self.revealed[y][x]:
                    print("This cell is already revealed. Choose a different cell.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numeric coordinates.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
