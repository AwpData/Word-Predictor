import random
import re

import nltk
from nltk import WhitespaceTokenizer

nltk.download("punkt")

while True:  # First, get the corpus text (and make sure it exists)
    try:
        file_name = str(input("Please enter the filename of your corpus: "))
        file = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found!")
    else:
        break

bigrams = list()
words = WhitespaceTokenizer().tokenize(file.read())
for i in range(0, len(words) - 1):  # Then, tokenize (by whitespace) the text into pairs (head and tail) and add to list
    bigrams.append([words[i], words[i + 1]])

print("\n")
for _ in range(0, 10):  # Loop for 10 sentences
    while True:  # Make sure the head word starts with a capital and has no period
        random_word = random.choice(bigrams)[0]
        if re.match(r"[A-Z][A-Za-z']*$", random_word) is not None:
            sentence = random_word
            break
    while True:  # Loop for at least 5 words
        counter_dict = dict()
        for words in bigrams:  # Gets all possible tails for head word, and then count them in dictionary
            if words[0] == random_word:
                counter_dict.setdefault(words[1], 0)
                counter_dict[words[1]] += 1
        random_tail = random.choices(list(counter_dict.keys()), weights=[nums * 10 for nums in counter_dict.values()])[
            0]  # Get the random tail based on probability (weight heavier towards more common words by counter)
        sentence += " " + random_tail  # Add to our sentence the valid tail
        if re.match(r"[\w']+[.?!]+$", random_tail) is not None:  # If random_tail contains end-punctuation
            if len(sentence.split()) >= 5:  # This is a valid sentence if word length >= 5, so break!
                break
        random_word = random_tail  # All else, the new head is the last tail
    print(sentence)  # Finally, print the sentence

print("\nEnter one word at a time now to see the probability of it being chosen ('0' = quit)")
while True:
    word = str(input())
    if word == "0":
        break
    else:
        counter_dict = dict()
        for words in bigrams:
            if words[0] == word:
                counter_dict.setdefault(words[1], 0)
                counter_dict[words[1]] += 1
        if len(counter_dict) == 0:
            print("The requested word is not in the model. Please input another word.")
            continue
        counter_dict = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))
        print("\nHead: {}".format(word))
        for key, value in counter_dict.items():
            print("Tail: {}\tCount: {}".format(key, value))
