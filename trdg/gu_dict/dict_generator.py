# A. Generate a Gujarati Dictionary with- 
#       - Only the 397 characters in consideration
#       - Around 50k words
#       - Roughly equal no. of occurances of characters - 2000 each
# ROUGH STEPS
#       1. initialise a weights list with 397 equal numbers (big or small?)
#          (alternatively, increase the weights of complex characters here only)
#       2. for loop of 50k
#       3.    select a random word length (L) from [1 - 7]
#       4.        for loop of L
#       5.           select a random character from space.names (with weights)
#       6.           append it to the word
#       7.           increase weights of all other chars / decrease weight of this char
#       8.        write word in file

# B. A separate Dictionary for 'Complex' characters which will be used 
#    to add additional images in the dataset for these characters. 

# C. A dictionary for testing dataset with only real words taken from
#    the Gujarati Wiki dataset, that satisfy the space.names filter.

import random
import os
from collections import Counter

import numpy as np
import matplotlib
from matplotlib import pyplot
import matplotlib.font_manager as font_manager

newFontEntry = font_manager.FontEntry(
    fname='/home/pika/Desktop/TIFR/YOLO-AppV2.0/trdg-dataset/TRDG/trdg/fonts/gu/Aakar.ttf',
    name='Aakar')
font_manager.fontManager.ttflist.insert(0, newFontEntry)
matplotlib.rcParams['font.family'] = newFontEntry.name

CWD = os.getcwd() 

spaceNamesFile = open(CWD+'/distribution_final/space.names', 'r')
spaceNames = [char.strip() for char in spaceNamesFile.readlines()]
spaceNames[spaceNames.index('Space')] = ' '

complexChars = spaceNames[0 : 5]
choiceList = []

for char in spaceNames:
    if char in complexChars:
        choiceList.extend([char]*5)
    else:
        choiceList.extend([char]*3)

choiceList.extend([' '] * 1)

dictFile = open(CWD+'/distribution_final/gu.txt', 'w')
dictSize = 880
sentenceLengths = range(20, 30)

def simple_random():
    for _ in range(dictSize):
        l = random.choice(sentenceLengths)
        sentence = ''
        for _ in range(l):
            char = random.choice(choiceList)
            sentence += char
        dictFile.write(" ".join(sentence.split())+'\n')
        
def calculate_distribution():
    dictFile = open(CWD+'/distribution_final/gu.txt', 'r')
    guDict = [word.strip() for word in dictFile.readlines()]

    maatras = ['ા', 'િ', 'ી', 'ુ', 'ૂ', 'ે', 'ૈ', 'ો', 'ૌ']
    charList = []

    for word in guDict:
        for i in range(len(word)): 
            if word[i] in maatras: continue 
            piece, j = word[i], i + 1
            while j < len(word) and word[j] in maatras: 
                piece += word[j]
                j += 1
            
            charList.append(piece) 

    return Counter(charList)

def plot_distribution(count_dict):

    x_labels = [char for char in count_dict.keys()]
    y_points = list(count_dict.values())

    # print(len(x_labels), len(y_points))

    pyplot.figure(figsize=(40, 10))
    pyplot.bar(x_labels, y_points, width=0.3, align='center', color='g')

    i=1.0
    j=50
    for i in range(len(x_labels)):
        pyplot.annotate(y_points[i], (-0.1 + i, y_points[i] + j))

    pyplot.title("Character Distribution of Gujarati Images Training Data")
    pyplot.xlabel("Characters")
    pyplot.ylabel("Frequency")

    pyplot.savefig('distribution_final/guDict.png', facecolor='white')

def write_distribution(distrbution):
    dist_file = open('distribution_final/gu_dist.txt', 'w')
    for k in ['અ', 'કિ', 'છા', 'જૂ', 'ણો', 'ત', 'રા', 'ડે', 'ન', 'ઘ', ' ']:
        dist_file.write(k + ' ' + str(distrbution[k]) + '\n' if k != ' ' else 'Space' + ' ' + str(distrbution[k]) + '\n')


if __name__ == '__main__':
    simple_random()
    distrbution = calculate_distribution()
    print(distrbution)
    plot_distribution(dict(distrbution))
    write_distribution(distrbution)
    pass
