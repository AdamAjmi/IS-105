#lab 4 pseudokode.
from collections import Counter

#Udacity-kode
def deal_cards(allhands, n=5, deck=[r+s for r in for r in '23456789TJQKA' for s in 'SHDC']):

def poker(hands):
    print hands
    print "The winning hand:"
    return max(hands, key=hand_rank)

def hand
def hand_rank(hand)
    #Udacity
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    #Vår kode
	suits = ['SHDC'].index(s) for r, s in hand
    #Udacity
    ranks.sort(reverse = True)
	nr_dif_ranks = len(set(ranks))
	if ranks == [14, 5, 4, 3, 2]:
		ranks = [5, 4, 3, 2, 1]
    #vår kode
    nr_dif_suits = len(set(suits)
    if nr_dif_suits == 1
        flush = True
    first, last = ranks[0], ranks[-1]
    if first - last == 4
        straigth = True
    #Henter ut første og siste verdi fra en liste.
    Straight Flush
    if straigth = True
        if flush = True
            if highcard = 14
                return Royal Straight Flush
            else
                return Straight Flush
    Kind(4)
    elif
    Full house
    elif
    Flush
    elif
    Straigth
    elif
    Kind(3)
    elif
    Two pairs
    elif
    Kind(2)
    elif
    High card
    else
    
def ranks
def straight
Fra 14 (ace) til 6,5,4,3,2 laveste straigth.
    9 mulige straigths
    if  highest card - lowest card = 4
      
    if max(ranks) - min(ranks) == 4
        hand = straight
    
def flush(hand)
Kunne skille mellom suit og rank
    len(set(hand))
    
    Kan vi bruke en counter?
    For s, r in hand:
        Counter(s)
        Counter({'S': 4, 'D' : 1 etc...}) 
    for s, r in hands:
        hands.count(S)
        hands.count(D)
        hands.count(C)
        hands.count(H)
        
def kind(n, ranks)
    for card in ranks:
        i = ranks.count(card)
            if i == n:
                kind(n) == True
                return card
print kind(2, ranks):

def two_pairs
    pair1 = kind(2, ranks)
    pair2 = kind(2, ranks)
    if pair1 != pair2
        two_pairs = True
        return (pair1, pair2)
    else
        return none

def max



#Shufflefunksjoner fra Udacity ligger under.

def shuffle1(deck):
    # O(N**2)
    # incorrect distribution
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2(deck):
    # O(N**2)
    # incorrect distribution?    
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2a(deck):
    # http://forums.udacity.com/cs212-april2012/questions/3462/better-implementation-of-shuffle2
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        j = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle3(deck):
    # O(N)
    # incorrect distribution    
    N = len(deck)
    for i in range(N):
        j = random.randrange(N)
        deck[i], deck[j] = deck[j], deck[i]

def shuffle(deck):
    # Knuth method
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i] 