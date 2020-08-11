def charcount(string):
    return len(string.replace(" ", ""))


if __name__ == "__main__":
    inputstring = input("What is the input string? ")
    count = charcount(inputstring)
    print(inputstring + " has " + str(count) + " characters")
