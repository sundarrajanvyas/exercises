""" Classification

The objective of this task is to build a classifier that can tell us whether a new, unseen deal 
requires a coupon code or not. 

We would like to see a couple of steps:

1. You should use bad_deals.txt and good_deals.txt as training data
2. You should use test_deals.txt to test your code
3. Each time you tune your code, please commit that change so we can see your tuning over time

Also, provide comments on:
    - How general is your classifier?
        Classifier is as general as it can be.It will work on just about any set
        data pertaining to any set of topics. 
        UpWeighing - An addon that works on the data that is fed into the 
                     classifier.eg Terms such as 'code' are treated as if they
                     have occured multiple times.Increasing their weight.
        Morphological stemming - Considering morphological stemming that reduces
                                 synonyms to root words. [Not included]
                                 [TBD] 
    - How did you test your classifier?
        Test it with the existing training set.Both good deals and bad deals.
        Usually industry practice is to train the classifier on 70 % of labeled
        data and use the remaining 30% for verification.
        However here since the labeled data is sparse initial attempts are to use
        100% of the data for training and testing.
        Depending on the initial train data set size(sparse) choosing 70-30 and
        testing will yield a broader range of accuracies.Hence the approach to
        use the same 100 % data set for trainging and testing purposes.
        There is a risk of overfitting the data that is also to be noted.
        Precision/recall and F1 scores is the standard for evaluation.
"""

## Reference
## http://www.slideshare.net/jpatanooga/sea-hug-navebayes24042011v5
import nltk
import sys
from text.classifiers import NaiveBayesClassifier

def cleanDoc(doc):
    stopset = nltk.corpus.stopwords.words('english')
    ##Add custom Stop words here.
    ##stopset.append('com')
    ##End adding custon Stop words
    stemmer = nltk.PorterStemmer()
    tokens = nltk.WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower()
             not in stopset and len(token) > 2]
    final = [stemmer.stem(word) for word in clean]
    return final

##Tuning by up weighing .
## Add important words to upWeigher
upWeighter = ['code','coupon','coupons','promo']
## No of times upWeigher terms are repeated
weight = 20
##End tuning by upweighing

def formTrainSet(fileName,classification):
    trainSet = []
    fOpen = open(fileName,'r')
    for lines in fOpen.readlines():
        ##Tune by eliminating generic stop words.
        stemmedLines = ''
        tempArray = []
        iterArray = []
        tempArray.append(lines.split())
        for word in tempArray[0]:
            if (word.lower() in upWeighter):
                for x in range(0,weight):
                    iterArray.append(word)
            else:
                iterArray.append(word)
        for word in iterArray:
            if (cleanDoc(word) != ' '):
                stemmedLines = stemmedLines+ ''.join(cleanDoc(word)) + ' '
        ##End stemming.
        temp = []
        temp.append(stemmedLines)
        temp.append(classification)
        trainSet.append(temp)
    fOpen.close()
    return trainSet

## Instance specific implementation
def getTrainSet():
    trainingSet = []
    goodSet = formTrainSet('../data/good_deals.txt','good_deals')
    badSet = formTrainSet('../data/bad_deals.txt','bad_deals')
    trainingSet = goodSet+badSet
    return trainingSet

def testSet(testSetFileName):
    trainSet = getTrainSet()
    classifierNB = NaiveBayesClassifier(trainSet)
    fOpen=open(testSetFileName,'r')
    for lines in fOpen.readlines():
        classification = ''
        ##Tune by eliminating generic stop words.
        stemmedLines = ''
        tempArray = []
        tempArray.append(lines.split())
        for word in tempArray[0]:
            if (cleanDoc(word) != ' '):
                stemmedLines = stemmedLines+ ''.join(cleanDoc(word)) + ' '
        ##End stemming.
        classification = classifierNB.classify(stemmedLines)
        print lines + " :: " + classification
    fOpen.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
        testSet(fileName)

        
## Compares difference in results based on the tuning.
## Returns instances of classifications that differed.
def compareStemmerEffects(testSetFileName):
    trainSet = getTrainSet()
    classifierNB = NaiveBayesClassifier(trainSet)
    fOpen = open(testSetFileName,'r')
    for lines in fOpen.readlines():
        classification = ''
        unTunedClassification = ''
        ##Tune by eliminating generic stop words.
        stemmedLines = ''
        tempArray = []
        tempArray.append(lines.split())
        for word in tempArray[0]:
            if (cleanDoc(word) != ' '):
                stemmedLines = stemmedLines+ ''.join(cleanDoc(word)) + ' '
        ##End stemming.
        classification = classifierNB.classify(stemmedLines)
        unTunedClassification = classifierNB.classify(lines)
        if (classification != unTunedClassification):
            print lines + "Tuned =" + classification + " ::  Untuned =" + unTunedClassification
    fOpen.close()

## Not optimized. Requires further clean up and optimization.[TBD] 
def accuracyTester(fileName,label):
    trainSet = getTrainSet()
    classifierNB = NaiveBayesClassifier(trainSet)
    total = 0
    correct = 0
    fOpen=open(fileName,'r')
    for lines in fOpen.readlines():
        classification = ''
        ##Tune by eliminating generic stop words.
        stemmedLines = ''
        tempArray = []
        tempArray.append(lines.split())
        for word in tempArray[0]:
            if (cleanDoc(word) != ' '):
                stemmedLines = stemmedLines+ ''.join(cleanDoc(word)) + ' '
        ##End stemming.
        classification = classifierNB.classify(stemmedLines)
        total += 1
        if (classification == label):
            correct+=1
    fOpen.close()
    return total,correct

def netAccuracyTester():
    goodSet = accuracyTester('../data/good_deals.txt','good_deals')
    badSet = accuracyTester('../data/bad_deals.txt','bad_deals')
    netAccuracy = 0.00
    netAccuracy = (((goodSet[1]+badSet[1]) * 100 )/ (goodSet[0]+badSet[0]))
    print "Theoretical best accuracy "+ str(netAccuracy) + "%"

