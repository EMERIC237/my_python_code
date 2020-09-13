#!/usr/bin/env python
# coding: utf-8

'''In this file, I use web scraping to have my poem to count my pi number'''

#import my differents modules

import requests
import bs4
import sys


# Get my url from where I'll grab the poem 

url = requests.get('https://fr.wikisource.org/wiki/D%C3%A9cimales_de_%CF%80')

p = bs4.BeautifulSoup(url.text,'lxml')


#create a function to display the poem only

def final_poem():  
    t=''
    for words in p.select('.poem'):
        t= ''+ str(words.text)
    print(t)


#Store the poem in a text file

orig_stdout = sys.stdout
f = open('pi_poem.txt', 'w')
sys.stdout = f

final_poem()

sys.stdout = orig_stdout
f.close()


