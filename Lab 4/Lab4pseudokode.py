#lab 4 pseudokode.

#Vi fikk ikke jobbet med Lab 4, men vi ønsker å vise fram litt
#pseudokode basert på funksjonene i oppgavespesifikasjonen.
#Koden er ikke testet og er ikke ment for å kjøres.
#Dette er bare en representasjon av noen av idéene vi hadde
#for å gjennomføre oppgaven.

def poker
# Skriver ut alle hender og prøver å returnere hånden
# med høyest rang.
	print deal(n, hender)
	return max(hender, key=hand_rank)

def deal
#Dele ut hender med å velge to tilfeldige verdier fra en
#liste 5 ganger for hver deltager.
ranklist = '23456789TJQKA'
suitlist = 'CDHS'
#Hvordan kan vi dele ut to tilfeldige verdier
#fra en eller to lister samtidig
#som vi passer på at en hver kombinasjon ikke kan gjentas?
#appende alle kort som går inn til hender inn i en egen liste?



def hand_rank
#Sorterer og sjekker hendenes rang i 
#rekkefølge fra beste til "verste" mulige hånd.
#Hver rang kan representeres med f.eks et nummer.
	Straight Flush
		if straigth = True
			if flush = True
				if highcard = 14
					return Royal Straight Flush
						rank = 9
				else
                return Straight Flush
					rank = 8
    Kind(4)
		rank = 7
    elif
    Full house
		rank = 6
    elif
    Flush
		rank = 5
    elif
    Straigth
		rank = 4
    elif
    Kind(3)
		rank = 3
    elif
    Two pairs
		rank = 2
    elif
    Kind(2)
		rank = 1
    else
    High card
		rank = 0

def ranks
#Hvis to hender har samme rank:
#Sammenligne verdiene av kombinasjonen
	
def straigth
#Hvis vi sorterer en hånd etter rank og tar minus - for hvert kort:
#ranks[14, 13, 12, 11, 10]
#if r1 -1 = r2
	if r2 -1 = r3
		if r3 -1 = r4
			if r4 -1 = r5
				straigth = True

def flush
	#Sjekker suit for hvert kort i hånden.
	Hvis nr_dif_suits er 1, betyr det at alle kortene
	#hånden inneholder bare en suit, med andre ord en flush.
	suits = ['SHDC'].index(s) for r, s in hand
	nr_dif_suits = len(set(suits)
    if nr_dif_suits == 1
        flush = True
		
def kind(n, ranks)
	#sjekker om du har n like kort.
	for card in ranks:
		i = ranks.count(card)
            if i == n:
                kind(n) == True
                return card
			
def two_pair
	#Legger like kort i hånden sammen i to forskjellige par.
	pair1 = kind(2, ranks)
	pair2 = kind(2, ranks)
	if pair1 != pair2
	#Hvis disse parene IKKE er like (unngå 4 like under two_pair
	# og at to av de samme kortene legges sammen)
		two_pairs = true
		return (pair1, pair2)
		
def full_house
	pair = kind(2, ranks)
	threes = kind(3, ranks)