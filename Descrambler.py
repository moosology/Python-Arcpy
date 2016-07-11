###############################################################################
#
# Author: Christian Snelgrove
# Purpose: Takes scrambled geocaching clues as input and unscrambles them
# Date Created: 7/10/2016
# Last Modified: 7/10/2016
#
###############################################################################


secret = list(raw_input('Please type the secret: ')) # Take user input of secret
lower_letters1 = list('abcdefghijklm') # First half of alphabet in a list lower case
lower_letters2 = list('nopqrstuvwxyz') # Second half of alphabet in a list lower case
upper_letters1 = list('ABCDEFGHIJKLM') # First half of alphabet in a list upper case
upper_letters2 = list('NOPQRSTUVWXYZ') # Second half of alphabet in a list upper case

unscrambler = [] # Empty list to store other lists that have characters and their matching alternate
temp = 0 # Used to manually iterate in later for-loops

for char in lower_letters1: # Opens up for loop
    temp_list = [] # Sets empty, tempory list to add to unscrambler
    temp_list.append(char) # Adds in original character
    temp_list.append(lower_letters2[temp]) # Adds in unscrabmled character
    temp += 1 # Adds 1 to manual iterator
    unscrambler.append(temp_list) # Adds list to unscrambler list

temp = 0
    
for char in lower_letters2:
    temp_list = []
    temp_list.append(char)
    temp_list.append(lower_letters1[temp])
    temp += 1
    unscrambler.append(temp_list)
    
temp = 0

for char in upper_letters1:
    temp_list = []
    temp_list.append(char)
    temp_list.append(upper_letters2[temp])
    temp += 1
    unscrambler.append(temp_list)

temp = 0

for char in upper_letters2:
    temp_list = []
    temp_list.append(char)
    temp_list.append(upper_letters1[temp])
    temp += 1
    unscrambler.append(temp_list)

unscrambler.append([' ', ' ']) # Allows for spaces in secret to be maintained
unscrambler.append(['.', '.']) # Allows for periods to be maintained
solved = '' # Empty to string to store descrambled text

###############################################################################
#
# Explanation of lines 65--82:
# First, a for loop is created to pull each character from the list of scrambled
# characters. Then, a for loop is created to test that character against each 
# list pair in the unscrambler object. The stop variable is used to end the while
# loop. Under the while loop, first the char is tested to see if it matches the 
# first pair. If it does, that character is added to the final output, stop
# variable ends the while loop, break command ends the second for loop, and a 
# new character is selected. If it does not the while loop is ended, stop is 
# reset to zero, and the next pair is tested. 
#
###############################################################################

for char in secret: 
    stop = True
    
    for pair in unscrambler: 
        stop = True
        
        while stop == True:
            
            if char == pair[0]:
                solved += pair[1]
                stop = False
                break
            
            elif char != pair[0]:
                stop = False

print 'Solved Secret:', solved
