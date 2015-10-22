# The world's simplest madlibs
def zeus():
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    anothernoun = input("Enter another noun: ")
    print("Zeus %sed  %s but %s was unaffected by it." % (verb, noun, anothernoun))


def about():
    adjective = input("Enter an adjective: ")
    adj = input("Enter another adjective: ")
    print("You're %s and %s" % (adjective, adj))

story = input("Which story would you like to play Possible options thelightgod, aboutYourEnemy:  ")
if story == "thelightgod":
    zeus()
elif story == "aboutYourEnemy":
    about()
else:
    print("Doesn't Exist.")
