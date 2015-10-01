#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys

def main():
  ''' This is the main function that is our initial entry point into our program '''
  # clear the console screen
  os.system('clear')

  # ask for whether they want prime checking or nth prime
  word = raw_input('What word would you like to check as a palindrome? ')

  # store any variables you will need (the list)
  new_word = []

  # reverse the word and store in a list
  for char in word:
    new_word.insert(0, char)

  # compare the words and print the results
  print 'It is ' + str(new_word == list(word)) + ' that the word is a palindrome\n'


  # wait for the user to press enter to quit
  raw_input('\nPress enter to quit...')

  # clear the console screen
  os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
  main()
