import random
count=0
while(count<=100):
    n=input("press r to roll a dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("ur random is",r)
        print("ur count is",count)
    if count==8:
            count=37
            print("wow! ur climbing the ladder")
    elif count==11:
              count=2
              print("sorry! snake bite")
    elif count==13:
              count=34
              print("wow! ur climbing the ladder")
    elif count==25:
              count=4
              print("sorry! snake bit")
    elif count==38:
              count=9
              print("sorry! snake bite")
    elif count==40:
              count=68
              print("wow! ur climbing the ladder")
    elif count==52:
              count=81
              print("wow! ur climbing the ladder")
    elif count==65:
              count=45
              print("sorry! snake bite")
    elif count==76:
                    count=97
                    print("wow! ur climbing the ladder")
    elif count==89:
                    count=70
                    print("sorry! snake bite")
    elif count==93:
                    count=64
                    print("sorry! snake bite")
    elif count>=100:
                    print("won")
    else:
                    print("continue the game")
                    
              
                    
    
