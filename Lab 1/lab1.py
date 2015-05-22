# -*- coding: utf-8 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys
#import psutil
#Import importerer og instansierer andre moduler slik at modulens funksjoner
#kan tas i bruk uten at koden må stå i denne filen.

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Adam Ajmi', \
            'student2': 'Fredrik Aass-Hansen', \
            'student3': 'Maria Sandø Andersen', \
            'student4': 'Stian Storbråten', \
            'student5': 'Øystein Traskjær', \
            'student6': 'Erik Oskar Zetterquist', \
            'student7': 'Vetle Horpestad', \
}


#  Oppgave 1
def ascii_bird():
    print """       \/_
  \,   /( ,/
   \\\\\\' ///
    \_ /_/
    (./
     '`"""
ascii_bird()
# \ er en "escape character" og må derfor dobles for hver linje som skal skrives ut.

#  Oppgave 2
def bitAnd(a, b):
    #def er et reservert ord som definerer en funksjon.
    #bitwise AND sier noe om hvilke bits som er identiske. Identiske bits gir 1.
    #Forskjellige bits gir 0.
    return a & b
    #return er et reservert ord som definerer slutten av en funksjon
    #og sender data tilbake til funksjonen.
bitwiseAnd = bitAnd(6, 5)

print "bitAnd: %d" % (bitwiseAnd)
print ""
    #print er et reservert ord som skriver noe ut i terminalen.

#  Oppgave 3
def bitXor(a, b):
    #Sier noe om hvilke bits som er ulike. Identiske bits gir 0.
    #Ulike bits gir 1.
    return a ^ b
    
bitwiseXor = bitXor(4, 5)

print "bitXor: %d" % (bitwiseXor)    
print ""

#  Oppgave 4
def bitOr(a, b):
    #Sier noe om en eller begge bitene har en verdi av 1.
    #Hvis a eller b har 1 i spesifisert bit får vi 1.
    #Hvis hverken a eller ba har 1 i spesifisert bit får vi 0.
    return a | b
    
bitwiseOr = bitOr(0, 1)

print "bitOr: %d" % (bitwiseOr)
print ""

#  Oppgave 5
def ascii8Bin(letter):
    
    lettervar = ord(letter)
    #ord er en funksjon som gir oss en representasjon av variabelens
    #byteverdi i ordinære tall.
    return "{0:08b}".format(lettervar)
    # .format formaterer en string (lettervar) etter argumentene vi ga foran
    # punktumet. 
    #Formatteringsstrengen forklart:
    #      {} setter en variabel inn i strengen
    #      0 tar variabelen i argument posisjon 0
    #      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
    #      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
    #      b konverterer tallet til dets binære representasjon
    print(toBin)

# print ascii8Bin('å')
# Når vi prøver å kjøre denne funksjonen, får vi feilmelding.
# "ord() expected a character, but string of length 2 found"
# Dette er fordi 'å' representeres med to bytes i unicode.


#  Oppgave 6
def transferBin(string): 
    l = list(string)
    #Vi legger input-stringen inn i en liste med variabelnavn l.
    #En liste er en datastruktur med flere verdier i en slags array.
    output = ""
    #Output defineres som en tom string.
    for c in l:
    #En for-løkke som sier "For hvert tegn i liste l:".
    #for er et reservert ord i python.
        output += ascii8Bin(c) + " "
        # += er en operator som sier at variabel til høyre legges sammen med
        # variabel til venstre og at de nå er like.
        #Vi påkaller funksjonen ascii8Bin for hvert tegn i listen.
        # " " på slutten skaper white-space mellom de to variablene.
    return output

print "Every letter in the word Python in binary:"    
print transferBin("Python")
print ""

#  Oppgave 7
def ascii2Hex(letter):
    lettervar = ord(letter)
    return "{:02x}".format(lettervar)
    #02 formatterer variabelen til to tegn.
    #x formatterer variabelen til hexadesimaler.
    print(toHex)


def transferHex(string):
    l = list(string)
    output = ""
    for c in l:
        output += ascii2Hex(c) + " "
        ascii2Hex(c)
    return output

print "Every letter in the word Python in hexadecimals:"
print transferHex("Python")
print ""

# Oppgave 8
def unicodeBin(letter):
    #Hvordan kan vi skrive denne om til å behandle små unicode tegn?
    #Disse har to bytes istedenfor en!
    output = ""
    lettervar = ord(letter.decode("utf8"))
    #Decoder stringen etter codec definert i parantes.
    return "{0:08b}".format(lettervar) 

print "The unicodeletter 'Ø' in binary:"
print unicodeBin('Ø')
print ""

#Får ikke innstallert psutils!
#Noen andre må ta for seg oppgave 9.

# Oppgave 9
#   Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
#           Brand and model
#           Hard drive capacity
#           Amount of RAM
#           Model and speed of CPU
#           Display resolution and size
#           Operating system
#   
#   Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#   Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#   Kan dere skrive en test for denne funksjonen?
#   Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#

#def printSysInfo():
#printSysInfo()
#pass

def test():
    print "--------------------------------------------------------------------"
    print "Starter testing..."
    assert bitAnd(6, 5) == 4
    #Assert kjører en funksjon med gitte variabler og tester resultatet med en
    #forhåndsdefinert verdi. Hvis den forhåndsdefinerte verdien
    #ikke matcher returnverdien til funksjonen vil det
    #oppstå en feilmelding.
    assert bitXor(4, 5) == 1
    assert bitOr(0, 1) == 1
    assert ascii8Bin('a') == '01100001'
    assert ascii8Bin('A') == '01000001'
    assert transferBin('One') == '01001111 01101110 01100101 '
    assert transferHex('Two') == '54 77 6f '
    assert unicodeBin('Å') == '11000101'
    return "Testene er fullført."
# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
