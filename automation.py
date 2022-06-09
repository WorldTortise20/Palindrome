#Code to see if a certain word is a palindrome or not

charCount = 0
counter = 1
newCounter = 0
word = input("Type any word and see if it's a palindrome!")
backwordsList = []
valid = "true"


for i in word:
    charCount = charCount+1
    newCharCount = charCount
    if(i == " "):
        valid = "false"
        
letterSplit = list(word.lower())

#print(letterSplit)
for a in letterSplit:
    if(newCharCount>0):
        backwords = letterSplit[charCount-counter]
        backwordsList.append(backwords)
        newCharCount -=1
        counter = counter + 1
        
#print(backwordsList)

if(valid == "true"):
    if(letterSplit == backwordsList):
        print("Palindrome")
    else:
        print("Not a Palindrome")
else:
    print("Not a word")
