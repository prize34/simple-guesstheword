#importing libs
import json
import sys
import numpy

#initial setup

number_letters = int(input("How many letters your word have?\n"))
using_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []

have_letters = []
word = ""
multiple = False

#load json file

try:

    with open('./words/{}-letter.json'.format(number_letters)) as f:
        json = json.load(f)
        for w in json:
            words.append(w['word'])

except:
    
    sys.exit('No json file with {} letters'.format(number_letters))

##functions to update the letters and words
def updateAlpha():
    for a in using_alphabet:
        has = False

        for w in words:
            if a in w:
                has = True
                break

        if not(has):
            using_alphabet.remove(a)

def dontHave( letter ):
    global words
    global using_alphabet

    using_alphabet.remove(letter)
    
    new_words = []
    for w in words:
        if not(letter in w):
            new_words.append(w)
    
    words = new_words

def have( letter ):
    global words

    new_words = []

    for w in words:
        if letter in w:
            new_words.append(w)

    updateAlpha()
    words = new_words

##main function
def main():
    global words

    while(len(words) != 1):
        for l in using_alphabet:
            if numpy.array_equal(have_letters, using_alphabet) or len(using_alphabet) == 0:
                if(len(words) > 0):
                    global multiple
                    global word

                    multiple = True
                    for k, w in enumerate(words):
                        word = word + w + ('' if k == (len(words) - 1) else ' or ')
                    return



            if l in have_letters:
                continue

            choice = ""
            while(not(choice.isalpha()) or not((choice.lower().startswith('y') or choice.lower().startswith('n')))):
                choice = input("Your word has {}?".format(l))

            if(choice.lower().startswith('y')):
                have(l)
                have_letters.append(l)
            else:
                dontHave(l)
                break
    word = words[0]

#start

main()

print('Your word is {}!'.format(word))