intro = input("Enter your introdution =")
charactercount = 0
wordcount = 1

for i in intro:
        charactercount = charactercount+1
        if(i==' '):
                wordcount=wordcount+1

print ("number of words in the string")
print (wordcount)
print ("number of characters in the string")
print (charactercount)