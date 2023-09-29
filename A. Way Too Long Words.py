n = int(input())
text = []

for i in range(n):
    word = input()

    if len(word) > 10:
        new_word = word[0] + str(len(word) - 2) + word[-1]
        text.append(new_word)
    else:
        text.append(word)

for i in range(n):
    print(text[i])
