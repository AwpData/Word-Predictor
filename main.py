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
words = WhitespaceTokenizer().tokenize(file.read())
for word in words:
    unique_words.add(word)

print("Corpus statistics")
print("All tokens: " + str(len(words)))
print("Unique tokens: " + str(len(unique_words)))

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
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
