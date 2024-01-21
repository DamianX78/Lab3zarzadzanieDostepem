# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:50:57 2024

@author: Damian Spyra

Lista nr3 cz1
"""

import base64


def baseCode(text):
    text2code = text
    
    '''Konwersja do danych binarnych jest wymagana gdyż w takim formacie 
    base64 przyjmuje dane. Dodatkowo utf-8 uzupełnia długosc do 8 znaków
    stosując 0 i 1 wiodace co też jest ważne dla base64'''
    
    toBinary = text2code.encode('utf-8')
    codeData = (base64.b64encode(toBinary)).decode('utf-8') #kodowanie napisu i prezentacja w postaci tekstowej
    print()
    print("Twój napis zakodowany przy pomocy base64: ", codeData)
    
    
if __name__ == "__main__":
    
    userData = input('Podaj napis do zakodowania i zatwierdz kalawiszem ENTER: ')
    baseCode(userData)
