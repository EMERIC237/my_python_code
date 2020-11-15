#!/usr/bin/env python
# coding: utf-8

'''Now,we actually find our decimal of pi using the previous text file'''

import string
global test
global letters

#function the get the correct test(without any puntuations)
def rigt_test():
    global test
    
    f = open('out.txt',"r")
    test = f.read()
    words = test.split()
    words[1] = "j'aime"
    words[38] = "l'admirable"
    words[40] = "l'oeuvre"
    words[69] = "l'espace"
    words[97] = "s'y"
    words[106] = "l'orbe"
    words[114] = "l'arc,"
    test = ' '.join(words)
    return  test
rigt_test()

#function to get the value of pi according to the user desired
def count_pi():
    global test
    global letters
    
# initializing punctuations string 
    punc = string.punctuation

# Removing punctuations in string Using loop 
    for ele in test: 
        if ele in punc:
            test = test.replace(ele, " ")
    words = test.split()
    letters = [str(len(w)) for w in words]
    letters[0] = "3,"
    return letters
count_pi()
    
def pi_decimal():
    global letters
    
    numberd = input('enter your desired decimal pi number(must be less than 120): ')
    while numberd not in [str(person) for person in range(1, 120)]:
        numberd = input("invalid choice. Please choose a number from 1 to 120 : ")
    numberd = int(numberd)           
    if numberd > 120:
        print("invalid entry, please try again")
        pi_decimal()
    else:
        pi_list = letters[0:numberd+1]
        pi = ''.join(pi_list)
        print('you choosed {} decimals of pi'.format(numberd))
        print('your pi value is :{}'.format(pi))

if __name__=="__main__":
    pi_decimal()

