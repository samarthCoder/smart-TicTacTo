#GAME

board = [' ' for x in range(10)]
def insertletter(letter,pos):
    board[pos]=letter
def spacefree(pos):
    return board[pos] == ' '
def b_print(board):
    print('  |  |')
    print(' '+board[1] + '| ' + board[2] + '| ' + board[3])
    print('  |  |')
    print('----------')
    print('  |  |')
    print(' '+board[4] + '| ' + board[5] + '| ' + board[6])
    print('  |  |')
    print('----------')
    print('  |  |')
    print(' '+board[7] + '| ' + board[8] + '| ' + board[9])
    print('  |  |')
def winner(bo,le):
    return(bo[7] == le and bo[8] == le and bo[9] == le)or(bo[4] == le and bo[5] == le and bo[6] == le)or(bo[1] == le and bo[2] == le and bo[3] == le)or(bo[1] == le and bo[4] == le and bo[7] == le)or(bo[2] == le and bo[5] == le and bo[8] == le)or(bo[3] == le and bo[6] == le and bo[9] == le)or(bo[1] == le and bo[5] == le and bo[9] == le)or(bo[3] == le and bo[5] == le and bo[7] == le)

def p_move():
    run = True
    while run:
        move = input('pos pls')
        try:
            move = int(move)
            if spacefree(move):
                run=False
                insertletter('X',move)
            else:
                print('space occupied')
        except:
            print('pls type num')
            
def c_move():
    possible = [x for x , letter in enumerate(board) if letter == ' ' and x != 0]
    move=0

    for let in ['O','X']: # this code is mainly to block the player
        for i in possible:
            boardcopy = board[:]# selects all the things in the board and put's it in it's copy
            boardcopy[i] = let
            if winner(boardcopy,let):#i can say it plays by itself with both X and O , if X wins in the copy it gets the position or move and put O in the original
                move=i
                return move

    opencon = [] #this code is mainly  to position the O (randomly) in the corners , edges and middle 
    for i in possible:
        if i in [1,3,7,9]:
            opencon.append(i)
    if len(opencon) > 0:
        move = selectrand(opencon)
        return move
    if 5 in possible:
        move=5
        return move
    edgo = []
    for i in possible:
        if i in [2,4,6,8]:
            edgo.append(i)
    if len(edgo) > 0:
        move = selectrand(edgo)
    return move
    
def selectrand(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
def b_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return False
def main():
    print('welcome')
    b_print(board)

    while not(b_full(board)):
        if not(winner(board,'O')):
            p_move()
            b_print(board)
        else:
            print('lost')
            break
        if not(winner(board,'X')):
            move = c_move()
            if move == 0 :
                print('tie game')
                break
            else:
                insertletter('O',move)
                print('computer placed an \'o\' in position',move,':')
                b_print(board)
        else:
            print('you won')
            break
                    
    if b_full(board):
        print('tiee')
main()
