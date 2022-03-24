
list =['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']

def loop_gaming():
    global list
    while True:
        print(list)
        print("**player one**")
        player1=input("enter your num1 and num2 saparated with comma \n or enter num1 only: ").replace(" ","").split(',')
        bugs(player1)
        update(player1)
        if winner():
            print("player1 is win")
            return False
        
        print(list)
        print("**player two**")
        player2=input("enter your num1 and num2 saparated with comma \n or enter num1 only: ").replace(" ","").split(',') 
        bugs(player2)
        update(player2)
        if winner():
            print("player2 is win")
            return True
        
       
def update(player):
    global list
    if len(player) == 1:
        if int(player[0]) <21:
            list[int(player[0]) - 1] = '-'
    elif len(player) ==2 :
        if abs(int(player[0]) - int(player[1])) == 1:
            list[int(player[0]) - 1] = '-'
            list[int(player[1]) - 1] = '-'

def winner():
    global list
    if list ==['-']*20:
        return True
    else:
        return False

def bugs(play):
    global list
    if len(play)==1:
        if int(play[0]) - 1 > 20 :
            print("###   please enter your number again  ### ")
            play=input("enter your num1 and num2 saparated with comma \n or enter num1 only: ").replace(" ","").split(',')
            update(play)
            bugs(play)
    if len(play)==2:  
        if abs(int(play[0]) - int(play[1])) != 1:
            print("###   please enter your number again   ###")
            play=input("enter your num1 and num2 saparated with comma \n or enter num1 only: ").replace(" ","").split(',')
            update(play)
            bugs(play)
            
        elif [int(play[0]) - 1] == '-' or [int(play[1]) - 1] == '-':
            print("###   please enter your number again  ### ")
            play=input("enter your num1 and num2 saparated with comma \n or enter num1 only: ").replace(" ","").split(',')
            update(play)
            bugs(play)
        
        elif int(play[0]) - 1 > 20 or int(play[1]) - 1 > 20:
            print("###   please enter your number again  ### ")
            play=input("enter your num1 and num2 saparated with comma \n or enter num1 only: ").replace(" ","").split(',')
            update(play)
            bugs(play)
        
loop_gaming()
    
       
        

    

