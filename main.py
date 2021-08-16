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

bigrams = list()
words = WhitespaceTokenizer().tokenize(file.read())
for i in range(0, len(words) - 1):
    bigrams.append([words[i], words[i + 1]])
print("Corpus statistics")
print("All tokens: " + str(len(words)))
print("\nEnter a word and see how many words follow it in the corpus ('exit' to quit)s: ")
while True:
    word = str(input())
    if word == "exit":
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
