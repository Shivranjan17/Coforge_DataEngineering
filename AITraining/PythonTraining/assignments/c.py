sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

for ch in sentence:

    if ch == " ":
        continue

    if ch == "!":
        break

    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Total Vowels =", vowels)
print("Total Consonants =", consonants)