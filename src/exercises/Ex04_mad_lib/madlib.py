def story(noun, verb, adjective, adverb):
    return "Do you {} your {} {} {}? That's hilarious!".format(verb, adjective, noun, adverb)


if __name__ == "__main__":
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter n adverb: ")
    print(story(noun, verb, adjective, adverb))
