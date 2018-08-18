#!/usr/bin/env python

#This Algorithm parses a file
#It could contain positive and negative integers,
#Squares each number detected,
#Sums each new element

File_Path = 'Drive:/To/your/File_Path/File.ext' #Path of the File to be parsed.

with open(File_Path) as fp: #Opens the selected file.
    Array_of_Numbers = [line for line in fp] #Saving the numbers to a list, i.e ['1 22 333 4444']
    Array_of_Numbers = line.split(" ") #Splitting each element separated by a white_space, adding a comma; i.e ['1', '22', '333', '4444']. It creates an array of Strings.
    Array_of_Numbers = [int (numeric_string) for numeric_string in Array_of_Numbers] #Converting the Array of strings to an Array of Numbers; i.e [1, 22, 333, 4444]. By using the int function
    Array_of_Numbers = [Square_Each_Element**2 for Square_Each_Element in Array_of_Numbers] #Squares each element of the array
    Sum_Array_of_Numbers = sum(Array_of_Numbers) #Sums each element of the Array
    print Sum_Array_of_Numbers #Prints the Sum