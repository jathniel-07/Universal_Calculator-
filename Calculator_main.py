import time
import math 
def load_screen():
    word="WELCOME TO AI POWERED CALCULATOR\n"
    for i in word:
        print(i,end=" ",flush=True)
        time.sleep(0.02)
    print("\n")
    interface_msg="INTERFACE LOADED\n"
    for i in interface_msg:
        print(i,end=" ",flush=True)
        time.sleep(0.1)
    print("\n")
    functions_ex="""


    
(THIS PROGRAM IS CASE INSENSITIVE)
(CONVERSATION IS PERMITTED RATHER THAN ONLY KEYWORDS)
(EXPLAIN YOU NEED AS SIMPLE AS POSSIBLE)

LIST OF LIBRARIES:

1.INTEREST CALCULATOR  => Interest Calculator to calculate interest(I),rate of interest(r),princpal amount(P) and number of years(n)
2.SIMPLE CALCULATOR    => Simple Calculator for basic Arithmetic operations
3.GROCERY CALCULATOR   => Grocery Calculator for calculating the total cost and cost of each grocery things
4.MULTIPLICATION TABLE => Multiplication Table for printing the multiplication table of any number
5.PHYSICS CALCULATOR   => Physics calculator for all physics values to be found (It's a large library)


"""
    for i in functions_ex:
        print(i,end="",flush=True)
        time.sleep(0.008)
    pd=str(input("\nPROCEED ?(Yes => y || No => n):"))
    if pd=="y":
        for i in range(0,101):
            print(f"\rLOADING LIBRARIES:{i}%",end="",flush=True)
            time.sleep(0.02)
        AI()
    print("\n")
def AI():
    for i in range(0,101):
        print(f"\rREGISTERING LIBRARIES:{i}%",end="",flush=True)
        time.sleep(0.01)
    def searching():
        print("\n")
        giving=str(input("JATH:WHAT DO YOU LIKE TO ACCESS ?:"))
        print("\n")
        cgiving=giving.lower()
        load_i=[]
        load=[]
        def filtering():
            pre_load=""
            for i in cgiving:
                if(i !=" "):
                    pre_load=pre_load+i
                else:
                    load_i.append(str(pre_load))
                    pre_load=""
            if pre_load:
                load_i.append(pre_load)
            for i in load_i:
                if(i not in ['object','of','i','implement','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','few','perform','do','calculate','generate','find','want','to','is', 'was', 'would', 'may', 'might', 'will', 'access', 'see', 'select', 'library', 'see', 'open', 'i', 'me', 'you', 'like', 'love', 'feel','accessing','accessed','accesses','accesses','accessing','accessed','accesses']):
                    load.append(i)
                else:
                    continue
        filtering()
        if(load in [['interest','calculator'],['interest','calc'],['interest','cal'],['interest','library'],['interest','lib'],['interest']]):
            from Interest_calc import Interest
            i=Interest()
            i.calc_Interest()
            searching()
        elif(load in [['calculator','calc'],['calculator','cal'],['multiply'],['add'],['subtract'],['divide'],['modulus'],['remainder'],['addition'],['subtraction'],['multiplication'],['division'],['calculator']]):
            from Simple_Calculator import Calculator
            c=Calculator()
            c.calc_Simple()
            searching()
        elif(load in [['grocery','calculator'],['grocery','calc'],['grocery','cal'],['grocery'],['supermarket'],['shopping','list'],['shopping'],['grocery','list']]):
            from Grocery_calc import Grocery
            g=Grocery()
            g.calc_grocery()
            searching()
        elif(load in [['multiplication','table'],['multiplication','tfunc'],['multiplication'],['series'],['multiplication','series']]):
            from Multiplication_table import Multiplication
            m=Multiplication()
            m.calc_Multiplication_table()
            searching()
        elif(load in [['physics','calculator'],['physics'],['displacement'],['speed'],['average','speed'],['velocity'],['angular','velocity'],['angle'],['angle','projection'],['projection'],['time','interval'],['time'],['acceleration']]):
            from Physics_calc import Physics
            p=Physics()
            p.calc_Physics()
            searching()
        elif(load in [['exit'],['quit'],['get','out'],['close']]):
            exit
        else:
            print("Error!")
            for i in range(0,101):
                    print(f"\rReturning:{i}%",end="",flush=True)
                    time.sleep(0.03)
            searching()

            
    searching()  
load_screen()
AI()
