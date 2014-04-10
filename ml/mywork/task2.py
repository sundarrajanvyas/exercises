""" Groups and Topics

The objective of this task is to explore the structure of the deals.txt file. 

Building on task 1, we now want to start to understand the relationships to help us understand:

1. What groups exist within the deals?
2. What topics exist within the deals?

"""
import sys
import numpy
from nltk.cluster import GAAClusterer
import nltk.corpus
from nltk import decorators
import nltk.stem
 
def getWords(titles):
    words = set()
    for title in jobTitles:
        for word in title.split():
            words.add(word)
    return list(words)

@decorators.memoize
def vectorSpaced(title):
    titleElements = [word for word in title.split()]
    return numpy.array([
        word in titleElements 
        for word in words], numpy.short)
 
if __name__ == '__main__':
##  fileName = 'smallDeals.txt'
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        noOfClusters = sys.argv[2]
    fOpen = open(fileName,'r')
    jobTitles = [line.strip() for line in fOpen.readlines()]
    words = getWords(jobTitles)
    cluster = GAAClusterer(5)
    cluster.cluster([vectorSpaced(title) for title in jobTitles if title])
    classified = [cluster.classify(vectorSpaced(title)) for title in jobTitles]
    for cluster_id, title in sorted(zip(classified, jobTitles)):
        print cluster_id, title

