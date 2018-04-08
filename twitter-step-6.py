import codecs

n=input("enter word: ")
print(n)
with codecs.open("step5/inverted-index.txt", 'r', encoding="utf-8") as f:
    for text in f.readlines():
        for word in text.split(":"):
            if(word == n):
                print("done!")
                strr = f.readline()
                print(strr)