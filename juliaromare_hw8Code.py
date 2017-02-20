#  Name: Julia Romare
#  Homework 8: Working with Text
#  Date: 11/12/2015
#  COMP 123-05
#  Professor: Katherine Kinnaird
#  Peer resources: Ramon Molina
#


import string

# -------------------------------------------------------------------------------------------------
# Question 1

def readWordList(filename):
    """Takes in a filename and reads the text from the file.  It assumes one word per line,
    and removes any whitespace from the front or end. It returns a list of the words"""
    fil = open(filename, 'r')
    words = []
    for line in fil:
        word = line.strip()
        words.append(word)
    fil.close()
    return words


# Put your definition of readTextList here

def readTextList(filename):
    """Takes in a filename and reads the text from the file. It reads the text from the line,
    split it into words and strip it from the punctuation. We do not assume one word per line.
    It returns a list of the words"""
    fil = open(filename, "r") #Opening up FILENAME and prepare for reading.
    vari = fil.read() #Reading the file and return string VARI.
    words = [] #Create empty list, WORDS.
    text_to_words = vari.split() #Splits the string VARI into a list, TEXT_TO_WORDS.
    for line in text_to_words: 
        word = line.strip(string.punctuation) #Striping all leading or following puncutation from the word.
        words.append(word) #Append WORD to the list WORDS.
    fil.close() #Close FIL.
    return words #Return the list WORDS.


 
# -------------------------------------------------------------------------------------------------
# Question 2

# Put your definition of findContaining here

def findContaining(string, lst_words):
    """Takes a string, STRING, and a list of words, LST_WORDS, as inputs.
    If a word from the list contains the substring, STRING, it will add the 
    word to a new list."""
    lst = [] #Create an empty list, LST, which will contain all words containing substring, STRING.
    for word in lst_words: #Iterates over each word in LST_WORDS.
        if string in word: #If STRING is a substring of WORD, append to LST.
            lst.append(word)
    return lst #Return the list, LST.



# -------------------------------------------------------------------------------------------------
# Question 3

# These functions implement a simple program to read in text from a file and compute the frequency
# of consonants in the text


def consonantCountFile(filename):
    """Takes in a filename and opens it for reading.  It reads in the contents of the file as 
    a string, and then calls the letterFreq function to compute the frequency table.  It then
    returns that table as the value of this function"""
    fil = open(filename, 'r')
    text = fil.read()
    fil.close()
    freqTable = CountConsonants(text)
    return freqTable



# Put your definition of countConsonants here

def countConsonants(string_text):
    """Takes in a string of text, STRING_TEXT.Creates a dictionary
    which holds how often each consonant occurs in the string. 
    The keys are consonants and the associated values is how many times
    it is seen in the string."""
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'] #Creating a list with all consonants.
    freqTable = {} #Create empty dictionary, FREQtABLE.
    for letter in string_text: #Iterate over characters in a STRING_TEXT.
        letter = letter.lower() #Make LETTER into lower key.
        if letter in consonants: #If LETTER is a consonant, proceed.
            if letter in freqTable: #If LETTER already have key-value pair, add one to the value. 
                freqTable[letter] = freqTable[letter] + 1
            else: 
                freqTable[letter] = 1 #Initializing a key-value in FREQtABLE with LETTER as the key and a value of 1.  
    return freqTable #Returns FREQtABLE.
        


# -------------------------------------------------------------------------------------------------
# Question 4


# Put your definition of collectAllMatches here

def collectAllMatches(patt,lst):
    """Takes in a pattern, PATT and a list of words, LST.
    Creates and returns a list of the words from LST that match
    the pattern."""
    match_lst = [] #Create an empty list, MATCH_LST.
    for word in lst: #Iterates over each word in LST.
        if matchesPattern(patt,word) == True : #Calls on matcherPattern and providing inputs PATT and WORD. If True, the word matches the pattern.
            match_lst.append(word) #Append word to MATCH_LST.
    return match_lst #Return MATCH_LST, the list containing all words that match the pattern.



def matchesPattern(patt, word):
    """Takes in two strings, a pattern string and a word string, and it
determines if they match.  If their lengths are different, then they don't
match.  If their lengths are the same, then they must match exactly, unless
the pattern string contains a *, in which case it matches any letter in the
word string.  This function returns True or False"""
    if len(patt) != len(word):
        return False
    for i in range(len(patt)):
        if patt[i] != "*" and patt[i] != word[i]:
            return False
    return True


