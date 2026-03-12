'''

raise --> it is a keyword, which helps us to throw an error in between a program.

Exception Creation

1. Custom Exception Creation(raise)
2. Userdefined Exception(raise)
3. Assertion Exception(assert)

'''
'''
## Custom Exception Creation(raise)
1. We use prebuilt exception classes according to our requirement

raise ValueError("message") --> it will create an object of ValueError class and pass the message
ValueError: message
'''

# num = 17
# if num>=18:
#     print("You are eligible for voting & driving.")
# else:
#     # raise ValueError("You are not eligible for voting & driving.")
#     # raise NameError("You are not eligible for voting & driving.")
#     raise Exception("You are not eligible for voting & driving.")


'''
## Userdefined Exception(raise)
1. It is a type of exception in which we can crete our own exception classes based upon our own requirement. We can also provide banes to those classes according to the use cases.

'''

# class MyException(Exception):
#     pass

# # raise MyException("This is a user defined exception.")

# n1, n2=10, 3
# if n2==0:
#     raise MyException("Please donot choose 0 as the second number.")
# else:
#     print(n1/n2)

'''
Assertion Exception(assert)
1.created by using assert keyword.

assert <condition>, print(ERROR)
print(output)

'''

s= input("Enter a string: ")
assert s==s[::-1], print("The string is not a palindrome")
print("The string is a palindrome.")