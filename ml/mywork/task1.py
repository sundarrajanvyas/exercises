""" Features

The objective of this task is to explore the corpus, deals.txt. 

The deals.txt file is a collection of deal descriptions, separated by a new line, from which 
we want to glean the following insights:

1. What is the most popular term across all the deals?
2. What is the least popular term across all the deals?
3. How many types of guitars are mentioned across all the deals?

"""
from gensim import corpora, models, similarities
from collections import Counter
import operator
import linecache
import nltk
import logging, gensim, bz2


def cleanDoc(doc):
    stopset = nltk.corpus.stopwords.words('english')
    ##Add custom Stop words here.
    stopset.append('com')
    ##End adding custon Stop words
    stemmer = nltk.PorterStemmer()
    tokens = nltk.WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower()
             not in stopset and len(token) > 2]
    final = [stemmer.stem(word) for word in clean]
    return final

def mostPopular(fileName,count):
    doc = cleanDoc(open(fileName).read())
    dictionary = corpora.Dictionary(line.lower().split() for line in doc)
    list1 = dictionary.doc2bow(doc,1)
    dict1={}
    dict1 = dict(list1)
    dispVal = sorted(dict1.iteritems(), key=lambda x:-x[1])[:count]
    for elements in dispVal:
        print dictionary[elements[0]] + ":" + str(elements[1])

def leastPopular(fileName,count):
    doc = cleanDoc(open(fileName).read())
    dictionary = corpora.Dictionary(line.lower().split() for line in doc)
    list1 = dictionary.doc2bow(doc,1)
    dict1={}
    dict1 = dict(list1)
    dispVal = sorted(dict1.iteritems(), key=lambda x:x[1])[:count]
    for elements in dispVal:
        print dictionary[elements[0]] + ":" + str(elements[1])

def noOfTypes(fileName,searchWord):
    dataElement =[]
    dataPosDict = {}
    fOpen = open(fileName,'r')
    for lines in fOpen.readlines():
        y=lines.split()
        dataElement.append(y)
    fOpen.close()
    ##Create word position dictionary
    for i in range(len(dataElement)):
        for word in dataElement[i]:
            if word in dataPosDict:
                dataPosDict[word].append(int(i) + 1)
            else:
                dataPosDict[word] = [int(i) + 1]

    retVal = 0
    outputSet = set()
    ##wordWindowSize = 2      ##Delete when Api is updated to handle multiple
    ##leading words as descriptors. eg "Super Awesome Guitar" is a type of gutar  
    if searchWord in dataPosDict:
        for lineNo in dataPosDict[searchWord]:
            semLine = linecache.getline(fileName, lineNo)
            semLine = semLine.split()
            for wordLoc in range(len(semLine)):
                if (semLine[wordLoc] == searchWord):
                    ##If the line starts with a guitar, then it is assumed the
                    ##type is not specified.
                    if (wordLoc != 0):
                        ##Assuming only the word before the searchWord is
                        ##usually the descriptor
                        outputSet.add(semLine[wordLoc - 1]) 
                    
        retVal = len(outputSet)
        return retVal
    else:
        return retVal

class MyCorpus(object):
    def __iter__(self):
        for line in open('deals.txt'):
            yield id2word.doc2bow(line.lower().split())

id2word = corpora.Dictionary(line.lower().split() for line
                             in cleanDoc(open('deals.txt').read()))

def perfTopic(no_of_topics):
    corpus = MyCorpus()
    corpora.MmCorpus.serialize('dealsCorpus.mm', corpus)
    corpus = corpora.MmCorpus('dealsCorpus.mm')
    print corpus
    ##  Following line should be commented for not displaying the online LDA
    ##  convergence Logs.
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)
    tfidf = models.TfidfModel(corpus)
    print tfidf
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word,
                                          num_topics=no_of_topics,
                                          update_every=1, chunksize=5,
                                          passes=1)
    return lda






    

        
        





    
