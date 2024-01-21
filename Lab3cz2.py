# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:50:57 2024

@author: Damian Spyra

Lista nr3 cz2
"""

import random


password = []
sep = ''

''''Funkcja generuje losowe hasła o długosci 32 znakow. Mozna wprowadzic
losowosc w generowaniu dlugosci hasla, jak i generowanie hasla tylko z 
unikalnych znakow. Ale mialo byc prosto i kompaktowo ;) '''

def randPass():
    for i in range(1, 33):
        randomChar = random.randint(33, 125)
        if randomChar != 92: # to jest ukosnik w lewo zostal usuniety jako znak funkcyjny
            password.append(chr(randomChar))
    return password


if __name__ == "__main__":
    
    print()
    print("To jest generator losowego hasla.")
    print()
    print("Twoje losowe hasło: ", sep.join(randPass()))


    