from porter2 import stem
import string

def getStopWordsList():
    f = open('C:\\Users\\Naveen\\Desktop\\Data Mining\\project\\inputs\\stopwords.txt','r')
    stopWordsList = []
    for stopWord in f:
        stopWordsList.append(stopWord[:-1])
    return stopWordsList

def removeStopWords(stopWordsList, punctuationRemovedAbstract):
    stopWordsRemovedAbstract = []
    words = punctuationRemovedAbstract.split(" ")
    for word in words:
        if(word.lower() not in stopWordsList):
            stopWordsRemovedAbstract.append(word)
    return stopWordsRemovedAbstract

def applyStemming(stopWordsRemovedAbstract):
    stemmmingAppliedAbstract = []
    for word in stopWordsRemovedAbstract:
        stemmmingAppliedAbstract.append(stem(word))
    return stemmmingAppliedAbstract

def processTrainingData(stopWordsList):
    #===========================================================================
    # f = open('C:\\Users\\Naveen\\Desktop\\Data Mining\\project\\inputs\\AP_train_sample.txt','r')
    #===========================================================================
    f = open('C:\\Users\\Naveen\\Desktop\\Data Mining\\project\\inputs\\AP_train.txt', encoding="utf8")
    authorMap = {}
    for line in f:
        #=======================================================================
        # print(line);
        #=======================================================================
        if(line.startswith("#index ")):
            print(line)
            authorsInPublication = []
        if(line.startswith("#a ")):
            authorsInPublication = line[2:].split(";")
        if(line.startswith("#! ")):
            line = line[2:]
            exclude = set(string.punctuation)
            punctuationRemovedAbstract = ''.join(ch for ch in line if ch not in exclude)
            stopWordsRemovedAbstract = removeStopWords(stopWordsList, punctuationRemovedAbstract)
            stemmmingAppliedAbstract = applyStemming(stopWordsRemovedAbstract)
    return authorMap

stopWordsList = getStopWordsList()
processTrainingData(stopWordsList)
print("Done")
