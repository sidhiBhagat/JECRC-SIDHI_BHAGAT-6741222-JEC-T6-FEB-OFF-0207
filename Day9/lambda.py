##lambda args: expression

# result=lambda a,b: a+b
# print(result(10,20))

# (lambda a,b: print(a+b))(int(input("First num: ")),int(input("Second num: ")))

##Wap a program to find the square of a number if it is even.
# num=int(input("Enter a number: "))
# if num%2==0:
#     print(num ** 2)

# result=lambda num: print(num ** 2) if num%2==0 else None
# result(num)

# result= lambda num: print(num ** 2) if num % 2 == 0 else print(num**3)
# result(num)

##Check if a number is positive or negative or zero.
num=int(input("Enter a number: "))
result=lambda num: print("Positive") if num>0 else print("Negative") if num<0 else print("Zero")
result(num)
