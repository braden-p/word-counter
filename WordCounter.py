#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WordCounter
Created by Braden Piper, bradenpiper.com
Created on Tue Jul 5, 2022
version = 1.0
------------------------------------------
WordCounter is a simple, friendly program that will count the number of times a
specific text string appears in a body of text. The user provides the key word and the
body of text via input.
------------------------------------------
"""

# FUNCTION DEFINITIONS

def wordCounter(keyword, textBody):
    '''
    Accepts a keyword (string), and a body of text (string).
    Both strings should be lowercase.
    Prints an int, the number of times the keyword appears in the body of text.
    '''
    index = -1         
    wordCount = 0
    for letter in textBody:   # iterate through all letters in the textBody
        index += 1            # add 1 to the index counter for each letter we iterate through
        if letter == keyword[:1]:     # look for the first letter in the keyword
            bookmark = index          # store it's index in bookmark
            if textBody.count(keyword, bookmark, (bookmark+len(keyword))):     # check if the first letter leads to the rest of the word
                wordCount += 1                               # if it does, add 1 to wordCount
    print('Number of times',keyword,'occurs is:', wordCount) # print wordCount

def replayQuery():
    '''
    Asks the user if they want to run the program again.
    Returns a boolean. True if the answer is yes, False if the answer is no.
    '''
    yesAnswers = ['y','Y','yes','Yes','YES']
    noAnswers = ['n','N','no','NO']
        
    while True:
        print('Would you like me to count any more words for you?')
        print('y / n')
        answer = input()
        if answer in yesAnswers:
            return True
        elif answer in noAnswers:
            return False
        else:
            print("I did not understand your answer, please type 'y' or 'n' to answer.")


# PROGAM          
  
runProgram = True  

# Intro
print("Hello, I am WordCounter. I count the number of times a particular word appears in the body of text you input.")
print('You may search for a particular word, or any piece of text you like, such as a phrase, a name, or even a punctuation mark.')
print('For your convenience, my search algorithm is not case sensitive.')

while runProgram == True:  
    keyword = input('What word would you like to count? Type your response, then press Enter: ').lower()
    textBody = input('Please input the text body you would like to search through, then press enter: ').lower()
    wordCounter(keyword, textBody) # run wordCounter func, prints count of keyword
    
    # Ask user if they want to run the program again
    if replayQuery() == False:    # run replayQuery func, returns a bool
        runProgram = False        # if False, end program
      
# Outro
print('Leaving so soon?')
print('If you ever need someone to count words for you, I am happy to be of service.')
print('Goodbye.')

