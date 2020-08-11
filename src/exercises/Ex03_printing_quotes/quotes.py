def quotation(who, says):
    return who + " says, \"" + says + "\""

if __name__ == "__main__":
    quote = input("What is the quote? ")
    who = input("Who said it? ")
    output = quotation(who, quote)
    print(output)
