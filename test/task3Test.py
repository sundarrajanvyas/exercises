from ml.mywork import task3

def testFormTrainSet():
    retValGood = task3.formTrainSet('../ml/data/good_deals.txt','good_deals')
    assert type(retValGood) == list , "Expecting List"
    assert retValGood > -1, "Values must be greater than or = to zero"
    retValBad = task3.formTrainSet('../ml/data/good_deals.txt','good_deals')
    assert type(retValBad) == list , "Expecting List"
    assert retValBad > -1, "Values must be greater than or = to zero"   

def testGetTrainSet():
    retVal = task3.getTrainSet('../ml/data/good_deals.txt',
                               '../ml/data/bad_deals.txt')
    assert type(retVal) == list , "Expecting List"
    assert retVal > -1, "Values must be greater than or = to zero"    

def testTestSet():
    retStatus = task3.testSet('../ml/data/test_deals.txt',
                           '../ml/data/good_deals.txt',
                           '../ml/data/bad_deals.txt')
    assert type(retStatus) == int , "Expecting integer indicating status"
    assert retStatus > 0 , "At least one classification should have occured"
