import numpy as np
import random
scoreBoard=[['','p1','p2','索引'],
            ['1',0,0,1],
            ['2',0,0,2],
            ['3',0,0,3],
            ['4',0,0,4],
            ['5',0,0,5],
            ['6',0,0,6],
            ['3條',0,0,7],
            ['4條',0,0,8],
            ['葫蘆',0,0,9],
            ['小順',0,0,10],
            ['大順',0,0,11],
            ['快艇',0,0,12],
            ['機會',0,0,13],
            ['總分',0,0,'*']]
bonusScoreCount=[0]*2
used=[[False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False],
    [False,False]]
def is3Same(dice):
    count=[0]*7
    for i in range(0,5):
        count[dice[i]]+=1
        if count[dice[i]]==3:
            return True
    return False
def is4Same(dice):
    count=[0]*7
    for i in range(0,5):
        count[dice[i]]+=1
        if count[dice[i]]==4:
            return True
    return False
def is5Same(dice):
    count=[0]*7
    for i in range(0,5):
        count[dice[i]]+=1
        if count[dice[i]]==5:
            return True
    return False
def isFull(dice):
    count=[0]*7
    # for i in range(0,5):
    #     if count.has_key(dice[i]):
    #         count[dice[i]]+=1
    #     else:
    #         count[dice[i]]==0
    has2=False
    has3=False
    for i in range(0,5):
        count[dice[i]]+=1
        if count[dice[i]]==2:
            has2=True
        if count[dice[i]]==3:
            has3=True
    return has2 & has3
def is4Increasing(dice):
    theMax=1
    now=1
    dice.sort()
    for i in range(0,4):
        if dice[i]+1==dice[i+1]:
            now+=1
            theMax=max(now,theMax)
        elif dice[i+1]>=dice[i]+2:
            now=0
    return theMax>=4

def is5Increasing(dice):
    theMax=1
    now=1
    dice.sort()
    for i in range(0,4):
        if dice[i]+1==dice[i+1]:
            now+=1
            theMax=max(now,theMax)
        elif dice[i+1]>=dice[i]+2:
            now=0
    return theMax>=5


def isValid(chooseScore, dice, player):
    if used[chooseScore][player-1]==True:
        return False
    if chooseScore == 7:
        return is3Same(dice)
    if chooseScore == 8:
        return is4Same(dice)
    if chooseScore == 9:
        return isFull(dice)
    if chooseScore == 10:
        return is4Increasing(dice)
    if chooseScore == 11:
        return is5Increasing(dice)
    if chooseScore == 12:
        return is5Same(dice)
    if chooseScore == 13:
        return True

def addSimpleScore(chooseScore,dice,player):
    total=0
    for i in dice:
        if i == chooseScore:
            total+=i
    scoreBoard[chooseScore][player]+=total
    scoreBoard[14][player]+=total
    bonusScoreCount[player-1]+=total
    

def add3Same(chooseScore,dice,player):
    scoreBoard[chooseScore][player]+=sum(dice)
    scoreBoard[14][player]+=sum(dice)

def add4Same(chooseScore,dice,player):
    scoreBoard[chooseScore][player]+=sum(dice)
    scoreBoard[14][player]+=sum(dice)

def add5Same(chooseScore,player):
    scoreBoard[chooseScore][player]+=50
    scoreBoard[14][player]+=50

def add4Increasing(chooseScore,player):
    scoreBoard[chooseScore][player]+=30
    scoreBoard[14][player]+=30

def add5Increasing(chooseScore,player):
    scoreBoard[chooseScore][player]+=40
    scoreBoard[14][player]+=40

def addFull(chooseScore,player):
    scoreBoard[chooseScore][player]+=25
    scoreBoard[14][player]+=25

def addChance(chooseScore,dice,player):
    scoreBoard[chooseScore][player]+=sum(dice)
    scoreBoard[14][player]+=sum(dice)

def processScore(chooseScore, dice, player):
    used[chooseScore][player-1]=True
    if (chooseScore >= 1) & (chooseScore <= 6):
        addSimpleScore(chooseScore,dice,player)
        return
    if chooseScore == 7:
        add3Same(chooseScore,dice,player)
        return
    if chooseScore == 8:
        add4Same(chooseScore,dice,player)
        return
    if chooseScore == 9:
        addFull(chooseScore,player)
        return
    if chooseScore == 10:
        add4Increasing(chooseScore,player)
        return
    if chooseScore == 11:
        add5Increasing(chooseScore,player)
        return
    if chooseScore == 12:
        add5Same(chooseScore,player)
        return
    if chooseScore == 13:
        addChance(chooseScore,dice,player)
        return

def printScoreBoard():
    for i in scoreBoard:
        print(i)
    print()
    print('獎分統計')
    print(bonusScoreCount[0],bonusScoreCount[1])

def reDrawFunc(dice):
    print('你要骰掉那些骰子 輸入1~5 一個一個輸 要結束輸入打0 輸入1~5以外的數視為要結束輸入')
    reDraw=[]
    reDrawDice=int(input())
    while (reDrawDice>=1)&(reDrawDice<=5):
        reDraw.append(reDrawDice-1)
        reDrawDice=int(input())
    for j in reDraw:
        dice[j]=random.randrange(1,7)
    return dice

yahzeeCount=[0]*2
for i in range(13):
    print('\n新回合')

    # 左手邊玩家
    printScoreBoard()
    print()
    player=1
    choose=1
    remainTimes=3

    # 玩家1回合開始
    dice=np.random.randint(1, 7, 5)
    while choose == 1:
        remainTimes-=1
        if remainTimes >=1:
            print('玩家'+str(player)+'你擲到的骰子是:')
            print(dice)

            print('你剩餘'+str(remainTimes)+'次重骰機會 你的選擇是?')
            print('1 重骰 2 選擇想要的分數')
            choose=int(input())
            while (choose !=1)&(choose !=2):
                print('請重新輸入')
                choose=int(input())
            if choose ==2:
                break
            dice=reDrawFunc(dice)
        else:
            print('你擲到的骰子是:')
            print(dice)
            break

    # 輸入想選的分數
    print('請選擇你要的分數 輸入1~13的數字')
    chooseScore=0
    chooseScore=int(input())
    while (chooseScore>13)|(chooseScore<1):
        print('輸入了無效的數字 請重新選擇')
        chooseScore=int(input())
    
    isManyYahtzee=False
    if is5Same(dice)&(yahzeeCount[player-1]>=1):
        scoreBoard[14][player]+=100*yahzeeCount[player-1]
        yahzeeCount[player-1]+=1
        processScore(chooseScore, dice, player)
        isManyYahtzee=True

    if isManyYahtzee==False:
        # 檢測是否合理的選擇
        skipProcess=False
        while isValid(chooseScore, dice, player)==False:
            while (chooseScore>13)|(chooseScore<1):
                print('輸入了無效的數字 請重新選擇')
                chooseScore=int(input())
            if used[chooseScore][player-1]==False:
                print('輸入了無效的選擇 確定以0分計算? y/n')
                chooseYN=input()
                while (chooseYN!='y')&(chooseYN!='n'):
                    print('請重新輸入')
                    chooseYN=input()
                if chooseYN=='y':
                    used[chooseScore][player-1]=True
                    scoreBoard[chooseScore][player]='*'
                    skipProcess=True
                    break
                else:
                    print('請重新輸入')
                    chooseScore=int(input())
                    while (chooseScore>13)|(chooseScore<1):
                        print('輸入了無效的數字 請重新選擇')
                        chooseScore=int(input())
            else:
                print('請重新輸入')
                chooseScore=int(input())
                while (chooseScore>13)|(chooseScore<1):
                    print('輸入了無效的數字 請重新選擇')
                    chooseScore=int(input())

        # 計算分數
        if skipProcess==False:
            processScore(chooseScore, dice, player)

        if bonusScoreCount[0]>=63:
            print('恭喜獲得35分的獎分')
            scoreBoard[14][player]+=35
            

#####################################################
    printScoreBoard()
    print()

    # 右手邊玩家
    player=2
    choose=1
    remainTimes=3

    # 玩家2回合開始
    dice=np.random.randint(1, 7, 5)
    while choose == 1:
        remainTimes-=1
        if remainTimes >=1:
            print('玩家'+str(player)+'你擲到的骰子是:')
            print(dice)

            print('你剩餘'+str(remainTimes)+'次重骰機會 你的選擇是?')
            print('1 重骰 2 選擇想要的分數')
            choose=int(input())
            while (choose !=1)&(choose !=2):
                print('請重新輸入')
                choose=int(input())
            if choose ==2:
                break
            dice=reDrawFunc(dice)
        else:
            print('你擲到的骰子是:')
            print(dice)
            break

    # 輸入想選的分數
    print('請選擇你要的分數 輸入1~13的數字')
    chooseScore=0
    chooseScore=int(input())
    while (chooseScore>13)|(chooseScore<1):
        print('輸入了無效的數字 請重新選擇')
        chooseScore=int(input())
    
    isManyYahtzee=False
    if is5Same(dice)&(yahzeeCount[player-1]>=1):
        scoreBoard[14][player]+=100*yahzeeCount[player-1]
        yahzeeCount[player-1]+=1
        processScore(chooseScore, dice, player)
        isManyYahtzee=True

    if isManyYahtzee==False:
        # 檢測是否合理的選擇
        skipProcess=False
        while isValid(chooseScore, dice, player)==False:
            
            if used[chooseScore][player-1]==False:
                print('輸入了無效的選擇 確定以0分計算? y/n')
                chooseYN=input()
                while (chooseYN!='y')&(chooseYN!='n'):
                    print('請重新輸入')
                    chooseYN=input()
                if chooseYN=='y':
                    used[chooseScore][player-1]=True
                    scoreBoard[chooseScore][player]='*'
                    skipProcess=True
                    break
                else:
                    print('請重新輸入')
                    chooseScore=int(input())
                    while (chooseScore>13)|(chooseScore<1):
                        print('輸入了無效的數字 請重新選擇')
                        chooseScore=int(input())
            else:
                print('請重新輸入')
                chooseScore=int(input())
                while (chooseScore>13)|(chooseScore<1):
                        print('輸入了無效的數字 請重新選擇')
                        chooseScore=int(input())


        # 計算分數
        if skipProcess==False:
            processScore(chooseScore, dice, player)

        if bonusScoreCount[0]>=63:
            print('恭喜獲得35分的獎分')
            scoreBoard[14][player]+=35

#####################################################
print('\n\n遊戲結束')
if scoreBoard[14][1]>scoreBoard[14][2]:
    print('p1 你是贏家夾到娃娃')
elif scoreBoard[14][2]>scoreBoard[14][1]:
    print('p2 你是贏家夾到娃娃')
else:
    print('和局')