import numpy as np
import random

coord = {1: '00', 2: '01', 3: '02', 4: '10', 5: '11', 6: '12', 7: '20', 8: '21', 9: '22'}


def end_game(board):  # check if there's 0 left in the board
    if True in np.array(np.any(board == 0)):
        return True


def player1_status(board):
    result1 = np.all(board == 1, axis=0)
    result2 = np.all(board == 1, axis=1)
    cross1 = np.array([int(board[0, 0]), int(board[1, 1]), int(board[2, 2])])
    cross2 = np.array([int(board[0, 2]), int(board[1, 1]), int(board[2, 0])])
    if True in result1 or True in result2 or np.all(cross1 == 1) == True or np.all(cross2 == 1) == True:
        return True


def player2_status(board):
    result1 = np.all(board == 2, axis=0)
    result2 = np.all(board == 2, axis=1)
    cross1 = np.array([int(board[0, 0]), int(board[1, 1]), int(board[2, 2])])
    cross2 = np.array([int(board[0, 2]), int(board[1, 1]), int(board[2, 0])])
    if True in result1 or True in result2 or np.all(cross1 == 2) == True or np.all(cross2 == 2) == True:
        return True


def verify_digit(n):
    while not n.isdigit and len(n) > 1 and int(n) not in range(1, 10):
        n = input("Enter a digit please:\n ")
    return int(n)


def player1_move(board):
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


def player2_move(board):
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


def computer_move(board):
    a = random.randint(0, 2)
    b = random.randint(0, 2)
    while board[a, b] > 0:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
    board[a, b] = 2
    print(board)


def play_with_comp():
    board = np.zeros((3, 3))
    print('START!!')
    while end_game(board):
        player1_move(board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if player1_status(board):
            print('YOU WON :)')
            break
        computer_move(board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if player2_status(board):
            print('YOU LOST ):')
            break


def play_with_others():
    board = np.zeros((3, 3))
    print('START!!')
    while end_game(board):
        player1_move(board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if player1_status(board):
            print('YOU WON :)')
            break
        player2_move(board)
        if not end_game(board):
            print('GAME OVER!!')
            break
        if player2_status(board):
            print('YOU LOST ):')
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
