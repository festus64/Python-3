import random
import time


def gen():
    i = 0
    while i < 5:
        i += 1
        words = ["Tears", "Lord", "Sadness", "Rage"]
        words2 = [" against the", "over the", "of the"]
        words3 = [" shadow", " light", " star"]
        words4 = [" in a lifetime", "in the shadow", "in a reflection", "for the star"]
        first = random.choice(words)
        two = random.choice(words2)
        three = random.choice(words3)
        four = random.choice(words4)
        print(first + two + three + four)

while True:
    print("Generating a poem in 2 seconds")
    time.sleep(2)
    gen()
