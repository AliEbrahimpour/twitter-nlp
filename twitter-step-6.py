import codecs

n=input("enter word: ")
print(n)
line=""
t=""

with codecs.open("step5/inverted-index.txt", 'r', encoding="utf-8") as f:
    for text in f.readlines():
        for i in range(0, len(text)):
            line += text[i]
            print(str(i)+line)
            for word in line.split(":"):
                print(word)
                if(word == n):
                    print("done")
                    # t += text[i+1]
                    print(t)



