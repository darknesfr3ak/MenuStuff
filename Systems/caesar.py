import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))) # Fix for relative imports, generic had some troubles
from generic import *

# Settings
UseEasyMethod = False

# Caeser Functions
ToMoveLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,;:()[] "
# ^ sollten Zeichen fehlen die man in der Nachricht verwenden will, einfach hinzufügen

def move_alphabet(letters, shift): # Shifts the alphabet by a given number
    newletters = []
    for i,v in enumerate(letters):
        if UseEasyMethod:
            newletters.append(chr(ord(v)+shift)) # Use chr and ord to convert the letter to its ASCII value and back + shift
        else:
            newletters.append(ToMoveLetters[(ToMoveLetters.index(v)+shift)%len(ToMoveLetters)]) # Use a list of characters to shift the letter
    return newletters


checkfor = ["ll","ss","mm","sch","ch","ie","ei","au","eu"] # Checks for common german letter combinations
def is_real_sentence(sentence_list): # Checks if the sentence is a "real sentence"
    sentence = combine_list_to_sentence(sentence_list)
    for i, v in enumerate(sentence):
        if i < len(sentence)-1:
            if sentence[i]+sentence[i+1] in checkfor:
                return True


def caeser_getkey(sentence_list): # Tries to get the key of a caeser encrypted sentence
    possible_sentence = []
    possible_key = []
    for i in range(1, len(ToMoveLetters)):
        temp_sentence = move_alphabet(sentence_list, -i) # Temporary sentence, moved by -i
        if is_real_sentence(temp_sentence):
            possible_sentence.append(temp_sentence)
            possible_key.append(i)

    return possible_key, possible_sentence