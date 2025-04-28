word = input()
# word = 'KARIJERA'
NO_WORD = [
'C',
'A',
'M',
'B',
'R',
'I',
'D',
'G',
'E',
]
for i in range(len(NO_WORD)):
    word  =word.replace(NO_WORD[i],'')
print(word)
