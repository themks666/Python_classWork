#TODO: to input age and check if eligible to vote
age = int(input("Enter your age : "))
if(age<18):
    print("Your are not eligible")
else:
    print("Your are eligible")

#TODO: to input a number and check if it is odd or even
Number = int(input("Enter your number : "))
if(Number%2==0):
    print("This is a even number ")
else:
    print("This is a odd number ")

#TODO: to inpiut 3 numbers and find the greatest among them
num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
num3=int(input("Enter your third number : "))

if (num1> num2 and num1>num3):
    print(f"{num1} is the greatest")
elif (num2> num1 and num2>num3):
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")
list1= [num3, num2, num1]
print(max(list1))


#TODO: to input gpa of a studwnr and display the grade

gpa=float(input("Enter your GPA : "))
if(gpa>4):
    print("GPA ca't be greater than four")
elif gpa>3.6:
    print("A+")
elif gpa>3.2:
    print("A")
elif gpa>2.8:
    print("B+")
elif gpa>2.4:
    print("B")
elif gpa<2.4:
    print("fail")


citizen = input("Citizen : ")
if age > 18:
    if citizen =="Nepali":
        print("you are eligible to vote")
    else:
        print("Your are not eligible to vote")
else:
    print("Your are not eligible to vote")
    
rand=int(input("Enter your second number : "))
if(rand<0):
    print("Negative  number")
else:
    print("Positive  number")