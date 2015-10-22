import random
while True:
     question = input("Ask the ball anything: ")
     replies = ["It is certain", "Concentrate and ask again", "No",
           "My sources say no", "My sources say yes",
           "It is decidedly so", "Reply hazy try again",
           "Very doubtful", "Outlook not so good",
           "Certainly"]
     print(replies[random.randint(0, len(replies) - 1)])
