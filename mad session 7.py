text = "abcdefg"
for lettervariable in text:
    print(lettervariable)

i = 0
while i < len(text):
    print(text[i])
    i += 1

i = 0
while i < len(text):
    print(text[len(text)-i-1], end="")
    i += 1
