

def bigger(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return false


a = int(input("Enter a number: "))
b = int(input("Enter a number2: "))
print(bigger(a, b))