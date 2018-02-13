while True:
    print ("hello..this is a 100 game .. i hope you enjoy it ....lets start")
    sum=0
    while sum<100:
        
            x=int(input("player 1 : "))
      
            if x>10:
                print("sorry the number is out of range ")
            
                continue
        
            sum=sum+x
            print (sum)
            if sum >=100:
                print("player 1 wons")
                break
        
            y=int(input("player 2 : "))
            sum=sum+y
            print(sum)
            if sum>=100:
            
                print ('congratiulations ...you won ')
            
    
