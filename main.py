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

tigrams = list()
words = WhitespaceTokenizer().tokenize(file.read())
for i in range(0, len(words) - 2):  # Then, tokenize (by whitespace) the text into pairs (head and tail) and add to list
    tigrams.append([words[i] + " " + words[i + 1], words[i + 2]])

print("\n")
for _ in range(0, 10):  # Loop for 10 sentences
    while True:  # Make sure the head word starts with a capital and has no period
        random_word = random.choice(tigrams)[0]
        if re.match(r"[A-Z][\w\s']*$", random_word) is not None:
            sentence = random_word
            break
    while True:  # Loop for at least 5 words
        counter_d = dict()
        for words in tigrams:  # Gets all possible tails for head word, and then count them in dictionary
            if words[0] == random_word:
                counter_d.setdefault(words[1], 0)
                counter_d[words[1]] += 1
        # Get the random tail based on probability (weight heavier towards more common words by counter)
        random_tail = random.choices(list(counter_d.keys()), weights=[nums * 10 for nums in counter_d.values()])[0]
        sentence += " " + random_tail  # Add to our sentence the valid tail
        if re.match(r"[\w']+[.?!]+$", random_tail) is not None:  # If random_tail contains end-punctuation
            if len(sentence.split()) >= 5:  # This is a valid sentence if word length >= 5, so break!
                break
        random_word = random_word.split()[1] + " " + random_tail  # All else, the new head is the last tail
    print(sentence)  # Finally, print the sentence
