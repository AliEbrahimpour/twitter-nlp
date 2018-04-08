import os,fnmatch,codecs
import re

i=0
alist=[]
strr =""

for dirpath, dirs, files in os.walk('step3'):
    for filename in fnmatch.filter(files, '*.txt'):

        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:
            for word in file.read().split(":"):
                if( i<20 ):
                    if(not word.isdigit() ):
                        i += 1
                        with codecs.open("step4/stop-words.txt", 'a+',encoding="utf-8") as f:
                            alist.append(word.strip())
                            print(alist)
                            f.write(word)


for dirpath, dirs, files in os.walk('step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8") as file:
            strr = " "
            text = file.read()
                # text = re.sub(r'alist', '', text)
                # print(text)
            for word in text.split():
                if(word not in alist):
                    strr = strr+word+" "
                        # text.replace(word," ")
        with codecs.open("step4/" + filename, 'w', encoding="utf-8") as f:
            f.write(strr)
            print(strr+'\r\n')
        # print()