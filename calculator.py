#CALCULATOR
def cal():
    print("1)Addition")
    print("2)Subtraction")
    print("3)Multiplication")
    print("4)Division")
    choice= input("Which operation do you wanna perform?(1/2/3/4):")
    if len(choice)==0:
        print("You have entered nothing, please enter something...!!!")
    else:
        if choice =="1":
            num = 0
            a= int(input("how many numbers you wanna add:"))
            for i in range(a):
                b = int(input("Enter a number:"))
                num+=b
            print(f"The sum of numbers=", num)
        elif choice =="2":
            n1= int(input("Enter a number:"))
            n2 = int(input("Enter a number:"))
            print(f"{n1}-{n2}=", n1-n2)
        elif choice =="3":
            num = 1
            a= int(input("how many numbers you wanna multiply:"))
            for i in range(a):
                b = int(input("Enter a number:"))
                num*=b
            print(f"The product of numbers=", num)
        elif choice=="4":
            n1= int(input("Enter a number:"))
            n2 = int(input("Enter a number:"))
            print(f"{n1}/{n2}= ",n1/n2)
        else:
            print("Incorrect choice...!!!")
cal()
use = input("Do you wanna use this calci again(yes/no):")
while use == "yes":
   cal()
   use = input("Do you wanna use this calci again(yes/no):")
else:
    print("THANK YOU...!!!")




   
    
        
        
            
