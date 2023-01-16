"HAND CRICKET PROJECT"
# RULES OF PLAYING HAND CRICKET:-

# RULE 1: IF BATSMEN AND BOWLER HAVE THE SAME NUMBER THEN THE BATSMEN IS OUT
# RULE 2:IF BATSMEN HITS ZERO AND BOWLER BOWLS ANY NUMBER OTHER THAN ZERO THEN THE BATSMEN WILL GET THE BOWLED NUMBER
# RULE 3:BATSMEN CAN hit in range of [0,6]
# RULE 4:BOWLER CAN throw only in range of [0,6]
# RULE 5:IF ONE PLAYER HITS X RUNS THEN OTHER PLAYER NEEDS X+1 RUNS TO WIN
# RULE 6:IF BOTH PLAYERS SCORES ARE EQUAL THEN ITS A DRAW
"NOTE :THERE ARE NO LIMITS TO NUMBER OF BALLS THAT A BOWLER CAN BOWL "

import random
player_score =0
coumpter_score=0
players=[0,0,0]
cplayers=[0,0,0]
i=0
j=0
cs=0
ps=0
t=["heads","tails"]
c=["bat","ball"]
print("lets play hand cricket !!!!")
#TOSS SECTION
player_toss=input("enter your choice for toss heads/tails : ").lower()
rand_toss=random.randint(0,1)
comp_toss=random.randint(0,1)

if(player_toss==t[rand_toss]):
    print("you won the toss!!!!")
    choice=input("bat or ball?? ").lower()
    if(choice=="bat"):
        comp_choice=1
    else:
        comp_choice=0
    print("you chose to ",choice)
else:
    print("computer won the toss!!")
    comp_choice=random.randint(0,1)
    if(comp_choice==0):
        choice="ball"
    else:
        choice="bat"
    print("computer chose to ",c[comp_choice])

# BATTING IF YOU CHOSE TO BAT OR COMPUTER CHOSE TO BALL
if(choice=="bat" or c[comp_choice]=="ball"):

    print("you are batting : ")
    while True:
        
        player_bat=int(input("enter runs between 0 to 6 which you want to hit :"))
        computer_bowl=random.randint(0,6)
        if(player_bat!=computer_bowl):
            if(player_bat==0):
                player_score+=computer_bowl
                ps+=computer_bowl
                print("player ",(i+1),"hit a ",player_bat)
            else:
                player_score+=player_bat
                ps+=player_bat
                print("player ",(i+1),"hit a ",player_bat)
        else:
            players[i]=player_score
            print("player ",(i+1),"is out !!! and scored: ",players[i])
            player_score=0
            i+=1
        if(i==3):
            break
    print("your score = ",ps," computer needs ",ps+1," runs to win")

    print("you are bowling ")
    while True:
        player_bowl=int(input("enter an integer between 0 to 6 :"))
        computer_bat=random.randint(0,6)
       
        if(player_bowl!=computer_bat):
            
            if(computer_bat==0):
                coumpter_score+=player_bowl
                cs+=player_bowl
                print("comp player",(j+1)," hit a ",computer_bat)
            else:
                coumpter_score+=computer_bat
                cs+=computer_bat
                print("comp player",(j+1)," hit a ",computer_bat)
        else:
            cplayers[j]=coumpter_score
            print(" computer player ",(j+1),"is out !!! and scored: ",cplayers[j])
            coumpter_score=0
            j+=1
        if(j==3):
            break
        if(cs>ps):
            print("computer scored ",cs)
            print("computer won the match by ",cs-ps)
            quit()
    
    print(cs)
# BOWLING IF COMPUTER CHOSE TO BAT OR YOU CHOSE TO BOWL
else:
    print("you are bowling ")
    while True:
        player_bowl=int(input("enter an integer between 0 to 6 :"))
        computer_bat=random.randint(0,6)
        if(player_bowl!=computer_bat):
            if(computer_bat==0):
                coumpter_score+=player_bowl
                cs+=player_bowl
                print("comp player",(j+1)," hit a ",computer_bat)
            else:
                coumpter_score+=computer_bat
                cs+=computer_bat
                print("comp player",(j+1)," hit a ",computer_bat)
        else:
            cplayers[j]=coumpter_score
            print("computer player ",(j+1),"is out !!! and scored: ",cplayers[j])
            coumpter_score=0
            j+=1
        if(j==3):
            break
    print("computer scored ",cs," you need ",cs+1," runs to win ")
    print("you are batting ")
    while True:
        
        player_bat=int(input("enter runs between 0 to 6 which you want to hit :"))
        computer_bowl=random.randint(0,6)
        if(player_bat!=computer_bowl):
            if(player_bat==0):
                player_score+=computer_bowl
                ps+=computer_bowl
                print("player ",(i+1),"hit a ",player_bat)
            else:
                player_score+=player_bat
                ps+=player_bat
                print("player ",(i+1),"hit a ",player_bat)
        else:
            players[i]=player_score
            print("player ",(i+1),"is out !!! and scored: ",players[i])
            player_score=0
            i+=1
        if(i==3):
            break
        if(ps>cs):
            print("your score ",ps)
            print("you won the match by ",ps-cs)
            quit()
    
    print(ps)
if(ps>cs):
    print("you wonn the match!!")
elif(cs==ps):
    print("match is a draw!!!")
else:
    print("you lost the match!!")
