'''
Exception handling Approaches

--> Specific Exception Handling
--> Generic Exception Handling
--> Default Exception Handling
'''

# Specific Exception Handling

# n1, n2=21, 0
# try:
#     ## Problem Statement
#     result = n1/n2
#     print(result)

# except ZeroDivisionError:
#     ## Solution Code
#     print("Please donot choose 0 as the second number.")


## Generic Exception Handling: type of exception is not specified.
# --> we cant handle keyboard interruption.

# try:
#     a, b, c=1, 2
    
# # except ValueError:
# except Exception:
#     print("For performing MVC, no of variables should be equal to no of values.")

# try:  
#     print(a, b, c)

# # except NameError:
# except Exception:
#     print("Identifiers are not there in the memory.")

#### keyboard interruption ######
# import time
# try:
#     while True:
#         print(time.time())

# # except Exception:
# #     print ("loop got stopped.")

# except:
#     print ("loop got stopped.")

## Default Exception Handling: type of exception is not specified and also no code is written in except block.