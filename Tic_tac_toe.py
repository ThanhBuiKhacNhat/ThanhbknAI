"""Trò chơi tic-tac-toe được chơi trên lưới 3x3. Trò chơi được chơi bởi hai người chơi, thay phiên nhau. 
Người chơi đầu tiên đánh dấu di chuyển bằng một cây thánh giá, người thứ hai với một vòng tròn. 
Người chơi nào tạo thành một chuỗi ba dấu ngang, dọc hoặc chéo sẽ thắng. 
Chương trình này vẽ bảng trò chơi, hỏi người dùng tọa độ của điểm đánh dấu tiếp theo,
thay đổi người chơi sau mỗi lần di chuyển thành công và hiển thị người chiến thắng."""
#ThanhBuifromHuewithlove
import random
#Ve ban co
def drawboard(board):
    print(board[7] + '|'+ board[8] + '|' + board[9])
    print("-+-+-+")
    print(board[4] + '|'+ board[5] + '|' + board[6])
    print("-+-+-+")
    print(board[1] + '|'+ board[2] + '|' + board[3])


#Nguoi choi chon O or X
def inputplayerletter():
    letter = ''
    while not ( letter == 'X' or letter  == 'O'):
        print("Do you want to be X or O ?")
        letter = input().upper()
    if letter  == 'X':
        return['X','O']
    else:
        return['O','X']


#Chon nguoi di truoc
def whogowfirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

#Ve ky tu len ban co
def makemove(board, letter,move):
    board[move]=letter

#Kiem tra xem nguoi choi da thang hay chua
def iswinner(bo,le):
    return (bo[7] == le and bo[8]== le and bo[9] == le) or (bo[4] == le and bo[5]== le and bo[6] == le) or (bo[1] == le and bo[2]== le and bo[3] == le) or (bo[1] == le and bo[5]== le and bo[9] == le) or (bo[7] == le and bo[5]== le and bo[3] == le) or (bo[1] == le and bo[4]== le and bo[7] == le) or (bo[2] == le and bo[5]== le and bo[8] == le) or (bo[3] == le and bo[6]== le and bo[9] == le)

#Copy du lieu cuar board
def getboardcopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

#Kiem tra xem ô trên bàn cờ còn không 
def isSpacefree(board,move):
    return board[move]  == ' '


#player nhập một bước đi
def getPlayermove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpacefree(board,int(move)):
        print("What is your next move ?(1-9)")
        move = input()
    return int(move)


#Chọn một bước đi từ tập hợp các bước đi
def chooseRandomMoveFromList(board , moveList):
    possibleMove = []
    for i in moveList:
        if isSpacefree(board,i):
            possibleMove.append(i)
    if len(possibleMove)!= 0:
        return random.choice(possibleMove)
    else:
        return None

#Tạo đoạn mã AI cho computer:
def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
#Kiểm tra máy tính có thể thắng trong một bước đi hay không 
    for i in range(1,10):
        boardCopy = getboardcopy(board)
        if  isSpacefree(boardCopy,i):
            makemove(boardCopy, computerLetter,i)
            if iswinner(boardCopy, computerLetter):
                return i
#Kiểm tra xem người chơi có thể thắng trong một bước đi hay không
    for i in range(1,10):
        boardCopy = getboardcopy(board)
        if isSpacefree(boardCopy,i):
            makemove(boardCopy,playerLetter,i)
            if iswinner(boardCopy,playerLetter):
                return i
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    if isSpacefree(board,5):
        return 5
    return chooseRandomMoveFromList(board,[2,4,6,8])

   #Kiem tra xem ban co da day hay chua
def isBoardfull(board):
    for i  in range(1,10):
        if isSpacefree(board,i):
            return False 
    return True 


print("Welcome to Tic Tac Toe!")
while True:
    #Thiet lap lai ban co
    theBoard = [' ']*10  
    playerLetter, computerLetter = inputplayerletter()
    turn = whogowfirst()
    print("The"+ turn + 'will go first!!!')
    gameIsplaying = True
    while gameIsplaying:
        if turn == 'player':
            drawboard(theBoard)
            move = getPlayermove(theBoard)
            makemove(theBoard,playerLetter,move)
            if iswinner(theBoard,playerLetter):
                drawboard(theBoard)
                print("Hooray!You have won the game!")
                gameIsplaying = False
            else:
                if isBoardfull(theBoard):
                    drawboard(theBoard)
                    print("The game is tie!")
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard,computerLetter)
            makemove(theBoard,computerLetter,move)
            if iswinner(theBoard,computerLetter):
                drawboard(theBoard)
                print("The computer has beaten you !You lose =(")
                gameIsplaying = False
            else:
                if isBoardfull(theBoard):
                    drawboard(theBoard)
                    print("The game is a tie !")
                    break
                else:
                    turn = 'player'
    print("Do you want to play again !")
    if not input().lower().startswith('y'):
        break
