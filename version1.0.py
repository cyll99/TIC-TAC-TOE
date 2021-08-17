import numpy as np
import random

def end_game(board):#check if there's 0 left in the board
    if True in np.array(np.any(board == 0)):
        return True

def player1_status(board):
    result1 = np.all(board == 1, axis=0)
    result2 = np.all(board == 1, axis=1)
    cross1 = np.array([int(board[0, 0]), int(board[1, 1]), int(board[2, 2])])
    cross2 = np.array([int(board[0, 2]), int(board[1, 1]), int(board[2, 0])])
    if True in result1 or True in result2 or np.all(cross1 == 1)==True or np.all(cross2 == 1)==True:
        return True

def player2_status(board):
    result1 = np.all(board == 2, axis=0)
    result2 = np.all(board == 2, axis=1)
    cross1 = np.array([int(board[0, 0]), int(board[1, 1]), int(board[2, 2])])
    cross2 = np.array([int(board[0, 2]), int(board[1, 1]), int(board[2, 0])])
    if True in result1 or True in result2 or np.all(cross1 == 2)==True or np.all(cross2 == 2)==True:
        return True

def verify_digit(n):
    while not n.isdigit and len(n)<2:
        n = input("Input 2 digits please:\n ")
    return int(n)

def move(board):
    num = input()
    verify_digit(num)
    while board[int(num[0]), int(num[1])] > 0 :
        print('Take another move please!!')
        num = input()
        verify_digit(num)
    board[int(num[0]), int(num[1])] = 1
    print(board)

def computer_move(board):
    a = random.randint(0,2)
    b= random.randint(0,2)
    while board[a,b]>0:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
    board[a,b] = 2
    print(board)


def play():
    board = np.zeros((3, 3))
    print('START!!')
    while end_game(board):
        move(board)
        if player1_status(board):
            print('YOU WON :)')
            break
        computer_move(board)
        if player2_status(board):
            print('YOU LOST ):')
            break

    print('GAME OVER!!')


def main():
    play()

if __name__ == '__main__':
    main()

