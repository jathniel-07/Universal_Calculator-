class Multiplication:
    def calc_Multiplication_table(self):
        x=int(input("Enter a range of multiplication table: "))
        y=int(input("Enter the multiple to be found: "))
        for i in range(1,x+1):
            print("|",i," x ",y," = ",i*y,"|")
        print(f"The multiplication table of {y} is printed")
