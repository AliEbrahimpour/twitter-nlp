import os,fnmatch,codecs

from collections import OrderedDict

wordcount={}

for dirpath, dirs, files in os.walk('step2'):
    for filename in fnmatch.filter(files, '*.txt'):

        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:

            for word in file.read().split():

                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1


b = OrderedDict(sorted(wordcount.items(), key=lambda t: t[1]))

for k,v in b.items():
    print (k,v)
    if len(wordcount) > 0:
        with codecs.open("step3/word-frequency.txt", 'a+', encoding="utf-8") as f:
            j = k+str(v)
            f.write(j+'\n')

# codecs.open("step2/" + filename, 'w', encoding="utf-8") as f:
#     f.write(tweet)

file.close();