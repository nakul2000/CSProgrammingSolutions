n = int(input())



def factorial(n):
    if n < 1:
        return 1

    else:
       returnNumber = n * factorial( n - 1 )
       return returnNumber


print(factorial(n))
c = (input("would you like to continue?"))

if c == "yes":
    n = int(input())
    print(factorial(n))
    c = (input("would you like to continue?"))






