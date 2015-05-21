# -*- coding: latin-1 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Adam Ajmi', \
            'student2': 'Fredrik Aass-Hansen', \
			'student3': 'Maria Sandø Andersen', \
            'student4': 'Stian Storbråten', \
            'student5': 'Øystein Traskjær', \
            'student6': 'Erik Oskar Zetterquist', \
            'student7': 'Vetle Horpestad', \
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
def ascii_bird():
	print """       \/_
  \,   /( ,/
   \\\\\\' ///
    \_ /_/
    (./
     '`"""
ascii_bird()
# \ er en "escape character" og må derfor dobles for hver linje som skal skrives ut

#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre

def bitAnd(a, b):
    print "performing bitAnd operation:"
    return a & b

bitwiseAnd = bitAnd(6, 5)

print "bitAnd: %d" % (bitwiseAnd)

#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(a, b):
    print "performing bitXor operation:"
    return a ^ b
    
bitwiseXor = bitXor(4, 5)

print "bitXor: %d" % (bitwiseXor)    
#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(a, b):
    print "performing bitOr operation:"
    return a | b
    
bitwiseOr = bitOr(0, 1)

print "bitOr: %d" % (bitwiseOr)

#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#	 Forklar resultatet ascii8Bin('å')
#	 Hvilke faktorer påvirker resultatet? Forklar.
#
def ascii8Bin(letter):
    lettervar = ord(letter)
    toBin = "{0:08b}".format(lettervar)
    print(toBin)

print "Letter in binary is:" 
	


# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def transferBin(string): 
	l = list(string)
	for c in l:
		print "Binary representation for %s =" % c
		ascii8Bin(c)
		
print transferBin("Python")
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)
		# print "Den binære representasjonen for %s" % c


#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  
def ascii2Hex(letter):
	lettervar = ord(letter)
	toHex = "{:02x}".format(lettervar)
	print(toHex)


def transferHex(string):
	l = list(string)
	for c in l:
		print "Hexadecimal representation for %s" % c
		ascii2Hex(c)

print transferHex("Python")
#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen

def unicodeBin(letter):
    lettervar = ord(letter.decode("utf8"))
    toBin = "{0:08b}".format(lettervar)
    print(toBin)

print "Letter Å in binary is:"
unicodeBin("Å")  

#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#

def SystemInfo():
    
	mem = psutil.virtual_memory()
	hdd = psutil.disk_partitions()
	cpu = psutil.cpu_percent()
	
	print "Memory info: " + str(mem) 
	print "HDD info: " + str(hdd)
	print "CPU usage: " + str(cpu)
	
SystemInfo()
pass

def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	# assert ascii8Bin('a') == 01100001
	# assert ascii8Bin('A') == 01000001
	# Skriv her inn passende tester for tarnsferBin og transferHex funksjoner
	# fra oppgavene 6 og 7
	# assert unicodeBin('å') == '11100101'
	# Dine egne tester
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()