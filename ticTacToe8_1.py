#########ALL THE HELPER FUNCTIONS
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

        for i in range(len(boardArr)):
            print("---", end = "")
        print("")



def isWinner(bo, le):
    #check all the rows
    for i in range(len(bo)):
        val = True
        for j in range(len(bo[0])):
            if(bo[i][j] != le):
                val = False
        if(val == True):
            #print("row win")
            return True

    #check all the columns
    for j in range(len(bo[0])):
        val = True
        for i in range(len(bo)):
            if(bo[i][j] != le):
                val = False
        if(val == True):
            #print("col win")
            return True

    #checking both the diagonals
    val = True
    for i in range (len(bo)):
        if(bo[i][i] != le):
            val = False
    if (val == True):
        #print("diagonal win")
        return True

    val = True
    for i in range (len(bo)):
        if(bo[i][len(bo[0])-i-1] != le):
            val = False
    if (val == True):
        #print("diagonal win")
        return True


def displayScore(player1Wins, player2Wins):
    print("player 1 has won {} games".format(player1Wins))
    print("player 2 has won {} games".format(player2Wins))

def winner(player1Wins, player2Wins):
    if(player1Wins> player2Wins):
        return "Player 1"
    else:
        return "Player 2"

#Function to determine if there is a winner yet
def isWinnerThreeByThree(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    return ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or # across the top
    (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or # across the middle
    (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or # across the bottom
    (bo[2][0] == le and bo[1][0] == le and bo[0][0] == le) or # down the left side
    (bo[2][1] == le and bo[1][1] == le and bo[0][1] == le) or # down the middle
    (bo[2][2] == le and bo[1][2] == le and bo[0][2] == le) or # down the right side
    (bo[2][0] == le and bo[1][1] == le and bo[0][2] == le) or # diagonal
    (bo[2][2] == le and bo[1][1] == le and bo[0][0] == le)) # diagonal

#For now assuming + is cross and o is nought. Alternates inputs, plays up to 9 moves
def isOccupied(board, pos):
    n = len(board)
    return (board[int((pos-1)/n)][(pos-1)%n] == player2Input or (board[int((pos-1)/n)][(pos-1)%n] == player1Input))

############ THE ACTUAL GAME
totalGameCount =  int(input("How many games would you like to play? Best of ________ (pick an odd number!)"))
majority = int(totalGameCount/2)+1
player1Wins = 0
player2Wins = 0
player1Input = str(input("Player one what chatacter would you like to be?"))
player2Input = str(input("Player two what chatacter would you like to be?"))
dimension = int(input("What board dimension would you like? For example, if you want a 3 by 3, enter 3!"))



currentGame = 1
while(player1Wins < majority and player2Wins < majority):
    board = createBoard(dimension)
    displayBoard(board)
    i = 0
    while(i < dimension**2):
        move = input("Player {} your move (indicate what number box):".format((i%2) +1))
        move = int(move)
        if(i % 2 == 0):
            #mapping back from number to array indices. subtracting one before division/modding
            # since everything is incremented by one and not starting at zero
            if(isOccupied(board, move)):
                print("that position is already occupied, try again!")
                #decrements so it's their move again!
                i -= 1
            else:
                board[int((move-1)/dimension)][(move-1)%dimension] = player2Input
        else:
            if(isOccupied(board, move)):
                print("that position is already occupied, try again!")
                #decrements so it's their move again!
                i -= 1
            else:
                board[int((move-1)/dimension)][(move-1)%dimension] = player1Input
        #print("i", i)
        if i>= (2*dimension-2):
            if isWinner(board, player2Input):
                print("player 1 is the winner!")
                player1Wins +=1
                i = dimension**2
            elif isWinner(board, player1Input):
                print("player 2 is the winner!")
                player2Wins +=1
                i = dimension**2
        displayBoard(board)
        i+=1

    #Checks if it's a tie right at the end:
    if((not(isWinner(board, player2Input)) and (not(isWinner(board, player1Input))))):
        print("it's a tie!")

    displayScore(player1Wins, player2Wins)
    if (player1Wins < majority and player2Wins < majority):
        print("Game {} is over, starting Game {}!".format(currentGame, currentGame+1))
        print("")
    currentGame+=1



print("Aaaand on a {}-{} decision......{} is the WINNER".format(player1Wins, player2Wins, winner(player1Wins, player2Wins)))




#features added:
#don't allow overwrites
#call tie at the end
#expand for n by n game
#what characters?

#possible features
#what characters?
#add in a sound when someone wins
#expand for n by n game
#keep track of score--OOH WHAT IF WE DID A BEST OF N KIND OF MATCH
#machine learning


