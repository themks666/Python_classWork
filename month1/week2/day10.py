num = int(input("enter your number : "))
if num%2==0:
    print("IT's not a prime number")

for i in range(2, num+1):
    if num%i==0:
        print(num)