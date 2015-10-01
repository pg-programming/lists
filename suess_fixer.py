#!/usr/bin/env python

# import some modules so that we get some extra functionality
import os
import sys
from copy import copy

def modify_line(line, letter):
  """ modifies the given line by finding and uppercasing """
  count = 0
  if letter in line:
    line = line.replace(letter, copy(letter).upper(), 1)
    count = 1
  return count, line

def has_substr(line, chars):
  """ checks to see if the line has one of the substrings given """
  for char in chars:
    if char in line:
      return True
  return False


def main():
  ''' This is the main function that is our initial entry point into our program '''
  # clear the console screen
  os.system('clear')

  filename = 'green_eggs_and_ham.txt'
  filename_fixed = 'green_eggs_and_ham_fixed.txt'

  # remove file if it exists
  if os.path.exists(filename_fixed):
    os.remove(filename_fixed)

  # keep track of the lines in the file
  lines = []

  # the list of possible i's in the file
  i_list = ['i ', ' i ', '-i-', ' i\n']

  # read all of the lines from the file into a list
  with open(filename) as f:
    lines = f.readlines()


  ### START YOUR CODE HERE ###

  # find every instance of ' i ' and '-i-' and uppercase it. make sure you keep
  # track of how many fixes you make and the line numbers of each fix

  # keep track of count, a list of line numbers, and the modified lines

  # iterate over every line in the list of lines (you might find it helpful to 
  # start your enumeration at 1)

    # loop while the line still has a bad i
      # loop over each character in our i_list to make sure that our line 
      # doesn't have any bad i's
        # modify our line
        # if our modification said that it modified the line
          # append the line number to our list of line numbers
        # add to our count of fixes
    # append each line to our new lines (so that we have the fixed versions)

  # print your results of fixed instances and the list of line numbers
  

  ### END YOUR CODE HERE ###


  # write the fixed lines to a new file
  with open(filename_fixed, 'w') as f:
    for line in new_lines:
      lines = f.write(line)

  correct_lines = []
  with open('green_eggs_and_ham_correct.txt') as f:
    correct_lines = f.readlines()

  the_same = correct_lines == new_lines

  print '\nYour solution is %scorrect!' % ('' if the_same else 'NOT ')

  # wait for the user to press enter to quit
  raw_input('\nPress enter to quit...')

  # clear the console screen
  os.system('clear')


# this makes it so that when you run your file that it will call the main
# function. It is always good practice to do this. We put all of the runtime
# functionality in the main function
if __name__ == '__main__':
  main()
