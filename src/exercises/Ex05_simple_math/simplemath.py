def addition(a, b):
    return a + b


def difference(a, b):
    return a - b


def product(a, b):
    return a * b


def quotient(a, b):
    if (b == 0):
        return float('inf')
    return a / b


if __name__ == "__main__":
    firstnum = input("What is the first number: ")
    secondnum = input("What is the second number: ")
    print(firstnum + " + " + secondnum + " = " + str(addition(float(firstnum), float(secondnum))))
    print(firstnum + " - " + secondnum + " = " + str(difference(float(firstnum), float(secondnum))))
    print(firstnum + " * " + secondnum + " = " + str(product(float(firstnum), float(secondnum))))
    print(firstnum + " / " + secondnum + " = " + str(quotient(float(firstnum), float(secondnum))))
