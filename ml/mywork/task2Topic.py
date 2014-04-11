
import gensim
from gensim import corpora, models, similarities
import nltk
import logging
import sys

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

class MyCorpus(object):
    def __iter__(self):
        for line in open('../data/deals.txt'):
            yield id2word.doc2bow(line.lower().split())

id2word = corpora.Dictionary(line.lower().split() for line
                             in cleanDoc(open('../data/deals.txt').read()))

def perfTopic(noOfTopics):
    corpus = MyCorpus()
    ##corpora.MmCorpus.serialize('dealsCorpus.mm', corpus)
    ##corpus = corpora.MmCorpus('dealsCorpus.mm')
    print corpus
    ##  Following line should be commented for not displaying the online LDA
    ##  convergence Logs.
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)
    tfidf = models.TfidfModel(corpus)
    print tfidf
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word,
                                          num_topics=noOfTopics,
                                          update_every=1, chunksize=5,
                                          passes=1)
    return lda


if __name__ == '__main__':
    if len(sys.argv) == 2:
        noOfTopics = sys.argv[1]
        perfTopic(int(noOfTopics))
        


