import numpy as np
import random

coord = {1: '00', 2: '01', 3: '02', 4: '10', 5: '11', 6: '12', 7: '20', 8: '21', 9: '22'}


def verify_digit(n):
    while not n.isdigit and len(n) > 1 and int(n) not in range(1, 10):
        n = input("Enter a digit please:\n ")
    return int(n)


class Player1(object):
    def __init__(self, name):
        self.name = name

    def enter_info(self):
        name = input("Player1's name: ")
        self.name = name

    def player_status(self, board):
        result1 = np.all(board == 1, axis=0)
        result2 = np.all(board == 1, axis=1)
        cross1 = np.array([int(board[0, 0]), int(board[1, 1]), int(board[2, 2])])
        cross2 = np.array([int(board[0, 2]), int(board[1, 1]), int(board[2, 0])])
        if True in result1 or True in result2 or np.all(cross1 == 1) == True or np.all(cross2 == 1) == True:
            return True

    def player_move(self, board):
        num = input()
        num = verify_digit(num)
        nb = coord[num]
        while board[int(nb[0]), int(nb[1])] > 0:
            print('Take another move please!!')
            num = input()
            num = verify_digit(num)
            nb = coord[num]
        board[int(nb[0]), int(nb[1])] = 1
        print(board)


class Player2(Player1):
    def __init__(self, name):
        super().__init__(name)


    def enter_info(self):
        name = input("Player2's name: ")
        self.name = name

    def player_status(self, board):
        result1 = np.all(board == 2, axis=0)
        result2 = np.all(board == 2, axis=1)
        cross1 = np.array([int(board[0, 0]), int(board[1, 1]), int(board[2, 2])])
        cross2 = np.array([int(board[0, 2]), int(board[1, 1]), int(board[2, 0])])
        if True in result1 or True in result2 or np.all(cross1 == 2) == True or np.all(cross2 == 2) == True:
            return True

    def player_move(self, board):
        num = input()
        num = verify_digit(num)
        nb = coord[num]
        while board[int(nb[0]), int(nb[1])] > 0:
            print('Take another move please!!')
            num = input()
            num = verify_digit(num)
            nb = coord[num]
        board[int(nb[0]), int(nb[1])] = 2
        print(board)


class Computer(Player1):
    def __init__(self, name):
        super().__init__(name)

    def computer_move(self, board):
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        while board[a, b] > 0:
            a = random.randint(0, 2)
            b = random.randint(0, 2)
        board[a, b] = 2
        print(board)


player1 = Player1('Player1')
player2 = Player2('Player2')
computer = Computer('Computer')


def end_game(board):  # check if there's 0 left in the board
    if True in np.array(np.any(board == 0)):
        return True


def play_with_comp():
    board = np.zeros((3, 3))
    print('START!!')
    while end_game(board):
        Player2.player_move(player2, board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if Player2.player_status(player2, board):
            print(f'{player2.name} WON :)')
            break
        Computer.computer_move(computer, board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if Computer.player_status(computer, board):
            print('YOU LOST ):')
            break


def play_with_others():
    Player1.enter_info(player1)
    Player2.enter_info(player2)
    board = np.zeros((3, 3))
    print('START!!')
    while end_game(board):
        Player1.player_move(player1, board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if Player1.player_status(player1, board):
            print(f'{player1.name} WON :)')
            break
        Player2.player_move(player2, board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if Player2.player_status(player2, board):
            print(f'{player2.name} WON :)')
            break


def intro():
    start = input("Two players :A and One player: B\n")
    while start.lower() != 'a' and start.lower() != 'b':
        start = input("Two players :A and One player: B\n")
    return start.lower()


def main():
    start = intro()
    if start == 'a':
        play_with_others()
    else:
        play_with_comp()


if __name__ == '__main__':
    main()
