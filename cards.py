from string import *
import random

suits = ['S', 'C', 'D', 'H']
longsuits = ['spades', 'clubs', 'diamonds', 'hearts']

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
longranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'jack', 'queen', 'king', 'ace']

ranklist = string.join(ranks, "")

ranklookup = {}
for i in range(len(ranks)):
    ranklookup[ranks[i]] = i

suitlookup = {}
for i in range(len(suits)):
    suitlookup[suits[i]] = i

class Card:
    """
    Class to hold information about a single playing card.  The card rank
    and suit are stored.

    The constructor takes two arguments, the rank and suit of the card.  The
    rank and suit must be values from the ranks and suits list.

    >>> c1 = Card('8', 'C')
    >>> c2 = Card('K', 'H')
    >>> print c1
    8C
    >>> print c2
    KH
    """

    def __init__(self, rank, suit):
        self.__rank = ranklookup[rank]
        self.__suit = suitlookup[suit]

    def __cmp__(self, other):
        """
        Compare two card objects.

        >>> c1 = Card('8', 'C')
        >>> c2 = Card('K', 'H')
        >>> c1<c2
        True
        >>> c1>c2
        False
        >>> c1==c2
        False
        """
        if self.__rank == other.__rank:
            return cmp(self.__suit, other.__suit)
        else:
            return cmp(self.__rank, other.__rank)

    def __str__(self):
        """
        Return a two-character string representing the card.

        >>> c1 = Card('8', 'C')
        >>> str(c1)
        '8C'
        """
        return self.shortname()
    def __repr__(self):
        """
        Return a the Python code required to construt the card.

        >>> c1 = Card('8', 'C')
        >>> print repr(c1) .split(".",1)[1]
        Card('8', 'C')
        """
        return "%s.Card('%s', '%s')" % (self.__module__, ranks[self.__rank], suits[self.__suit])

    def suit(self):
        """
        Return a character representing the card suit.  This will be one of the
        characters from suits.

        >>> c1 = Card('8', 'C')
        >>> c1.suit()
        'C'
        """
        return suits[self.__suit]

    def rank(self):
        """
        Return a character with the card rank.  This will be one of the
        characters from ranks.

        >>> c1 = Card('8', 'C')
        >>> c1.rank()
        '8'
        """
        return ranks[self.__rank]

    def shortname(self):
        """
        Output a short two-character description of the card.

        >>> c1 = Card('8', 'C')
        >>> c1.shortname()
        '8C'
        """
        return ranks[self.__rank] + suits[self.__suit]

    def longname(self):
        """
        Return a long English description of the card.

        >>> c1 = Card('8', 'C')
        >>> c1.longname()
        'eight of clubs'
        """
        return longranks[self.__rank] + " of " + longsuits[self.__suit]



testhand = [ Card('9', 'H'), Card('6', 'C'), Card('7', 'S'), Card('6', 'D'), Card('A', 'H') ]

def deck():
    """
    Return an *unshuffled* deck of cards (list of card objects).

    >>> d = deck()
    >>> print hand_string(d)
    2S 3S 4S 5S 6S 7S 8S 9S TS JS QS KS AS 2C 3C 4C 5C 6C 7C 8C 9C TC JC QC KC AC 2D 3D 4D 5D 6D 7D 8D 9D TD JD QD KD AD 2H 3H 4H 5H 6H 7H 8H 9H TH JH QH KH AH
    >>> print len(d)
    52
    """
    d = []
    for suit in range(len(suits)):
        for rank in range(len(ranks)):
            c = Card(ranks[rank], suits[suit])
            d.append(c)

    return d


def small_deck():
    """
    Return a small *unshuffled* deck of cards (list of card objects).  This is
    smaller than a regular deck and can be used for testing.

    >>> d = small_deck()
    >>> print hand_string(d)
    9S TS JS QS KS AS 9C TC JC QC KC AC 9D TD JD QD KD AD 9H TH JH QH KH AH
    >>> print len(d)
    24
    """
    d = []
    for suit in range(len(suits)):
        for rank in [7,8,9,10,11,12]:
            c = Card(ranks[rank], suits[suit])
            d.append(c)

    return d



def start_pair(hand):

    """
        Return index of first card in first pair of the hand.
        The index is for the order the hand has after sorting.
        If there are no pairs, return -1.

        Side effect:  The hand is sorted.
    """
    hand.sort()
    start = -1
    for i in range(len(hand)-1, 0, -1):
        if hand[i].rank() == hand[i-1].rank():
            start = i -1
    return start





def drop_pair(hand):
    """
    Remove a pair from the hand (list of card objects) if possible.  Return
    the new hand and the number of pairs dropped (0 or 1).  A "pair" is two
    cards with the same rank.

    If there is more than one pair, only the first is removed.

    The hand MUST be sorted by rank before this function is called.  This
    can be done with:
        hand.sort()

    >>> testhand.sort()
    >>> print hand_string(testhand)
    6C 6D 7S 9H AH
    >>> newhand, pts = drop_pair(testhand)
    >>> print hand_string(newhand)
    7S 9H AH
    >>> print pts
    1
    """
    newhand = hand[:]
    for i in range(len(newhand)-1):
        if newhand[i].rank() == newhand[i+1].rank():
            del(newhand[i+1])
            del(newhand[i])
            return newhand, 1
    return newhand, 0



def hand_string(hand):
    """
    Create a string that represents the cards in the player hand.

    >>> hand_string(testhand)
    '6C 6D 7S 9H AH'
    >>> hand_string([])
    ''
    """

    return " ".join( [c.shortname() for c in hand] )


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
