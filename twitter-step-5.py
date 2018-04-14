import codecs
import fnmatch
import os

wordcount={}
worddirc={}

for dirpath, dirs, files in os.walk('step4'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:
            for word in file.read().split():
                if word not in wordcount:
                    wordcount[word] = 1
                    worddirc[word] = filename+","
                else:
                    wordcount[word] += 1
                    worddirc[word] += filename+","

s = [(k, wordcount[k]) for k in sorted(wordcount, key=wordcount.get, reverse=True)]


with codecs.open("step5/inverted-index.txt", 'a+', encoding="utf-8") as f:
    f.write("data = "+'\r\n')
    for k,v in s:
        # print(worddirc[k])
        f.write(k+":"+'\r\n')
        f.write("{"+str(v)+", ["+str(worddirc[k])+"]"+"},"+'\r\n')
