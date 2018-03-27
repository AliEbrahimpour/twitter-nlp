import os,fnmatch,codecs

i=0


for dirpath, dirs, files in os.walk('step3'):
    for filename in fnmatch.filter(files, '*.txt'):

        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:
            for word in file.read().split(":"):
                if( i<21 ):
                    if(not word.isdigit() ):
                        i += 1
                        with codecs.open("step4/stop-words.txt", 'a+',encoding="utf-8") as f:
                            print(word)
                            f.write(word)
