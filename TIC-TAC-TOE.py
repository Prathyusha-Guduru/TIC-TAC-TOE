print("******************TIC-TAC-TOE******************")
print("********************WELCOME********************\n\n")

def is_even(num):
    if(num % 2 == 0):
        return True
    else:
        return False

def is_win(arr):
    if(arr[0][0] == arr[1][1] == arr[2][2]):
        return True
    elif(arr[0][2] == arr[1][1] == arr[2][0]):
        return True
    elif(arr[0][0] == arr[0][1] == arr[0][2]):
        return True
    elif(arr[1][0] == arr[1][1] == arr[1][2]):
        return True
    elif(arr[2][0] == arr[2][1] == arr[2][2]):
        return True
    else:
        return False

def print_tic_tac_toe(tic_tac_toe):
    print('{} | {} | {}\n--+---+--\n{} | {} | {}\n--+---+--\n{} | {} | {}'.format(tic_tac_toe[0][0], tic_tac_toe[0][1],
                                                                                  tic_tac_toe[0][2], tic_tac_toe[1][0],
                                                                                  tic_tac_toe[1][1], tic_tac_toe[1][2],
                                                                                  tic_tac_toe[2][0], tic_tac_toe[2][1],
                                                                                  tic_tac_toe[2][2]))

row_1 = [1,2,3]
row_2 = [4,5,6]
row_3 = [7,8,9]
tic_tac_toe = [row_1,row_2,row_3]
p1 = 'X'
p2 = 'O'


print_tic_tac_toe(tic_tac_toe)
print('\n')
print("Player 1 : X\nPlayer 2 : O\n")



player_1_moves = 5
player_2_moves = 4
total_moves = 9

while(total_moves != 0):
    if(is_even(total_moves)==True):
        row, position = input("Player 2's turn:\nAt which position do you want to place 'O'\nEnter row number first and then the position:\t").split(' ')
        row, position = int(row), int(position)
        tic_tac_toe[row-1][position-1] = 'O'
        print_tic_tac_toe(tic_tac_toe)
        if(is_win(tic_tac_toe)):
            print('Game Over\nPlayer 2 is the winner')
            raise SystemExit
        else:
            pass
    elif(is_even(total_moves)==False):
        row, position = input("Player 1's turn:\nAt which position do you want to place 'X'\nEnter row number first and then the position:\t").split(' ')
        row, position = int(row), int(position)
        tic_tac_toe[row - 1][position - 1] = 'X'
        print_tic_tac_toe(tic_tac_toe)
        if (is_win(tic_tac_toe)):
            print('Game Over\nPlayer 1 is the winner')
            raise SystemExit
        else:
            pass
    total_moves -= 1







