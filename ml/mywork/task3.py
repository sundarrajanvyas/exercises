""" Classification

The objective of this task is to build a classifier that can tell us whether a new, unseen deal 
requires a coupon code or not. 

We would like to see a couple of steps:

1. You should use bad_deals.txt and good_deals.txt as training data
2. You should use test_deals.txt to test your code
3. Each time you tune your code, please commit that change so we can see your tuning over time

Also, provide comments on:
    - How general is your classifier?
    - How did you test your classifier?

"""
## Reference
## http://www.slideshare.net/jpatanooga/sea-hug-navebayes24042011v5
from text.classifiers import NaiveBayesClassifier

def formTrainSet(fileName,classification):
    trainSet = []
    fOpen = open(fileName,'r')
    for lines in fOpen.readlines():
        temp = []
        temp.append(lines)
        temp.append(classification)
        trainSet.append(temp)
    fOpen.close()
    return trainSet

## Instance specific implementation
def getTrainSet():
    trainingSet = []
    goodSet = formTrainSet('good_deals.txt','good_deals')
    badSet = formTrainSet('bad_deals.txt','bad_deals')
    trainingSet = goodSet+badSet
    return trainingSet

def testSet(testSetFileName):
    trainSet = getTrainSet()
    classifierNB = NaiveBayesClassifier(trainSet)
    fOpen=open(testSetFileName,'r')
    for lines in fOpen.readlines():
        classification = ''
        classification = classifierNB.classify(lines)
        print lines + " :: " + classification
