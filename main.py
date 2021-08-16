import nltk
from nltk import WhitespaceTokenizer

nltk.download("punkt")

while True:
    try:
        file_name = str(input("Please enter the filename of your corpus: "))
        file = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found!")
    else:
        print("File found!")
        break

unique_words = set()
bigrams = list()
words = WhitespaceTokenizer().tokenize(file.read())
for word in words:
    unique_words.add(word)
for i in range(0, len(words) - 1):
    bigrams.append([words[i], words[i + 1]])
print("Corpus statistics")
print("All tokens: " + str(len(words)))
print("Unique tokens: " + str(len(unique_words)))
print("Number of bigrams: " + str(len(bigrams)))

while True:
    try:
        index = str(input())
        if index == "exit":
            break
        index = int(index)
    except ValueError or TypeError:
        print("Type Error. Please input an integer")
    else:
        try:
            print(words[index])
            if index < 0:
                print("Head: {}\tTail: {}".format(words[index - 1], words[index]))
            else:
                print("Head: {}\tTail: {}".format(words[index], words[index + 1]))
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
