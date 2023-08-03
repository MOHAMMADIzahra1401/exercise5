starter=int(input("Enter 1 or 2 ,(1:start 2 :exit ) :"))
import random
while True:
    if starter==2:
        print("exit")
        break


    elif starter==1:
        adad_tas=random.randint(1,6)
        print("adad_tas:",adad_tas)
        if adad_tas==6:
            print(" you can have two adad tas")
            for i in range(2):
                adad_tas_2=random.randint(1,6)
                print("adad_tas_2:", adad_tas_2)
            break
        else:
            break


    else:
        print("Error")
        break
        
    
     
