def countWords(file):
    return len(file.split())

def countLetters(file):
    letters = {}
    words = file.split()
    for word in words:
        for char in word.lower():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters


try:
    with open('books/frankenstein.txt') as f:
        file_content = f.read()
except FileNotFoundError:
    print("File not found")

totalWords = countWords(file_content)
totalLetters = countLetters(file_content)

print(f"--- Beging report of {f.name} ---")
print(totalWords)
reportLetters = list(totalLetters)
reportLetters.sort()
for letter in reportLetters:
    print(f"The '{letter}' character as found {totalLetters[letter]} times")
print("--- End report ---")

