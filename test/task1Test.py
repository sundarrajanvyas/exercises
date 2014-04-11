from ml.mywork import task1

def testnoOfTypes():
    retVal = task1.noOfTypes('../ml/data/deals.txt','Guitar')
    assert type(retVal) == int , "Expecting integer"
    assert retVal > -1, "Values must be greater than or = to zero"
    print 'Guitar ' + str(retVal)

def testMostPopular():
    retVal = task1.mostPopular('../ml/data/deals.txt',1)
    assert type(retVal) == list , "Expecting list"
    assert len(retVal) == 1 , "expecting only 1 element"

def testLeastPopular():
    retVal = task1.leastPopular('../ml/data/deals.txt',1)
    assert type(retVal) == list , "Expecting list"
    assert len(retVal) == 1 , "expecting only 1 element"
