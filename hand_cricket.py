import random

toss=["head","tail"]
play=["batting","bowling"]

score_player_bat_first=0
score_cpu_bat_first=0
print("Welcome to Beginner Hand Cricket")

def cpu_bat_later():
    global score_player_bat_first
    cpu_score=0
    
    while cpu_score<=score_player_bat_first:
        a=random.randint(1,6)
        n=int(input("Enter a number (1-6) "))
        print()
        print("You Entered ",n)
        print("CPU entered ",a)
        print()
        
        if n==a:
            print("CPU out! You Win")
            print("CPU Score: ",cpu_score)
            print("Your Score: ",score_player_bat_first)
            break
        else:
            cpu_score+=a
            print(cpu_score)
    if cpu_score>score_player_bat_first:
        print("CPU won , CPU Successfully Chased",cpu_score,"runs")

def bat_first():
   
    while True:
        b=random.randint(1,6)
        
        a=int(input("Enter a number from 1-6: "))
        print("-------------------------")
        print("CPU entered",b)
        print("You entered",a)
        print("-------------------------")
        if a not in range(1,7):
            print("Enter a valid Number:")
        elif a!=b:
            global score_player_bat_first
            score_player_bat_first+=a
            print("Your score is ",score_player_bat_first)
           
        elif a==b:
            print("-----------------------------------------------------")
            print("You are out !! ,Your score is",score_player_bat_first)
            print()
            print("CPU has to score", score_player_bat_first +1,"runs")
            print("-----------------------------------------------------")
            break
    cpu_bat_later()

def cpu_bowl_later():
    global score_cpu_bat_first
    player_score=0
    print("You Have to Chase",score_cpu_bat_first+1,"runs")
    while player_score<=score_cpu_bat_first:
        a=random.randint(1,6)
        n=int(input("Enter a number (1-6): "))
        print('-------------------------------')
        print("You Entered ",n)
        print("CPU entered ",a)
        print('-------------------------------')
        print("Your Score: ",player_score)
        print()
        
        if n==a:
            print("You are out! CPU Wins")
            print("Your Score: ",player_score)
            print("CPU Score: ",score_cpu_bat_first)
            break
        else:
            player_score+=n
            print(player_score)
    if player_score>score_cpu_bat_first:
        print("You Win! You Successfully Chased",score_cpu_bat_first,"runs")

def bowl_first():
    global score_cpu_bat_first
    while True:
        a=int(input("Enter a Number(1-6): "))
        print()
        b=random.randint(1,6)
        if a not in range(1,7):
            print("Enter a valid Number")
            print()
        elif a==b:
            print("You Entered: ",a)
            print("CPU Entered: ",b)
            print()
            print("CPU OUT !!")
            print("CPU Score: ",score_cpu_bat_first)
            break
        elif a!=b:
            score_cpu_bat_first+=b
            print("You Entered: ",a)
            print("CPU Entered: ",b)
            print("CPU Score: ",score_cpu_bat_first)
    cpu_bowl_later()    

def toss_selection():
    toss_select=input("Input Head/Tail: ")
    print()
    a=random.choice(toss)
    print("\nToss Result:", a.capitalize())
    print()
    if toss_select.lower()==a:
        print("You Win!")
        play=input("Batting Or Bowling: ")
        if play.lower()=="batting":
            print("You Have Chosen to Bat First")
            print()
            bat_first()
        if play.lower()=="bowling":
            print("You have chosen to bowl first")
            print()
            bowl_first()
    if toss_select.lower()!=a:
        print('CPU Has won the Toss')
        b=random.choice(play)
        if b=="batting":
            print("CPU Has Decided to Bat First")
            print()
            bowl_first()
        elif b=="bowling":
            print("CPU Has Decided to Bowl First")
            print()
            bat_first()
            
    
toss_selection()
