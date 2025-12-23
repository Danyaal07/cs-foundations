sentence = "hello, this is a sentence."
counter = {}
def count(sentence):
    for c in sentence:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1

count(sentence)
for character, occurances in counter.items():
    print(f"{character} appeared {occurances} times")

#VERSION 2

from collections import Counter

c = Counter("banana")
for character, occurances in c.items():
    print(f"{character} appeared {occurances} times")
