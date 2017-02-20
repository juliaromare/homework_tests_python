#  Name: Julia Romare
#  Homework 8: Working with Text
#  Date: 11/12/2015
#  COMP 123-05
#  Professor: Katherine Kinnaird
#  
#


from juliaromare_hw8Code import *



# ==========================================================================================
# Tests for readWordList

def readWordListTests():
    print("--------------------------------------")
    print("Testing readWordList:")
    
    allOk = True
    shortList = readWordList('shortcross.txt')
    # We only print a message if a call fails
    if len(shortList) != 80:
        print("Called: readWordList('shortcross.txt')")
        print("Resulting list the wrong length, should be 80 long")
        allOk = False
    elif shortList[0] != 'aa':
        print("Called: readWordList('shortcross.txt')")
        print("Expected first value to be:", 'aa', "   but function returned:", shortList[0])
        allOk = False
    elif shortList[10] != 'aardvarks':
        print("Called: readWordList('shortcross.txt')")
        print("Expected 10th value to be:", 'aardvarks', "   but function returned:", shortList[10])
        allOk = False
    elif  shortList[79] != 'abbeys':
        print("Called: readWordList('shortcross.txt')")
        print("Expected last value to be:", 'abbeys', "   but function returned:", shortList[79])
        allOk = False
    
    longList = readWordList('crosswords.txt')
    # We only print a message if a call fails
    if len(longList) != 113809:
        print("Called: readWordList('crosswords.txt')")
        print("Resulting list the wrong length, should be 113809 long")
        allOk = False
    elif longList[0] != 'aa':
        print("Called: readWordList('crosswords.txt')")
        print("Expected first value to be:", 'aa', "   but function returned:", longList[0])
        allOk = False
    elif longList[20000] != 'condyle':
        print("Called: readWordList('crosswords.txt')")
        print("Expected 20000th value to be:", 'condyle', "   but function returned:", longList[20000])
        allOk = False
    elif  longList[113000] != 'yahoo':
        print("Called: readWordList('crosswords.txt')")
        print("Expected last value to be:", 'yahoo', "   but function returned:", longList[113000])
        allOk = False
    
    
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")
    
    
# Remove the # from the following line to run the test for readWordList
#readWordListTests()

# ==========================================================================================
# ==========================================================================================
# Tests for readTextList

def readTextListTests():
    print("--------------------------------------")
    print("Testing readTextList:")
    
    allOk = True
    aliceList = readTextList('alice.txt')
    # We only print a message if a call fails
    if len(aliceList) != 57:
        print("Called: readTextList('alice.txt')")
        print("Resulting list the wrong length, should be 57 long")
        allOk = False
    elif aliceList[0] != 'Alice':
        print("Called: readTextList('alice.txt')")
        print("Expected first value to be:", 'Alice', "   but function returned:", aliceList[0])
        allOk = False
    elif aliceList[11] != 'sister':
        print("Called: readTextList('alice.txt')")
        print("Expected 10th value to be:", 'sister', "   but function returned:", aliceList[11])
        allOk = False
    elif  aliceList[-1] != 'conversation':
        print("Called: readTextList('alice.txt')")
        print("Expected last value to be:", 'conversation', "   but function returned:", aliceList[-1])
        allOk = False
    
    mobyList = readTextList('mobydick.txt')
    # We only print a message if a call fails
    if len(mobyList) != 212024:
        print("Called: readTextList('mobydick.txt')")
        print("Resulting list the wrong length, should be 212024 long, but was", len(mobyList))
        allOk = False
    elif mobyList[0] != 'ETYMOLOGY':
        print("Called: readTextList('mobydick.txt')")
        print("Expected first value to be:", 'ETYMOLOGY', "   but function returned:", mobyList[0])
        allOk = False
    elif mobyList[20000] != 'hideous':
        print("Called: readTextList('mobydick.txt')")
        print("Expected 20000th value to be:", 'hideous', "   but function returned:", mobyList[20000])
        allOk = False
    elif  mobyList[210147] != 'Ahab':
        print("Called: readTextList('mobydick.txt')")
        print("Expected 210147 value to be:", 'Ahab', "   but function returned:", mobyList[210147])
        allOk = False
    
    
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")
    
    
# Remove the # from the following line to run the test for readTextList
#readTextListTests()

# ==========================================================================================


#==========================================================================================
# Tests for findContaining

# findContaining depends on readTextList, so that must be working first before you run these tests.

# Uncomment the calls to readTextList below, before running these tests
#shortList = readWordList('shortcross.txt')
#longList = readWordList('crosswords.txt')
#persWords = readTextList('persuasion.txt')
#mobyWords = readTextList('mobydick.txt')

# These are defined globally so that later test functions can also use them

def findContainingTests():
    print("--------------------------------------")
    print("Testing findContaining:")
    
    allOk = True
    
    testList1 =  ['xanadu', 'zany', 'exult', 'x-rays', 'mixup']
    testList2 = ['raccoon', 'balloon', 'june', 'candy', 'prune', 'moon']
    # We only print a message if a call fails
    
    lst1 = findContaining('tion', shortList)
    lst2 = findContaining('xu', testList1)
    lst3 = findContaining('oo', testList2)
    lst4 = findContaining('cht', longList)
    lst5 = findContaining('Anne', persWords)
    lst6 = findContaining('whale', mobyWords)
    if lst1 != []:
        print("Called: findContaining('tion', shortList)")
        print("Expected:", [], "   but function returned:", lst1)
        allOk = False
    if lst2 != ['exult', 'mixup']:
        print("Called: findContaining('xu', ['xanadu', 'zany', 'exult', 'x-rays', 'mixup'])")
        print("Expected:", ['exult', 'mixup'], "   but function returned:", lst2)
        allOk = False
    if lst3 != ['raccoon', 'balloon', 'moon']:
        print("Called: findContaining('oo', ['raccoon', 'balloon', 'june', 'candy', 'prune', 'moon'])")
        print("Expected: ", ['raccoon', 'balloon', 'moon'], "   but function returned:", lst3)
        allOk = False
    if  len(lst4) != 35:
        print("Called: findContaining('cht', longList)")
        print("Expected result length to be 35, but function returned:", len(lst4))
        allOk = False
    if  len(lst5) != 497:
        print("Called: findContaining('Anne', persWords)")
        print("Expected result length to be 497, but function returned:", len(lst5))
        allOk = False
    if  len(lst6) != 1322:
        print("Called: findContaining('whale', mobyWords)")
        print("Expected result length to be 1322, but function returned:", len(lst6))
        allOk = False
    if  lst6.count('whales') != 235:
        print("Called: findContaining('whale', mobyWords)")
        print("Expected result has 236 'whales', but function returned:", lst6.count('whales'))
        allOk = False
    
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")    

# Remove the # from the following line to run the test for findContaining
#findContainingTests()


# ==========================================================================================


# ==========================================================================================
# Tests for countConsonants

def countConsonantsTests():
    print("--------------------------------------")
    print("Testing countConsonants:")
    
    allOk = True
    
    testStr1 = 'Peter Piper picked a peck of pickled peppers'
    testStr2 = 'She sells sea shells by the sea shore'
    testStr3 = ''
    testStr4 = 'aeiouaeioua`~!@#$%^&*()-_=+[{]}|?/><,.;:1234567890'
    testStr5 = 'cccccccccc cccccccccc'
    # We only print a message if a call fails
    
    d1 = countConsonants(testStr1)
    d1Ans = {'c': 3, 'd': 2, 'f': 1, 'k': 3, 'l': 1, 'p': 9, 's': 1, 'r': 3, 't': 1}
    d2 = countConsonants(testStr2)
    d2Ans = {'b': 1, 'h': 4, 'l': 4, 's': 8, 'r': 1, 't': 1, 'y': 1}
    d3 = countConsonants(testStr3)
    d4 = countConsonants(testStr4)
    d5 = countConsonants(testStr5)
    if d1 != d1Ans:
        print("Called: countConsonants(testStr1)")
        print("Expected:", d1Ans, "   but function returned:", d1)
        allOk = False
    if d2 != d2Ans:
        print("Called: countConsonants(testStr2)")
        print("Expected:", d2Ans, "   but function returned:", d2)
        allOk = False
    if d3 != {}:
        print("Called: countConsonants(testStr3)")
        print("Expected: ", {}, "   but function returned:", d3)
        allOk = False
    if  d4 != {}:
        print("Called: countConsonants(testStr4)")
        print("Expected: ", {}, "   but function returned:", d4)
        allOk = False
    if  d5 != {'c': 20}:
        print("Called: countConsonants(testStr5)")
        print("Expected: ", {'c': 20}, "   but function returned:", d5)
        allOk = False
    
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")       


# Remove the # from the following line to run the test for countConsonants
#countConsonantsTests()

# ==========================================================================================

# ==========================================================================================
# Tests for matchesPattern

def matchesPatternTests():
    print("--------------------------------------")
    print("Testing matchesPattern:")
    
    allOk = True
    # We only print a message if a call fails
    
    a1 = matchesPattern('ability', 'ability')
    a2 = matchesPattern('Ability', 'ability')
    a3 = matchesPattern('b**m', 'balm')
    a4 = matchesPattern('b**m*', 'balm')
    a5 = matchesPattern('*****', 'agony')
    a6 = matchesPattern('*bix*', 'Obix!')
    if a1 != True:
        print("Called: matchesPattern('ability', 'ability'")
        print("Expected:", True, "   but function returned:", a1)
        allOk = False
    if a2 != False:
        print("Called: matchesPattern('Ability', 'ability')")
        print("Expected:", False, "   but function returned:", a2)
        allOk = False
    if a3 != True:
        print("Called: matchesPattern('b**m', 'balm')")
        print("Expected:", True, "   but function returned:", a3)
        allOk = False
    if  a4 != False:
        print("Called: matchesPattern('b**m*', 'balm')")
        print("Expected:", False, "  but function returned:", a4)
        allOk = False
    if  a5 != True:
        print("Called: matchesPattern('*****', 'agony')")
        print("Expected:", True, "  but function returned:", a5)
        allOk = False
    
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")       

# Remove the # from the following line to run the test for matchesPattern
#matchesPatternTests()

# ==========================================================================================

# ==========================================================================================
# Tests for collectAllMatches

def collectAllMatchesTests():
    print("--------------------------------------")
    print("Testing collectAllMatches:")
    
    allOk = True
    # We only print a message if a call fails
    sent1 = ['I', 'was', 'going', 'home', 'I', 'was', 'going', 'to', 'bed']
    sent2 = ["Don't", 'bug', 'me', "don't", 'beg', 'me', 'be', 'a', 'big', 'boy', 
             'and', 'bag', 'the', 'bog', 'monster']
    sent3 = ['Frog', 'Toad', 'Ant', 'Caterpillar', 'Deer']
    a1 = collectAllMatches('was', sent1)
    a2 = collectAllMatches('b*g', sent2)
    a3 = collectAllMatches('****', sent3)

    if a1 != ['was', 'was']:
        print("Called: collectAllMatches('was', sent1)")
        print("Expected:", ['was', 'was'], "   but function returned:", a1)
        allOk = False
    if a2 != ['bug', 'beg', 'big', 'bag', 'bog']:
        print("Called: collectAllMatches('b*g', sent2)")
        print("Expected:", ['bug', 'beg', 'big', 'bag', 'bog'], 
              "   but function returned:", a2)
        allOk = False
    if a3 != ['Frog', 'Toad', 'Deer']:
        print("Called: collectAllMatches('****, sent3)")
        print("Expected:", ['Frog', 'Toad', 'Deer'], "   but function returned:", a3)
        allOk = False
    
    if allOk:
        print("Tests Ok")
    print("--------------------------------------")       

# Remove the # from the following line to run the test for collectAllMatches
#collectAllMatchesTests()

# ==========================================================================================
