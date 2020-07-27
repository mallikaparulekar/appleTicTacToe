#creates the board of n by n dimensions, and fills with numbers from 1...n^2
def createBoard(n):
    return [[(i+1 + j*n) for i in range (n)]for j in range(n)]

#print(createBoard(3))

#input is the n by n array, output is printed on the console.
def displayBoard(boardArr):
    for i in range(len(boardArr)):
        for j in range(len(boardArr[i])):
            if(j < (len(boardArr))-1):
                #says unexpected syntax for the end = part (which prevents it from going to a new line and adds the separator), but code still works
                print(boardArr[i][j], end = ' | ')
            else:
                print(boardArr[i][j])


        print("----------")

board = createBoard(3)
displayBoard(board)


#For now assuming + is cross and o is nought. Alternates inputs, plays up to 9 moves
i = 0
while(i < 9):
    move = input("Player {} your move (indicate what number box):".format((i%2) +1))
    move = int(move)
    if(i % 2 == 0):
        #mapping back from number to array indices. subtracting one before division/modding
        # since everything is incremented by one and not starting at zero
        board[int((move-1)/3)][(move-1)%3] = "+"
    else:
        board[int((move-1)/3)][(move-1)%3] = "o"

    displayBoard(board)
    i+=1







