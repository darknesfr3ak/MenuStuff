import random
# Generic Functions

def turn_sentence_to_list(sentence): # Turns a sentence into a list of characters
    alphabeticlist = []
    for i, v in enumerate(sentence):
        alphabeticlist.append(v)
    return alphabeticlist
    
def combine_list_to_sentence(list): # Turns a list of characters into a sentence
    sentence = ""
    for i in list:
        sentence += i
    return sentence



def is_prime(n): # Basic Prime Check
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_random_prime(min_value, max_value):
    primes = []
    for i in range(min_value, max_value):
        if is_prime(i):
            primes.append(i)
    return random.choice(primes)