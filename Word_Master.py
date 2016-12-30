import random
import urllib.request

## Make sure you have wifi connectivity when playing this game
# The line below sets up the global variable "lets" that contains all of the letters of the alphabet
lets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
class setUp(object): # A class that sets up the game

    def __init__(self):
        pass
    
    def drawBoard(self,board): #Draws the game board
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------') 
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[0]+' |'+ board[1]+ '  |' +board[2]+'  |'+board[3]+'  |'+ board[4]+ '  |' +board[5]+ '  |'+board[6]+'  |'+ board[7]+ '  |' +board[8]+'  |'+board[9]+'  |'+ board[10]+ ' |' +board[11]+' |'+board[12]+' |'+board[13]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[14]+'|'+ board[15]+ ' |' +board[16]+' |'+board[17]+' |'+ board[18]+ ' |' +board[19]+ ' |'+board[20]+' |'+ board[21]+ ' |' +board[22]+' |'+board[23]+' |'+ board[24]+ ' |' +board[25]+' |'+board[26]+' |'+board[27]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[28]+'|'+ board[29]+ ' |' +board[30]+' |'+board[31]+' |'+ board[32]+ ' |' +board[33]+ ' |'+board[34]+' |'+ board[35]+ ' |' +board[36]+' |'+board[37]+' |'+ board[38]+ ' |' +board[39]+' |'+board[40]+' |'+board[41]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[42]+'|'+ board[43]+ ' |' +board[44]+' |'+board[45]+' |'+ board[46]+ ' |' +board[47]+ ' |'+board[48]+' |'+ board[49]+ ' |' +board[50]+' |'+board[51]+' |'+ board[52]+ ' |' +board[53]+' |'+board[54]+' |'+board[55]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[56]+'|'+ board[57]+ ' |' +board[58]+' |'+board[59]+' |'+ board[60]+ ' |' +board[61]+ ' |'+board[62]+' |'+ board[63]+ ' |' +board[64]+' |'+board[65]+' |'+ board[66]+ ' |' +board[67]+' |'+board[68]+' |'+board[69]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[70]+'|'+ board[71]+ ' |' +board[72]+' |'+board[73]+' |'+ board[74]+ ' |' +board[75]+ ' |'+board[76]+' |'+ board[77]+ ' |' +board[78]+' |'+board[79]+' |'+ board[80]+ ' |' +board[81]+' |'+board[82]+' |'+board[83]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('|'+' '+board[84]+'|'+ board[85]+ ' |' +board[86]+' |'+board[87]+' |'+ board[88]+ ' |' +board[89]+ ' |'+board[90]+' |'+ board[91]+ ' |' +board[92]+' |'+board[93]+' |'+ board[94]+ ' |' +board[95]+' |'+board[96]+' |'+board[97]+' |')
        print ('|'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |'+'   |'+'   |   |'+'   |   |')
        print ('-----------'+'-----------'+'-----------'+'-----------'+'------------')
          
    def copyBoard(self,board): #Makes a copy of the board to test different scenarios
        global copyBoard
        copyBoard=[]
        for i in board:
            copyBoard.append(i)
        return copyBoard
    
    def setUpDict(self): #Sets up the letter value dictionary
        l='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        vals='1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10'.split(' ')
        global letterValueDict
        letterValueDict={} #Empty dictionary that will contain each value
        for h in (range(0,26)):
            letterValueDict[l[h]]=vals[h]  
            
    def assignLetters(self): #Assigns letters to each player
        global player
        player=[]
        for key,values in letterValueDict.items():
            player.append(key)
        random.shuffle(player) #I am shuffling all of the letters (keys)  
        return player[0:7]
    
    def playerLetters(self,numberPlayers): #Informs users of different players
        global playerLetters
        playerLetters=[]
        for i in range(numberPlayers):
            playerLetters.append(game.assignLetters())
            print('Player '+str(i+1)+' your letters are '+str(playerLetters[i]))
        return playerLetters
    
    def playerScoresDict(self,numberPlayers): #Dictionary that contains the scores of each player
        global playerScores
        playerScores={}
        for i in range(numberPlayers):
            playerScores[str(i+1)]=0
        return playerScores
        
    
    def makeMove(self,playerTurn,board,allLetters,playerScoresDict): #Used to make moves for the player !!! MAKE SURE TO MAKE CHECKS SO THAT CODE DOES NOT BREAK
        def setUp(board,playerTurn,allLetters):
            copyBoard=game.copyBoard(board)
            game.drawBoard(board)
            print('Player '+str(playerTurn+1)+" it's your turn and your letters are: ")
            return board,copyBoard
    
        def enterWord(board,copyBoard,allLetters,playerScoresDict): # Make sure to enter the letters that you will be using on the board too
            global wordString
            letList=[] #The list that is used to determine which letters were used
            entered=[]# Used to check the entered letters
            copyBoard=game.copyBoard(copyBoard) #Copies the board
            print(allLetters[playerTurn])
            try: #If an error occurs, it will prompt the user for the letters they would like to input again
                skip=input('Would you like to PLAY your turn, SKIP, or EXIT? ')[0].lower()
                if skip=='s':
                    allLetters[playerTurn]=game.passLet(allLetters[playerTurn])
                    print ('Player '+str(playerTurn+1)+' your letters are now: ')
                    print(allLetters[playerTurn])
                    return(board)
                elif skip=='e':
                    return 'exit' #add functions
                
                wordLength=int(input("Enter the number of letters you would like to add to the board: "))
                word=input("Enter position numbers and letters in the form 'position letter' (ex: M11) with no spaces and separated by spaces:").split(" ")
                wordString=input("Enter the resultant word you are trying to spell: ").upper()   
                for i in range(wordLength): #iterates through each entry in word and generates a preview of the word
                    pos=int(word[i][1:])
                    let=word[i][0].upper()
                    entered.append(let)    
                    if len(word[i])==3:
                        copyBoard[pos]=let+' '
                    else:   
                        copyBoard[pos]=let
            except:
                print ('Ooops, you may have entered an invalid input earlier.')
                enterWord(board,copyBoard,allLetters,playerScoresDict)
            
            
            entered=''.join(entered)
            game.drawBoard(copyBoard)
            ans=input ('Is this the word that you expected on the board? (y/n) ')[0].lower()
            valid=game.moveCheck(entered,allLetters[playerTurn],board)
            if ans=='n' or valid=='n': #Checks validity of the entered word. Refer to game.moveCheck
                print ('Re-input your letters again!')
                for i in range(wordLength): #Fixes the board so that the person can make decisions based on the correct version of the board
                    pos=int(word[i][1:])
                    copyBoard[pos]=str(pos)
                game.drawBoard(copyBoard)
                enterWord(board,copyBoard,allLetters,playerScoresDict)
            else:
                count=game.scoring(wordString) #Counts the points
                game.scoreKeeper(count,playerTurn,playerScoresDict) #Keeps score of the players
                for i in range(wordLength): #iterates through each entry in word and alters the board layout 
                    pos=int(word[i][1:])
                    let=word[i][0]
                    letList.append(let)
                    if len(word[i])==3:
                        board[pos]=let+' '
                    else:   
                        board[pos]=let
                allLetters[playerTurn]=game.replaceLet(letList,allLetters[playerTurn]) #Replenishes supply of letters
                print ('Your letters are now' + str(allLetters[playerTurn]))
            return board
        setUp(board,playerTurn,allLetters)
        a=enterWord(board,copyBoard,allLetters,playerScoresDict)
        if a=='exit':
            return 'exit'
        return board
    
    def moveCheck(self,entered,playerLetters,board): #Takes argument of the word inputed and the player's letters
        entered=entered.lower()
        url='http://dictionary.com/browse/'+entered
        for letter in entered: #Checks if the word is in the player's letters.
            if letter.upper() not in playerLetters:
                print ('It seems that word is not valid!')
                return 'n'
        try: #The try statement checks dictionary.com to see if a word is valid word. If an error pops up, the word is not valid.
            response=urllib.request.urlopen(url) #Opening the url for the word
        except:
            print ('The word is not valid')
            return 'n' 
       
        return None
    
    def scoring(self,wordString): #Checks every single inputed word in order to score the input
        count=0
        for char in wordString:
            count=count+int(letterValueDict[char])
        return count
    
    def scoreKeeper(self,count,playerTurn,playerScores): #Contains a hash table that contains each score for every player
        playerScores[str(playerTurn+1)]=playerScores[str(playerTurn+1)]+count #Increments scores
        for key,value in playerScores.items():
            print ('Player '+str(key)+': '+str(value)+ ' points')
        return playerScores
    
    def replaceLet(self,letList,allLetters):# A method that replaces the letter of the player who just played
        random.shuffle(lets) #Shuffles arrangements of the letters
        for char in letList: #Removes the used letters
            allLetters.remove(char)
        for i in range(0,len(letList)): #Replenishes letters
            allLetters.append(lets[i])
        return allLetters
    
    def passLet(self,allLetters): #Adds letters for the person who just passed
        random.shuffle(lets)
        allLetters=allLetters[0:5]+lets[0:2]
        return allLetters

class gameStart(object):
    def boardNums(self): #Creates the array of board position numbers
        board=[]
        for i in range(0,100):
            board.append(str(i))
        return board
    def setUp(self,board): #Calls to the set up class above
        global game
        game=setUp()
        game.drawBoard(board)
        game.setUpDict()     
        while(1): #Setting up the number of players in the game
            try:
                num=int(input('Enter the number of people playing: '))
                break
            except:
                pass
        allLetters=game.playerLetters(num) #Assigns all letters for players
        playerScores=game.playerScoresDict(num)
        game.drawBoard(board)
        play=random.randint(0,num-1)
        return play, board, allLetters,playerScores,num 
    def gameRun(self,play,board,allLetters,playerScores,num): #Runs the actual game
        while(1):    
            board=game.makeMove(play,board,allLetters,playerScores)
            if board=='exit':
                print ("Thank you for playing word-master. We hope you enjoyed your experience!")
                max=0
                for key,value in playerScores.items():
                    print ('Player '+str(key)+': '+str(value)+ ' points')
                    if playerScores[key]>max:
                        max=value
                        winner=key
                print ('Player '+ str(winner)+', with '+str(max)+' points, is the winner!!!!')
                break
            play+=1
            if play>=num:
                play=0

#Calls the methods from the classes to start actual game
start=gameStart()
board=start.boardNums()
play,board,allLetters,playerScores,num=start.setUp(board)
final=start.gameRun(play,board,allLetters,playerScores,num)
