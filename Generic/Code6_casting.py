words = ['hi','hello','cool']
x = str(input("enter a word:"))
for i in words:    
    if(i == x):
        print("you entered exact word which is " + x)
#using index to get position of an element
        print('@position ' + str(words.index(i)))
        break
    else:
        print("word entered by you was not word in list")
print("you entered :" + x)