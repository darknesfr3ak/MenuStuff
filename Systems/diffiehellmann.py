import random

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))) # Fix for relative imports, generic had some troubles
from generic import get_random_prime

def get_Infos():
    # Client A
    p = get_random_prime(10000, 100000) # Primzahl
    g = random.randint(1, p-1) # Natürliche Zahl kleiner als p

    a = random.randint(1, p-1)

    # Client B
    b = random.randint(1, p-1)

    # Client A
    A = pow(g, a, p) # bzw, pow(g, a, p) bzw, (g ** a) % p

    # Client B
    B = pow(g, b, p)

    return p, g, a, b, A, B

def get_Key(B=0, a=0, p=0, A=0, b=0):
    
    p, g, a, b, A, B = get_Infos()

    # Client A
    KeyA = pow(B, a, p)

    # Client B
    KeyB = pow(A, b, p)

    return KeyA, KeyB